"""Chapter 7 — Variables / Objects, Memory Drawers, and Naming Rules.

Covers:
- Memory drawer analogy (`id()`)
- Dynamic typing
- Case sensitivity (`NAME` vs `name`)
- Naming rules (allowed, discouraged, forbidden)
- Multiple assignment (`name, age, gender, height = 'Maria', 32, 'F', 1.89`)
- Chained assignment (`num1 = x = a1 = 10`)

Run:
    python modules/module_01_fundamentals/examples/ch07_variables_objects.py
"""

import keyword


def demonstrate_dynamic_typing_and_case() -> dict[str, object]:
    """Show dynamic type rebinding and case sensitivity (`NAME` vs `name`)."""
    variable = 100
    initial_type = type(variable).__name__

    # Dynamic typing: the same label now points to a `str` object
    variable = "one hundred"
    final_type = type(variable).__name__

    # Case sensitivity: NAME and name are completely distinct objects
    NAME = "CONSTANT_OR_OTHER_VAR"
    name = "Maria"

    return {
        "initial_type": initial_type,
        "final_type": final_type,
        "NAME": NAME,
        "name": name,
        "are_equal": NAME == name,
    }


def demonstrate_multiple_and_chained_assignment() -> dict[str, object]:
    """Run the book's classic multiple and chained assignment examples."""
    # Multiple assignment (positional unpacking)
    name, age, gender, height = "Maria", 32, "F", 1.89

    # Chained assignment (all labels initially refer to the same `10` object)
    num1 = x = a1 = 10
    shared_initial_id = id(num1) == id(x) == id(a1)

    return {
        "person": (name, age, gender, height),
        "chained": (num1, x, a1),
        "shared_initial_id": shared_initial_id,
    }


def validate_variable_name(identifier: str) -> str:
    """Classify a candidate variable name by Python syntax and PEP 8 rules."""
    if identifier in keyword.kwlist:
        return "forbidden: reserved keyword"
    if not identifier.isidentifier():
        return "forbidden: invalid syntax (space, leading digit, or symbol)"
    if not identifier.isascii() or any(ch.isupper() for ch in identifier):
        return "allowed, discouraged (non-ASCII accent or uppercase in regular variable)"
    return "allowed and recommended (snake_case)"


def main() -> None:
    print("=== Chapter 7: Variables and Objects ===\n")

    dynamic = demonstrate_dynamic_typing_and_case()
    print("1) Dynamic typing and case sensitivity:")
    print(f"   Type changed from {dynamic['initial_type']} to {dynamic['final_type']}")
    print(f"   NAME={dynamic['NAME']!r} != name={dynamic['name']!r}")

    multi = demonstrate_multiple_and_chained_assignment()
    print("\n2) Multiple and chained assignment:")
    print("   Multiple:", multi["person"])
    print("   Chained (num1 = x = a1 = 10):", multi["chained"])
    print("   Shared initial memory id()?", multi["shared_initial_id"])

    print("\n3) Naming validation:")
    samples = ["student_name", "salário", "NAME", "1score", "my name", "class"]
    for ident in samples:
        print(f"   {ident!r:14s} -> {validate_variable_name(ident)}")


if __name__ == "__main__":
    main()
