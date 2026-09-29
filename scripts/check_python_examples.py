#!/usr/bin/env python3
"""Audit fenced Python examples in ``src/**/*.md``.

Usage:
    python3 scripts/check_python_examples.py
    python3 scripts/check_python_examples.py --strict

By default, syntax failures return a non-zero exit status. ``--strict`` also
fails for Python fences that cannot be classified reliably, such as an
unterminated fence. The checker intentionally skips placeholders, explicit
fragments/pseudocode, and examples in Common Mistakes or error-example
sections; the rules are kept below as small, named regular expressions.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

PYTHON_FENCE_RE = re.compile(
    r"^ {0,3}(?P<fence>`{3,}|~{3,})\s*(?P<language>python|py)\b[^`~]*$",
    re.IGNORECASE,
)
BLOCKQUOTE_RE = re.compile(r"^ {0,3}> ?")


def unquote(line: str) -> str:
    """Strip Markdown blockquote markers so fenced code inside quotes is audited too."""
    previous = None
    while previous != line:
        previous = line
        line = BLOCKQUOTE_RE.sub("", line)
    return line
HEADING_RE = re.compile(r"^(?P<level>#{1,6})\s+(?P<title>.+?)\s*$")
ERROR_CONTEXT_RE = re.compile(
    r"common mistakes?|common bug|错误示例|错误写法|错误代码|故意.*错|会报错|报错|syntaxerror|语法错|(?:找出|修复|被埋).{0,12}bug|bug.{0,12}(?:找出|修复)",
    re.IGNORECASE,
)
FRAGMENT_CONTEXT_RE = re.compile(
    r"代码片段|片段|伪代码|只展示|省略.*代码|示意",
    re.IGNORECASE,
)
COMMENT_FRAGMENT_RE = re.compile(r"片段|伪代码|示意|省略|此处", re.IGNORECASE)
CONTINUATION_RE = re.compile(r"^(?:elif|else|except|finally|case)\b")


@dataclass
class PythonBlock:
    index: int
    start_line: int
    end_line: int
    source: str
    context: str
    closed: bool


@dataclass
class Finding:
    status: str
    path: Path
    block: PythonBlock
    detail: str


def parse_python_blocks(path: Path) -> list[PythonBlock]:
    """Return fenced Python blocks and their enclosing Markdown headings."""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    blocks: list[PythonBlock] = []
    headings: list[str] = []
    index = 0
    line_number = 0

    while line_number < len(lines):
        line = lines[line_number]
        heading = HEADING_RE.match(line)
        if heading:
            level = len(heading.group("level"))
            headings = headings[: level - 1]
            headings.append(heading.group("title"))

        opening = PYTHON_FENCE_RE.match(unquote(line))
        if not opening:
            line_number += 1
            continue

        index += 1
        fence = opening.group("fence")
        fence_char = re.escape(fence[0])
        closing_re = re.compile(rf"^ {{0,3}}{fence_char}{{{len(fence)},}}\s*$")
        start_line = line_number + 2
        code_start = line_number + 1
        line_number += 1
        code_lines: list[str] = []

        while line_number < len(lines) and not closing_re.match(unquote(lines[line_number])):
            code_lines.append(unquote(lines[line_number]))
            line_number += 1

        closed = line_number < len(lines)
        end_line = line_number if closed else len(lines)
        before = "".join(unquote(item) for item in lines[max(0, code_start - 4):code_start])
        after_start = line_number + 1 if closed else len(lines)
        after = "".join(unquote(item) for item in lines[after_start:after_start + 3])
        context = "\n".join(headings) + "\n" + before + after
        blocks.append(
            PythonBlock(
                index=index,
                start_line=start_line,
                end_line=end_line,
                source="".join(code_lines),
                context=context,
                closed=closed,
            )
        )

        if closed:
            line_number += 1

    return blocks


def skip_reason(block: PythonBlock) -> str | None:
    """Return a documented reason when a block is intentionally non-runnable."""
    if "..." in block.source:
        return "含省略号占位符"
    if ERROR_CONTEXT_RE.search(block.context):
        return "位于错误示例或 Common Mistakes 上下文"
    nonempty_lines = [line.strip() for line in block.source.splitlines() if line.strip()]
    if not nonempty_lines:
        return "空代码块"
    if all(line.startswith("#") for line in nonempty_lines):
        return "仅含注释说明"
    if any(
        line.startswith("#") and COMMENT_FRAGMENT_RE.search(line)
        for line in nonempty_lines
    ):
        return "注释标注为片段或伪代码"
    if FRAGMENT_CONTEXT_RE.search(block.context):
        return "位于片段或伪代码上下文"
    return None


def uncertainty_reason(block: PythonBlock) -> str | None:
    """Identify fences that should be reviewed rather than treated as programs."""
    if not block.closed:
        return "Python fenced 代码块没有闭合"
    first_code_line = next(
        (line for line in block.source.splitlines() if line.strip()), ""
    )
    if first_code_line.startswith((" ", "\t")):
        return "代码块以缩进代码开头，可能是局部片段"
    if CONTINUATION_RE.match(first_code_line):
        return "代码块以续接语句开头，可能是局部片段"
    return None


def check_block(path: Path, block: PythonBlock) -> Finding:
    skipped = skip_reason(block)
    if skipped:
        return Finding("skipped", path, block, skipped)

    uncertain = uncertainty_reason(block)
    if uncertain:
        return Finding("uncertain", path, block, uncertain)

    try:
        compile(block.source, str(path), "exec")
    except SyntaxError as error:
        document_line = block.start_line + (error.lineno or 1) - 1
        message = error.msg or "SyntaxError"
        return Finding("failed", path, block, f"第 {document_line} 行：{message}")
    return Finding("passed", path, block, "语法通过")


def relative_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="检查 src/**/*.md 中 fenced Python 代码块的语法。"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="无法可靠分类的代码块也返回非零状态。",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="项目根目录（默认：脚本所在项目根目录）。",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    source_dir = root / "src"
    if not source_dir.is_dir():
        parser.error(f"找不到源码目录：{source_dir}")

    findings = [
        check_block(path, block)
        for path in sorted(source_dir.rglob("*.md"))
        for block in parse_python_blocks(path)
    ]
    counts = {status: sum(item.status == status for item in findings) for status in (
        "passed", "skipped", "uncertain", "failed"
    )}

    for finding in findings:
        if finding.status not in {"failed", "uncertain"}:
            continue
        label = "失败" if finding.status == "failed" else "待确认"
        print(
            f"[{label}] {relative_path(finding.path, root)} "
            f"代码块 #{finding.block.index}：{finding.detail}"
        )

    print(
        "检查完成："
        f"通过 {counts['passed']}，跳过 {counts['skipped']}，"
        f"待确认 {counts['uncertain']}，失败 {counts['failed']}。"
    )

    if counts["failed"] or (args.strict and counts["uncertain"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
