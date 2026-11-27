"""Module 4 — Chapter 22: Tracebacks and Exception Handling.

Demonstrates reading NameError, ValueError, and TypeError, specific vs.
generic except blocks, and the corrected try / except / else / finally pattern
fixing the p. 213 bug from the book.
"""

import sys


def demonstrate_common_exceptions() -> dict[str, str]:
    """Trigger and catch educational examples of NameError, ValueError, and TypeError."""
    errors = {}

    try:
        # Intentionally reference an undefined variable to trigger NameError
        _ = undefined_variable  # type: ignore[name-defined]  # noqa: F821
    except NameError as exc:
        errors["NameError"] = str(exc)

    try:
        int("not_a_number")
    except ValueError as exc:
        errors["ValueError"] = str(exc)

    try:
        _ = "10" + 5  # type: ignore[operator]
    except TypeError as exc:
        errors["TypeError"] = str(exc)

    return errors


def safe_add_pattern(raw_first, raw_second) -> dict:
    """Correct try / except / else / finally pattern (fixes book p. 213 bug).

    - try: only risky integer conversions.
    - except: explicit ValueError and TypeError handlers.
    - else: runs ONLY when num1 and num2 exist.
    - finally: always runs and NEVER references num1 or num2.
    """
    result = None
    error = None
    error_type = None
    finally_ran = False

    try:
        num1 = int(raw_first)
        num2 = int(raw_second)
    except ValueError as exc:
        error_type = "ValueError"
        error = f"Invalid integer value: {exc}"
    except TypeError as exc:
        error_type = "TypeError"
        error = f"Incompatible type for conversion: {exc}"
    else:
        result = num1 + num2
    finally:
        # Always safe: does not reference num1/num2, preventing NameError
        finally_ran = True

    return {
        "ok": error is None,
        "result": result,
        "error": error,
        "error_type": error_type,
        "finally_ran": finally_ran,
    }


def interactive_addition() -> dict:
    """Interactive input() workflow wrapped in a function so imports never block."""
    first = input("Enter the first integer: ")
    second = input("Enter the second integer: ")
    output = safe_add_pattern(first, second)
    if output["ok"]:
        print(f"Sum: {output['result']}")
    else:
        print(f"Error ({output['error_type']}): {output['error']}")
    return output


def main() -> None:
    """Run non-blocking demo by default; pass --interactive for input() prompt."""
    if "--interactive" in sys.argv:
        interactive_addition()
        return

    print("=== CH. 22: COMMON EXCEPTIONS ===")
    for name, detail in demonstrate_common_exceptions().items():
        print(f"  {name}: {detail}")

    print("\n=== CH. 22: CORRECT try/except/else/finally PATTERN ===")
    print("  Valid ('10', '20'):", safe_add_pattern("10", "20"))
    print("  ValueError ('abc', '20'):", safe_add_pattern("abc", "20"))
    print("  TypeError (None, '20'):", safe_add_pattern(None, "20"))


if __name__ == "__main__":
    main()
