"""Module 3 — Chapter 17: Functions (def, return, *args, and **kwargs).

Covers built-in vs. imported vs. custom functions, parameterless functions
returning None, parameterized functions with return, *args (tuple), and **kwargs (dict).
"""

import math
import sys


def welcome():
    """Simple parameterless function with no return statement (returns None)."""
    print("Welcome to Module 3 of Python!")


def cube_number(number):
    """Parameterized function returning number raised to the power of 3."""
    return number ** 3


def sum_variadic(*args):
    """Collect variable positional arguments into a TUPLE (not a list)."""
    return {
        "args": args,
        "type": type(args),
        "total": sum(args),
    }


def user_info(**kwargs):
    """Collect variable keyword arguments into a DICT."""
    summary = [f"{key}={value}" for key, value in kwargs.items()]
    return {
        "kwargs": kwargs,
        "type": type(kwargs),
        "summary": ", ".join(summary),
    }


def demonstrate_builtin_and_imported(values: list[int]) -> dict:
    """Contrast built-in functions (len, sum) with imported ones (math.sqrt)."""
    total = sum(values)
    count = len(values)
    sqrt_total = math.sqrt(total) if total >= 0 else 0.0
    return {
        "total": total,
        "count": count,
        "sqrt_total": round(sqrt_total, 4),
    }


def interactive_cube_prompt() -> int | float:
    """Interactive prompt encapsulated in a function so imports never block."""
    raw = input("Enter a number to cube: ")
    number = float(raw) if "." in raw else int(raw)
    result = cube_number(number)
    print(f"{number} cubed is {result}")
    return result


def main() -> None:
    """Run non-blocking demo by default; use --interactive for input() prompt."""
    if "--interactive" in sys.argv:
        interactive_cube_prompt()
        return

    print("=== CH. 17: FUNCTIONS ===")
    return_val = welcome()
    print(f"Return value of welcome() without 'return': {return_val!r}")
    print(f"cube_number(4) = {cube_number(4)}")
    print("sum_variadic(1, 2, 3, 4):", sum_variadic(1, 2, 3, 4))
    print("user_info(name='Ana', track='Python'):", user_info(name="Ana", track="Python"))
    print("Built-in & imported:", demonstrate_builtin_and_imported([4, 5, 7]))


if __name__ == "__main__":
    main()
