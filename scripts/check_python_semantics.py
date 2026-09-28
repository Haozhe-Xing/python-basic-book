#!/usr/bin/env python3
"""Run semantic regression tests for selected runnable examples in the book.

Usage:
    python3 scripts/check_python_semantics.py
    python3 scripts/check_python_semantics.py --list

This script deliberately tests a small, explicit registry of stable examples.
Unlike ``check_python_examples.py``, it executes examples and checks their
results. Interactive, GUI, network, random, and teaching-fragment examples are
kept out of this suite on purpose.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from check_python_examples import PythonBlock, parse_python_blocks


@dataclass(frozen=True)
class ExampleTest:
    """One stable textbook example and the behavior it promises."""

    name: str
    source_path: str
    marker: str
    check: Callable[[dict[str, object]], None]
    block_index: int | None = None


def find_block(root: Path, test: ExampleTest) -> PythonBlock:
    """Find a documented Python fence and verify its stable marker is still present."""
    path = root / test.source_path
    blocks = parse_python_blocks(path)
    if test.block_index is not None:
        matches = [block for block in blocks if block.index == test.block_index]
        if len(matches) != 1 or test.marker not in matches[0].source:
            raise RuntimeError(
                f"定位失败：{test.source_path} 的代码块 #{test.block_index} 已不包含标记 {test.marker!r}"
            )
        return matches[0]

    matches = [block for block in blocks if test.marker in block.source]
    if len(matches) != 1:
        raise RuntimeError(
            f"定位失败：标记 {test.marker!r} 在 {test.source_path} 中匹配 {len(matches)} 个代码块"
        )
    return matches[0]


def run_example(root: Path, test: ExampleTest) -> None:
    """Execute a fenced example in isolation, then assert its promised behavior."""
    block = find_block(root, test)
    namespace: dict[str, object] = {"__name__": "__example_test__"}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(block.source, f"{test.source_path}:{block.start_line}", "exec"), namespace)
    test.check(namespace)


def function(namespace: dict[str, object], name: str):
    value = namespace.get(name)
    if not callable(value):
        raise AssertionError(f"没有得到可调用函数 {name}()")
    return value


def check_binary_search(namespace: dict[str, object]) -> None:
    search = function(namespace, "binary_search")
    assert search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23) == 5
    assert search([1, 3, 5], 2) == -1
    assert search([], 1) == -1


def check_dedupe_and_sort(namespace: dict[str, object]) -> None:
    dedupe = function(namespace, "dedupe_and_sort")
    assert dedupe([5, 3, 9, 3, 5, 1, 9, 7, 1]) == [1, 3, 5, 7, 9]
    assert dedupe([]) == []


def check_climb_stairs(namespace: dict[str, object]) -> None:
    recursive = function(namespace, "climb_rec")
    memoized = function(namespace, "climb_memo")
    dynamic = function(namespace, "climb_dp")
    assert dynamic(0) == 1
    assert dynamic(10) == 89
    assert recursive(5) == memoized(5) == dynamic(5) == 8


def check_sorting(namespace: dict[str, object], name: str) -> None:
    sort = function(namespace, name)
    source = [5, 3, 8, 1, 9, 2]
    assert sort(source) == [1, 2, 3, 5, 8, 9]
    assert source == [5, 3, 8, 1, 9, 2], "示例承诺不修改原列表"
    assert sort([1, 2, 2, 3]) == [1, 2, 2, 3]


def check_merge_sort(namespace: dict[str, object]) -> None:
    merge_sort = function(namespace, "merge_sort")
    merge = function(namespace, "merge")
    source = [38, 27, 43, 3, 9, 82, 10]
    assert merge_sort(source) == [3, 9, 10, 27, 38, 43, 82]
    assert merge([1, 4, 7], [2, 3, 8]) == [1, 2, 3, 4, 7, 8]
    assert source == [38, 27, 43, 3, 9, 82, 10]


def check_fibonacci(namespace: dict[str, object]) -> None:
    fib = function(namespace, "fib")
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(50) == 12_586_269_025


def check_parentheses(namespace: dict[str, object]) -> None:
    balanced = function(namespace, "is_balanced")
    assert balanced("()()()") is True
    assert balanced("(()") is False
    assert balanced("())") is False
    assert balanced("(a)") is True


def check_activity_selection(namespace: dict[str, object]) -> None:
    select = function(namespace, "max_activities")
    assert select([(1, 3), (2, 5), (4, 6), (6, 8)]) == 3
    assert select([]) == 0


def check_backspace(namespace: dict[str, object]) -> None:
    simulate = function(namespace, "type_and_backspace")
    assert simulate("abc#d") == "abd"
    assert simulate("a##b") == "b"
    assert simulate("a#b#c") == "c"


def check_coins(namespace: dict[str, object]) -> None:
    count = function(namespace, "min_coins")
    assert count(67) == 6
    assert count(93) == 8
    assert count(0) == 0


def check_waiting_time(namespace: dict[str, object]) -> None:
    total = function(namespace, "total_wait")
    assert total([3, 1, 2]) == 4
    assert total([8, 2, 5, 1, 4]) == 23
    assert total([]) == 0


def check_text_adventure(namespace: dict[str, object]) -> None:
    go = function(namespace, "go")
    play = function(namespace, "play")
    inventory = namespace.get("inventory")
    assert isinstance(inventory, list), "没有得到背包列表 inventory"

    namespace["current"] = "entrance"
    inventory.clear()
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        go("west")
    assert namespace["current"] == "entrance", "非法移动不应改变当前位置"
    assert "走不通" in output.getvalue()

    with contextlib.redirect_stdout(io.StringIO()):
        go("north")
        go("take")
        go("take")
    assert namespace["current"] == "hall"
    assert inventory == ["key"], "拿同一物品两次不应重复放入背包"

    namespace["current"] = "entrance"
    inventory.clear()
    commands = iter(["north", "take", "down", "open"])
    namespace["input"] = lambda _prompt: next(commands)
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        play()
    assert namespace["current"] == "treasure"
    assert inventory == ["key"]
    assert "通关！你用一把钥匙解开了古堡的秘密。" in output.getvalue()


def check_visitor_profiles(namespace: dict[str, object]) -> None:
    check_in = function(namespace, "check_in")
    ride = function(namespace, "ride")
    profile = function(namespace, "profile")
    champion = function(namespace, "champion")
    visitors = namespace.get("visitors")
    assert isinstance(visitors, list), "没有得到游客档案列表 visitors"

    visitors.clear()
    with contextlib.redirect_stdout(io.StringIO()):
        check_in("小云")
        check_in("小雨")
        ride("小云", "过山车", 50)
        ride("小云", "过山车", 50)
        ride("小云", "摩天轮", 30)
        ride("小雨", "碰碰车", 40)

    assert visitors == [
        {"name": "小云", "score": 80, "played": ["过山车", "摩天轮"]},
        {"name": "小雨", "score": 40, "played": ["碰碰车"]},
    ]

    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        profile("小云")
        champion()
    text = output.getvalue()
    assert "小云：80 分，玩过 ['过山车', '摩天轮']" in text
    assert "冠军：小云，80 分" in text


def check_visitor_export(namespace: dict[str, object]) -> None:
    data = namespace.get("data")
    text = namespace.get("text")
    back = namespace.get("back")
    assert isinstance(text, str), "没有得到 JSON 导出文本 text"
    assert back == data, "JSON 导出后应能完整读回原嵌套数据"
    assert "小明" in text, "ensure_ascii=False 应保留中文字符"
    assert back["visitors"][0]["score"] == 80


def check_data_analysis(namespace: dict[str, object]) -> None:
    scores = namespace.get("scores")
    ranked = namespace.get("ranked")
    assert scores == {"小明": 92, "小红": 78, "小刚": 85, "小丽": 96, "小强": 64, "小芳": 88}
    assert namespace.get("highest") == 96
    assert namespace.get("lowest") == 64
    assert namespace.get("average") == sum(scores.values()) / len(scores)
    assert ranked == [("小丽", 96), ("小明", 92), ("小芳", 88), ("小刚", 85), ("小红", 78), ("小强", 64)]


def check_ticket_validation(namespace: dict[str, object]) -> None:
    parse = function(namespace, "parse_ticket_count")
    assert parse(" 3 ") == 3
    for bad in ("三", "0", "11"):
        try:
            parse(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"非法票数 {bad!r} 应触发 ValueError")


def check_file_round_trip(namespace: dict[str, object]) -> None:
    save_json = function(namespace, "save_json")
    save_csv = function(namespace, "save_csv")
    load_json = function(namespace, "load_json")
    players = [{"name": "小云", "score": 80}, {"name": "小雨", "score": 95}]

    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        json_path = root / "scores.json"
        csv_path = root / "scores.csv"
        save_json(json_path, players)
        save_csv(csv_path, players)
        assert load_json(json_path) == players
        assert load_json(root / "missing.json") == []
        assert "小云" in json_path.read_text(encoding="utf-8")
        csv_text = csv_path.read_text(encoding="utf-8")
        assert "name,score" in csv_text and "小雨,95" in csv_text


def check_score_rule_tests(namespace: dict[str, object]) -> None:
    level = function(namespace, "level_for_score")
    run_tests = function(namespace, "run_tests")
    assert level(0) == "继续加油"
    assert level(60) == "银牌"
    assert level(90) == "金牌"
    for bad in (-1, 101):
        try:
            level(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"非法分数 {bad} 应触发 ValueError")
    with contextlib.redirect_stdout(io.StringIO()):
        run_tests()


TESTS = [
    ExampleTest("二分查找", "src/projects/algorithm-arena.md", "def binary_search(arr, target):", check_binary_search),
    ExampleTest("去重排序", "src/projects/algorithm-arena.md", "def dedupe_and_sort(nums):", check_dedupe_and_sort),
    ExampleTest("爬楼梯三种解法", "src/projects/algorithm-arena.md", "def climb_rec(n):", check_climb_stairs),
    ExampleTest("冒泡排序", "src/algorithms/sorting.md", "def bubble_sort(a):", lambda ns: check_sorting(ns, "bubble_sort")),
    ExampleTest("选择排序", "src/algorithms/sorting.md", "def selection_sort(a):", lambda ns: check_sorting(ns, "selection_sort")),
    ExampleTest("插入排序", "src/algorithms/sorting.md", "def insertion_sort(a):", lambda ns: check_sorting(ns, "insertion_sort")),
    ExampleTest("归并排序", "src/algorithms/recursion-divide.md", "def merge_sort(arr):", check_merge_sort, block_index=2),
    ExampleTest("记忆化斐波那契", "src/algorithms/recursion-divide.md", "def fib(n, memo=None):", check_fibonacci, block_index=5),
    ExampleTest("括号配对", "src/algorithms/basic-structures.md", "def is_balanced(s):", check_parentheses),
    ExampleTest("活动选择", "src/algorithms/greedy-simulation.md", "def max_activities(intervals):", check_activity_selection),
    ExampleTest("退格模拟", "src/algorithms/greedy-simulation.md", "def type_and_backspace(s):", check_backspace, block_index=2),
    ExampleTest("贪心找零", "src/algorithms/greedy-simulation.md", "def min_coins(amount):", check_coins, block_index=3),
    ExampleTest("最短总等待", "src/algorithms/greedy-simulation.md", "def total_wait(times):", check_waiting_time, block_index=4),
    ExampleTest("文字冒险：非法移动、拿钥匙与通关", "src/projects/text-adventure.md", "def play():", check_text_adventure, block_index=5),
    ExampleTest("游客档案：建档、去重计分与冠军", "src/data-structures/nested-data.md", "# 算法游乐场 · 完整游客档案（嵌套数据版）", check_visitor_profiles, block_index=13),
    ExampleTest("游客档案：JSON 导出与读回", "src/data-structures/nested-data.md", "text = json.dumps(data, ensure_ascii=False, indent=2)", check_visitor_export, block_index=17),
    ExampleTest("班级成绩：统计与排行榜", "src/projects/data-analysis.md", "ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)", check_data_analysis, block_index=8),
    ExampleTest("异常处理：票数转换与范围校验", "src/functions/exceptions.md", "def parse_ticket_count(text):", check_ticket_validation, block_index=10),
    ExampleTest("文件数据：JSON 与 CSV 往返", "src/functions/files-data.md", "def save_json(path, players):", check_file_round_trip, block_index=16),
    ExampleTest("类型与测试：计分边界", "src/functions/testing-types.md", "def level_for_score(score: int) -> str:", check_score_rule_tests, block_index=15),
]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="执行书中已登记完整代码示例的语义回归测试。"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="项目根目录（默认：脚本所在项目根目录）。",
    )
    parser.add_argument("--list", action="store_true", help="只列出当前覆盖的示例。")
    args = parser.parse_args()
    root = args.root.resolve()

    if args.list:
        for test in TESTS:
            print(f"- {test.name}：{test.source_path}")
        print(f"共 {len(TESTS)} 个语义回归测试。")
        return 0

    failures: list[tuple[ExampleTest, Exception]] = []
    for test in TESTS:
        try:
            run_example(root, test)
        except Exception as error:  # Show every failed promise in one run.
            failures.append((test, error))
            print(f"[失败] {test.name}（{test.source_path}）：{error}")
        else:
            print(f"[通过] {test.name}")

    print(f"语义测试完成：通过 {len(TESTS) - len(failures)}，失败 {len(failures)}，共 {len(TESTS)}。")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
