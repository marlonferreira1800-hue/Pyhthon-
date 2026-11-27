"""Chapter 8 — Basic Functions (`print`, `input`), Formatting, and Type Conversion.

Covers:
- `print()` and safe `input()` (non-blocking on import and resilient to empty stdin)
- Legacy `%s` placeholders, `.format()`, and `f-strings`
- Newline `\\n` formatting (overdue invoice example)
- Variable interaction (`int + float = float`) and `type()`
- Explicit casting (`str()`, `int()`, `float()`)
- `{5}` (`set`) vs `{}` / `{k: v}` (`dict`)
- Concatenating `str + int` safely using `str(15)`

Run:
    python modules/module_01_fundamentals/examples/ch08_basic_functions_casting.py
"""

import sys


def format_three_styles(name: str, age: int) -> dict[str, str]:
    """Compare legacy % masks, .format(), and modern f-strings."""
    percent_style = "Customer: %s | Age: %d years" % (name, age)
    format_style = "Customer: {} | Age: {} years".format(name, age)
    fstring_style = f"Customer: {name} | Age: {age} years"
    return {
        "percent": percent_style,
        "format": format_style,
        "fstring": fstring_style,
    }


def generate_overdue_invoice(customer: str, amount: float, due_date: str) -> str:
    """Use `\\n` line breaks to format a clean overdue invoice."""
    return (
        "=== OVERDUE INVOICE ===\n"
        f"Customer: {customer}\n"
        f"Amount Due: ${amount:.2f}\n"
        f"Due Date: {due_date}"
    )


def demonstrate_interaction_and_casting() -> dict[str, object]:
    """Show `int + float = float`, `{5}` set vs `{k: v}` dict, and `str(15)`."""
    whole_num = 10
    decimal_num = 2.5
    mixed_sum = whole_num + decimal_num  # int + float -> float

    single_set = {5}                 # set!
    empty_dict = {}                  # empty dict!
    populated_dict = {"number": 5}   # dict with key: value!

    # Concatenating str + int directly raises TypeError.
    # Fix: convert integer explicitly via str(15).
    safe_concat = "Recorded age: " + str(15)

    return {
        "mixed_sum": mixed_sum,
        "mixed_sum_type": type(mixed_sum).__name__,
        "braces_5_type": type(single_set).__name__,
        "empty_braces_type": type(empty_dict).__name__,
        "braces_kv_type": type(populated_dict).__name__,
        "safe_concat": safe_concat,
        "conversions": (str(15), int("42"), float("3.5")),
    }


def read_interactive_inputs() -> tuple[str, float, str]:
    """Read input() safely with fallback for EOF or blank input."""
    try:
        customer = input("Customer name [Maria]: ").strip() or "Maria"
        raw_amount = input("Invoice amount [250.00]: ").strip() or "250.00"
        due_date = input("Due date [05/10]: ").strip() or "05/10"
    except (EOFError, OSError):
        return "Maria", 250.0, "05/10"

    try:
        amount = float(raw_amount.replace(",", "."))
    except ValueError:
        amount = 250.0
    return customer, amount, due_date


def main() -> None:
    print("=== Chapter 8: Basic Functions, Formatting, and Type Conversion ===\n")

    if "--interactive" in sys.argv:
        customer, amount, due_date = read_interactive_inputs()
    else:
        customer, amount, due_date = "Maria", 250.0, "05/10"

    styles = format_three_styles(customer, 32)
    print("1) Three string formatting styles:")
    for style_name, rendered in styles.items():
        print(f"   [{style_name}] {rendered}")

    print("\n2) Line breaks (\\n) in an overdue invoice:")
    print(generate_overdue_invoice(customer, amount, due_date))

    details = demonstrate_interaction_and_casting()
    print("\n3) Types, numeric coercion, and explicit casting:")
    print(f"   10 + 2.5 = {details['mixed_sum']} (type {details['mixed_sum_type']})")
    print(f"   type({{5}}) -> {details['braces_5_type']}")
    print(f"   type({{}}) -> {details['empty_braces_type']}")
    print(f"   type({{'number': 5}}) -> {details['braces_kv_type']}")
    print(f"   Safe concatenation with str(15): {details['safe_concat']}")


if __name__ == "__main__":
    main()
