"""Chapter 10 — Conditional Structures (`if`, `elif`, `else`, and `switch/case` patterns).

Covers:
- `go_to_the_market` conditional algorithm
- Grade classification (`>= 9`, `>= 7`, `>= 5`, `else`)
- `and` / `or` inside conditionals and nested conditionals
- Simulating `switch/case` via `class Color` + `if/elif`, dictionary mapping, and Python 3.10+ `match/case`

Run:
    python modules/module_02_control_flow_strings/examples/ch10_conditionals.py
"""


class Color:
    """Symbolic constants used to simulate switch/case cleanly."""

    RED = 1
    GREEN = 2
    BLUE = 3


def go_to_the_market(
    item_needed: str,
    budget: float,
    item_price: float,
    is_raining: bool,
    has_umbrella: bool,
) -> str:
    """Model the book's `go_to_the_market` algorithm with nested/combined checks."""
    if is_raining and not has_umbrella:
        return "Wait for the rain to stop before leaving."
    if budget >= item_price:
        remaining = budget - item_price
        return f"Bought '{item_needed}'. Remaining budget: ${remaining:.2f}."
    return f"Insufficient budget for '{item_needed}'; return home and adjust list."


def classify_grade(grade: float) -> str:
    """Classify a numeric score (0..10) using ordered `if/elif/else` bands."""
    if grade < 0 or grade > 10:
        raise ValueError("Grade must be between 0 and 10.")
    if grade >= 9:
        return "Excellent"
    elif grade >= 7:
        return "Good"
    elif grade >= 5:
        return "Recovery"
    else:
        return "Failed"


def check_store_discount(
    balance: float,
    order_total: float,
    is_vip: bool,
    is_student: bool,
    age: int,
) -> str:
    """Demonstrate `and`/`or` in conditionals plus nested `if` branching."""
    if balance >= order_total:
        if is_vip and (is_student or age >= 60):
            return "Purchase approved with VIP + Priority discount (20%)."
        elif is_vip or is_student or age >= 60:
            return "Purchase approved with standard discount (10%)."
        return "Purchase approved at regular price."
    return "Purchase declined: insufficient balance."


def select_color_if_elif(code: int) -> str:
    """Classic switch/case simulation using `class Color` and `if/elif/else`."""
    if code == Color.RED:
        return "Selected Red"
    elif code == Color.GREEN:
        return "Selected Green"
    elif code == Color.BLUE:
        return "Selected Blue"
    else:
        return "Unknown color"


def select_color_dict(code: int) -> str:
    """Idiomatic switch/case simulation using a dictionary mapping."""
    mapping = {
        Color.RED: "Selected Red",
        Color.GREEN: "Selected Green",
        Color.BLUE: "Selected Blue",
    }
    return mapping.get(code, "Unknown color")


def select_color_match_case(code: int) -> str:
    """Native Python 3.10+ structural pattern matching (`match` / `case`)."""
    match code:
        case Color.RED:
            return "Selected Red"
        case Color.GREEN:
            return "Selected Green"
        case Color.BLUE:
            return "Selected Blue"
        case _:
            return "Unknown color"


def main() -> None:
    print("=== Chapter 10: Conditional Structures ===\n")

    print("1) go_to_the_market:")
    print("  -", go_to_the_market("Coffee", 30.0, 18.5, is_raining=True, has_umbrella=True))
    print("  -", go_to_the_market("Coffee", 10.0, 18.5, is_raining=False, has_umbrella=False))

    print("\n2) Grade classification:")
    for score in (9.5, 7.5, 5.5, 3.0):
        print(f"  - Grade {score:4.1f} -> {classify_grade(score)}")

    print("\n3) Nested conditionals with and/or:")
    print("  -", check_store_discount(200.0, 120.0, is_vip=True, is_student=True, age=22))
    print("  -", check_store_discount(50.0, 120.0, is_vip=False, is_student=False, age=30))

    print("\n4) Simulating switch/case (if/elif vs dict vs Python 3.10+ match/case):")
    for code in (Color.RED, Color.GREEN, Color.BLUE, 99):
        print(
            f"  code={code:2d} -> if/elif: {select_color_if_elif(code)} | "
            f"dict: {select_color_dict(code)} | match: {select_color_match_case(code)}"
        )


if __name__ == "__main__":
    main()
