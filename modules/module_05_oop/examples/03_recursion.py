"""Module 5 (Ch. 21) — Applying Recursion (book example + OOP tree traversal).

Demonstrates stopping condition (base case), call stack trace, and
hierarchical traversal inside a class.
"""


def print_sequence(maximum: int, current: int = 1) -> list[int]:
    """Adaptation of the book's recursive counter `imprimir(maximo, atual)`.

    Base case: when `current > maximum`, return an empty list without
    spawning another stack frame.
    """
    if current > maximum:
        return []
    print(f"  [stack push] current = {current}")
    rest = print_sequence(maximum, current + 1)
    print(f"  [stack pop ] current = {current}")
    return [current] + rest


def factorial(n: int) -> int:
    """Classic mathematical recursion with input validation."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers.")
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)


class FleetCategory:
    """Tree node demonstrating recursion in Object-Oriented Programming."""

    def __init__(self, name: str, direct_count: int = 0) -> None:
        self.name = name
        self.direct_count = direct_count
        self.subcategories: list[FleetCategory] = []

    def add_subcategory(self, sub: "FleetCategory") -> None:
        self.subcategories.append(sub)

    def count_total_vehicles(self) -> int:
        """Sums vehicles in this node plus all descendant categories recursively."""
        total = self.direct_count
        # Implicit base case: when self.subcategories is empty, the loop does not run.
        for sub in self.subcategories:
            total += sub.count_total_vehicles()
        return total

    def format_tree(self, level: int = 0) -> list[str]:
        """Builds an indented hierarchy representation via recursion."""
        lines = [f"{'  ' * level}- {self.name} ({self.direct_count} direct)"]
        for sub in self.subcategories:
            lines.extend(sub.format_tree(level + 1))
        return lines


def demonstrate_recursion() -> None:
    print("=== 1. Book recursive counter with call stack trace ===")
    seq = print_sequence(4, 1)
    print("Returned sequence:", seq)

    print("\n=== 2. Recursive factorial ===")
    print("5! =", factorial(5))

    print("\n=== 3. Recursion in an OOP fleet category tree ===")
    root = FleetCategory("Entire Fleet", 0)
    passenger = FleetCategory("Passenger", 2)
    passenger.add_subcategory(FleetCategory("Economy", 5))
    passenger.add_subcategory(FleetCategory("Executive", 3))
    utility = FleetCategory("Utility", 4)

    root.add_subcategory(passenger)
    root.add_subcategory(utility)

    for line in root.format_tree():
        print(line)
    print("Total consolidated vehicles in tree:", root.count_total_vehicles())


if __name__ == "__main__":
    demonstrate_recursion()
