"""Chapter 9 — Operators: Assignment, Arithmetic, Logical, Bitwise, and Identity (`is` vs `==`).

Covers:
- Assignment `=` and safe input-driven updates
- Compound assignments (`+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`)
- Arithmetic operators and precedence (`+`, `-`, `*`, `/`, `**`, `//`, `%`)
- Logical operators (`and`, `or`, `not`), truth tables (AND/OR/XOR/NOT), bitwise (`&`, `|`, `^`)
- Book's financial goal: `goal = balance > 0 and salary - expenses >= 0.2 * salary`
- Membership (`in`, `not in`) and relational (`>`, `>=`, `<`, `<=`, `==`, `!=`)
- Identity (`is` vs `==`) with `rent` and `utilities` + CPython memory note

Run:
    python modules/module_02_control_flow_strings/examples/ch09_operators.py
"""

import sys


def compound_assignment_walkthrough(initial: float = 10.0) -> dict[str, float]:
    """Apply all 7 compound assignment operators step by step."""
    steps: dict[str, float] = {}
    val = initial
    val += 5
    steps["after_+="] = val      # 15.0
    val -= 3
    steps["after_-="] = val      # 12.0
    val *= 2
    steps["after_*="] = val      # 24.0
    val /= 4
    steps["after_/="] = val      # 6.0
    val **= 2
    steps["after_**="] = val     # 36.0
    val //= 5
    steps["after_//="] = val     # 7.0
    val %= 4
    steps["after_%="] = val      # 3.0
    return steps


def evaluate_financial_goal(balance: float, salary: float, expenses: float) -> bool:
    """Reverse-engineered financial goal from Chapter 9."""
    # Order of operations:
    # 1. `0.2 * salary` and `salary - expenses`
    # 2. `balance > 0` and `>=` comparisons
    # 3. `and` evaluates both boolean results
    goal = balance > 0 and salary - expenses >= 0.2 * salary
    return goal


def generate_truth_table() -> list[dict[str, bool]]:
    """Build complete AND, OR, XOR, and NOT truth table rows."""
    rows: list[dict[str, bool]] = []
    for a in (True, False):
        for b in (True, False):
            rows.append(
                {
                    "A": a,
                    "B": b,
                    "AND": a and b,
                    "OR": a or b,
                    "XOR": a ^ b,
                    "NOT_A": not a,
                }
            )
    return rows


def demonstrate_bitwise_operators(x: int = 6, y: int = 3) -> dict[str, int]:
    """Show bitwise AND (&), OR (|), and XOR (^) on integers."""
    # 6 in binary: 110 | 3 in binary: 011
    return {
        "and": x & y,   # 010 -> 2
        "or": x | y,    # 111 -> 7
        "xor": x ^ y,   # 101 -> 5
    }


def compare_identity_vs_equality() -> dict[str, object]:
    """Demonstrate `is` (memory identity) vs `==` (value equality) using rent/utilities."""
    rent = int("1000")
    utilities = int("1000")
    shared_alias = rent

    return {
        "rent": rent,
        "utilities": utilities,
        "value_equal": rent == utilities,
        "distinct_objects_is": rent is utilities,
        "shared_alias_is": rent is shared_alias,
        "ids": (id(rent), id(utilities), id(shared_alias)),
    }


def read_balance_update(current_balance: float) -> float:
    """Safely update a balance via input() with EOF/blank fallback."""
    try:
        raw = input("Deposit amount to add [50.0]: ").strip() or "50.0"
    except (EOFError, OSError):
        raw = "50.0"
    try:
        deposit = float(raw.replace(",", "."))
    except ValueError:
        deposit = 50.0
    return current_balance + deposit


def main() -> None:
    print("=== Chapter 9: Operators ===\n")

    balance = 100.0
    if "--interactive" in sys.argv:
        balance = read_balance_update(balance)
    else:
        balance = balance + 50.0
    print(f"1) Reassigned balance: {balance}")

    print("2) Compound assignments from 10.0:", compound_assignment_walkthrough(10.0))
    print("3) Precedence: 2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2, "| (2 + 3) * 4 ** 2 =", (2 + 3) * 4 ** 2)

    print("\n4) Truth Table (AND / OR / XOR / NOT):")
    for row in generate_truth_table():
        print(
            f"   A={str(row['A']):5s} B={str(row['B']):5s} | "
            f"AND={str(row['AND']):5s} OR={str(row['OR']):5s} "
            f"XOR={str(row['XOR']):5s} NOT_A={str(row['NOT_A']):5s}"
        )

    print("\n5) Bitwise operators on 6 (110) and 3 (011):", demonstrate_bitwise_operators(6, 3))
    print(
        "6) Financial goal (balance=500, salary=4000, expenses=2800):",
        evaluate_financial_goal(500.0, 4000.0, 2800.0),
    )

    fruits = ["apple", "banana", "grape"]
    print("7) Membership: 'apple' in fruits ->", "apple" in fruits, "| 'pear' not in fruits ->", "pear" not in fruits)

    identity_info = compare_identity_vs_equality()
    print("\n8) Identity (`is`) vs. Equality (`==`) with rent=1000 & utilities=1000:")
    print(f"   rent == utilities -> {identity_info['value_equal']} (compares VALUE)")
    print(f"   rent is utilities -> {identity_info['distinct_objects_is']} (compares MEMORY id)")
    print(f"   rent is shared_alias -> {identity_info['shared_alias_is']} (same object in RAM)")


if __name__ == "__main__":
    main()
