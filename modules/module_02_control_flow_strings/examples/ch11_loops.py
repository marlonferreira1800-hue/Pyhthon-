"""Chapter 11 — Repetition Structures (`while`, `for`, `range`, `for...else`).

Covers:
- `while` loop with increment and `break`
- `for` iterating over a `groceries` list
- `range(0, 6)` vs `range(6)`
- `for ... else` (search completion without `break`)
- Nested `for` generating the full `0x0` through `10x10` multiplication table

Run:
    python modules/module_02_control_flow_strings/examples/ch11_loops.py
"""


def count_until_break(limit: int, stop_at: int) -> list[int]:
    """Demonstrate `while` with explicit increment and `break`."""
    visited: list[int] = []
    counter = 0
    while counter < limit:
        if counter == stop_at:
            break
        visited.append(counter)
        counter += 1
    return visited


def list_groceries(groceries: list[str]) -> list[str]:
    """Format a grocery list using a `for` loop with 1-based numbering."""
    formatted: list[str] = []
    for index, item in enumerate(groceries, start=1):
        formatted.append(f"{index}. {item}")
    return formatted


def search_with_for_else(items: list[str], target: str) -> str:
    """Use `for ... else` to report when an item is missing without a flag variable."""
    for item in items:
        if item == target:
            return f"Found '{target}' in list."
    else:
        return f"'{target}' was not found."


def build_multiplication_table(max_factor: int = 10) -> list[str]:
    """Generate the complete multiplication table from 0x0 to max_factor x max_factor."""
    lines: list[str] = []
    for a in range(max_factor + 1):
        for b in range(max_factor + 1):
            lines.append(f"{a} x {b} = {a * b}")
    return lines


def main() -> None:
    print("=== Chapter 11: Repetition Structures ===\n")

    print("1) while with increment and break (limit=10, stop_at=5):")
    print("  ", count_until_break(10, 5))

    groceries = ["rice", "beans", "coffee", "milk"]
    print("\n2) for over groceries list:")
    for line in list_groceries(groceries):
        print("  ", line)

    print("\n3) range(0, 6) == range(6):", list(range(0, 6)) == list(range(6)), list(range(6)))

    print("\n4) for ... else search:")
    print("  -", search_with_for_else(groceries, "coffee"))
    print("  -", search_with_for_else(groceries, "chocolate"))

    table = build_multiplication_table(10)
    print(f"\n5) Nested for multiplication table (0x0 to 10x10): {len(table)} entries")
    print("   First 5:", table[:5])
    print("   Last 5: ", table[-5:])


if __name__ == "__main__":
    main()
