"""Solved exercises for Module 2 (Chapters 9 to 12).

All functions are pure and testable (no blocking `input()` calls).

Run directly:
    python modules/module_02_control_flow_strings/solutions/solved_exercises.py
"""

from math import pi


class Color:
    """Symbolic constants used for switch/case simulations."""

    RED = 1
    GREEN = 2
    BLUE = 3


def ex01_financial_goal_and_compound(
    initial_balance: float,
    deposit: float,
    salary: float,
    expenses: float,
) -> dict[str, object]:
    """Update balance using `+=` and evaluate the financial goal expression."""
    balance = initial_balance
    balance += deposit
    goal_met = balance > 0 and salary - expenses >= 0.2 * salary
    return {
        "updated_balance": round(balance, 2),
        "savings_margin": round(salary - expenses, 2),
        "goal_met": goal_met,
    }


def ex02_truth_and_bitwise_summary(
    a: bool,
    b: bool,
    int_x: int,
    int_y: int,
) -> dict[str, object]:
    """Compute logical (AND/OR/XOR/NOT) and bitwise (&/|/^) results."""
    return {
        "logical": {
            "and": a and b,
            "or": a or b,
            "xor": bool(a) ^ bool(b),
            "not_a": not a,
        },
        "bitwise": {
            "and": int_x & int_y,
            "or": int_x | int_y,
            "xor": int_x ^ int_y,
        },
    }


def ex03_compare_identity_and_equality(
    rent_value: int,
    utilities_value: int,
) -> dict[str, object]:
    """Contrast value equality (`==`) against memory identity (`is`)."""
    rent_obj = int(str(rent_value))
    utilities_obj = int(str(utilities_value))
    alias = rent_obj

    return {
        "equal_value": rent_obj == utilities_obj,
        "alias_same_identity": rent_obj is alias,
        "independent_same_identity": rent_obj is utilities_obj,
    }


def ex04_classify_grade_and_market(
    grade: float,
    budget: float,
    price: float,
) -> dict[str, str]:
    """Classify a 0..10 grade and decide market purchase affordability."""
    if grade < 0 or grade > 10:
        raise ValueError("Grade must be between 0 and 10.")
    if grade >= 9:
        grade_status = "Excellent"
    elif grade >= 7:
        grade_status = "Good"
    elif grade >= 5:
        grade_status = "Recovery"
    else:
        grade_status = "Failed"

    market_status = "Bought" if budget >= price else "Insufficient budget"
    return {
        "grade_status": grade_status,
        "market_status": market_status,
    }


def ex05_dispatch_color_switch(code: int) -> dict[str, str]:
    """Simulate switch/case via if/elif/else, dictionary dispatch, and match/case."""
    if code == Color.RED:
        if_elif_result = "Red"
    elif code == Color.GREEN:
        if_elif_result = "Green"
    elif code == Color.BLUE:
        if_elif_result = "Blue"
    else:
        if_elif_result = "Unknown"

    dict_result = {
        Color.RED: "Red",
        Color.GREEN: "Green",
        Color.BLUE: "Blue",
    }.get(code, "Unknown")

    match code:
        case Color.RED:
            match_result = "Red"
        case Color.GREEN:
            match_result = "Green"
        case Color.BLUE:
            match_result = "Blue"
        case _:
            match_result = "Unknown"

    return {
        "if_elif": if_elif_result,
        "dict": dict_result,
        "match_case": match_result,
    }


def ex06_while_break_and_for_search(
    items: list[str],
    target: str,
    limit: int,
    stop_at: int,
) -> dict[str, object]:
    """Collect sequence via `while` + `break` and search `items` via `for...else`."""
    collected: list[int] = []
    counter = 0
    while counter < limit:
        if counter == stop_at:
            break
        collected.append(counter)
        counter += 1

    for item in items:
        if item == target:
            search_status = "found"
            break
    else:
        search_status = "not_found"

    return {
        "collected": collected,
        "search_status": search_status,
    }


def ex07_multiplication_table(start: int = 0, end: int = 10) -> list[str]:
    """Generate multiplication table lines from `start` to `end` inclusive."""
    if start < 0 or start > end:
        raise ValueError("Require 0 <= start <= end.")
    lines: list[str] = []
    for a in range(start, end + 1):
        for b in range(start, end + 1):
            lines.append(f"{a} x {b} = {a * b}")
    return lines


def ex08_string_pipeline_ansi(
    raw_csv: str,
    search_term: str,
    value: float,
) -> dict[str, object]:
    """Practice immutability, `.split()`, `in`, `.center()`, ANSI, and numeric formatting."""
    snapshot_before = raw_csv
    preview_upper = raw_csv.upper()
    original_unchanged = raw_csv == snapshot_before
    tokens = [token.strip() for token in raw_csv.split(",") if token.strip()]
    term_found = search_term.lower() in raw_csv.lower()
    centered_header = " REPORT ".center(30, "-")
    ansi_tag = f"\033[91m{search_term}\033[0m"

    return {
        "original_unchanged": original_unchanged,
        "upper_preview": preview_upper,
        "tokens": tokens,
        "term_found": term_found,
        "centered_header": centered_header,
        "ansi_tag": ansi_tag,
        "legacy_2": "%.2f" % value,
        "legacy_5": "%.5f" % value,
        "modern_2": f"{value:.2f}",
    }


def main() -> None:
    print("=== Module 2 Solved Exercises ===")
    print("Ex 01:", ex01_financial_goal_and_compound(100.0, 50.0, 4000.0, 2800.0))
    print("Ex 02:", ex02_truth_and_bitwise_summary(True, False, 6, 3))
    print("Ex 03:", ex03_compare_identity_and_equality(1000, 1000))
    print("Ex 04:", ex04_classify_grade_and_market(8.5, 50.0, 35.0))
    print("Ex 05:", ex05_dispatch_color_switch(Color.GREEN))
    print("Ex 06:", ex06_while_break_and_for_search(["rice", "beans"], "beans", 10, 4))
    print("Ex 07 count (0..10):", len(ex07_multiplication_table(0, 10)))
    print("Ex 08:", ex08_string_pipeline_ansi("Python,Strings,ANSI", "ansi", pi))


if __name__ == "__main__":
    main()
