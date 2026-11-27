"""Module 3 — Chapter 16: String Interpolation.

Illustrates the evolution of Python formatting across %, .format(), and
f-strings (including inline expressions such as {3 * age}).
"""


def generate_interpolation_examples(name: str = "Fernando", age: int = 25) -> dict:
    """Return equivalent formatted strings using %, .format(), and f-strings."""
    # 1st generation: printf-style % operator
    using_percent = "Name: %s | Age: %d | Triple: %d" % (name, age, 3 * age)

    # 2nd generation: .format() with empty {} and explicit positional indices {0}, {1}
    using_format_auto = "Name: {} | Age: {} | Triple: {}".format(name, age, 3 * age)
    using_format_indexed = "{0}'s age: {1} (3x for {0}: {2})".format(
        name, age, 3 * age
    )

    # 3rd generation (Python 3.6+): f-strings with inline math expressions
    using_fstring = f"Name: {name} | Age: {age} | Triple: {3 * age}"

    return {
        "percent": using_percent,
        "format_auto": using_format_auto,
        "format_indexed": using_format_indexed,
        "fstring": using_fstring,
    }


def main() -> None:
    """Run Chapter 16 demonstration."""
    print("=== CH. 16: STRING INTERPOLATION ===")
    for style, output in generate_interpolation_examples().items():
        print(f"  [{style}] {output}")


if __name__ == "__main__":
    main()
