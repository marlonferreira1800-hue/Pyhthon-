"""Chapter 4 — Basic Program Structure ("Batteries Included").

Run:
    python modules/module_01_fundamentals/examples/ch04_basic_structure.py
"""

import datetime
import math


def basic_greeting() -> str:
    """Return the classic Chapter 4 greeting."""
    return "Hello World!!!"


def demonstrate_batteries_included() -> dict[str, object]:
    """Use built-in standard library modules without external installs."""
    current_year = datetime.date.today().year
    sqrt_144 = math.sqrt(144)
    return {
        "current_year": current_year,
        "sqrt_of_144": sqrt_144,
    }


def main() -> None:
    print("=== Chapter 4: Basic Structure & Batteries Included ===\n")

    # Call anatomy: function_name(arguments_inside_parentheses)
    print(basic_greeting())

    # Keyword arguments of print(): sep (separator) and end (line terminator)
    print("Python", "Batteries", "Included", sep=" | ", end=".\n")

    data = demonstrate_batteries_included()
    print(f"Year (datetime module): {data['current_year']}")
    print(f"Square root of 144 (math module): {data['sqrt_of_144']}")


if __name__ == "__main__":
    main()
