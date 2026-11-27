"""Chapter 6 — Comments, Docstrings, and Assigned Triple-Quoted Strings.

Demonstrates:
- Single-line comments with `#`
- Commenting out lines to isolate tests (`# total = var1 + var2`)
- Standalone triple-quoted strings vs triple-quoted strings assigned to a variable

Run:
    python modules/module_01_fundamentals/examples/ch06_comments.py
"""


def compute_with_isolated_line(var1: int, var2: int) -> int:
    """Show the practical debugging habit of commenting out lines during tests."""
    # When testing an alternative hypothesis, comment out the previous line:
    # total = var1 + var2
    test_result = var1 * var2
    return test_result


def demonstrate_triple_quotes() -> str:
    """Prove that triple quotes assigned to a variable become a live `str` object."""
    # Standalone string literal below is not bound to any name (ignored at runtime),
    # though `#` is the proper way to write inline code comments.
    """Standalone illustrative string literal."""

    # When assigned to a variable, triple quotes create an actual `str` in memory:
    notice = """Note: when assigned to a variable,
a triple-quoted string stays alive in memory as text!"""
    return notice


def main() -> None:
    print("=== Chapter 6: Comments ===\n")
    print("1) Isolating a line with # (# total = var1 + var2):")
    print("   Test result (var1 * var2):", compute_with_isolated_line(4, 5))

    print("\n2) Triple-quoted string assigned to a variable becomes `str`:")
    text = demonstrate_triple_quotes()
    print(f"   Type: {type(text).__name__}")
    print(text)


if __name__ == "__main__":
    main()
