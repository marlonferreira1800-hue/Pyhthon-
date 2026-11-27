"""Chapter 3 — Programming Logic, Syntax, Keywords, and Indentation.

Covers:
- 3 algorithm types (input->output, no-input->output, input->no visible output)
- Logic error ('5' + '2' -> '52') vs arithmetic addition (5 + 2 -> 7)
- Reserved keywords (35 in Python 3 vs 31 classic keywords noted in the book)
- Lexical analysis (top-to-bottom, left-to-right, `*` precedence over `+`)
- Mandatory indentation and positive/negative classification using `int(var1) >= 0`

Run:
    python modules/module_01_fundamentals/examples/ch03_logic_syntax_indentation.py
"""

import keyword
import sys


# Type 1: Algorithm with input -> produces output
def algorithm_input_to_output(num1: int, num2: int) -> int:
    """Take two integers and return their sum."""
    return num1 + num2


# Type 2: Algorithm with no input -> produces output
def algorithm_no_input_to_output() -> str:
    """Return a fixed greeting without external input."""
    return "Hello! No-input algorithm producing output."


# Type 3: Algorithm with input -> no direct visible output (internal state update)
def algorithm_input_no_visible_output(log: list[str], entry: str) -> None:
    """Record an entry into internal state without returning or printing."""
    log.append(entry)


def demonstrate_syntax_vs_logic() -> tuple[str, int, str]:
    """Compare a logic error ('5' + '2') with true addition and explain SyntaxError."""
    logic_error = "5" + "2"  # String concatenation -> '52'
    math_sum = 5 + 2         # Integer addition -> 7
    syntax_note = "Print(5) + 2 =  -> SyntaxError (invalid trailing '=' and uppercase 'Print')"
    return logic_error, math_sum, syntax_note


def lexical_analysis_compliment(with_spaces: bool = True) -> str:
    """Demonstrate evaluation order (`*` evaluated before `+`, left to right)."""
    # Reverse Engineering:
    # 1. `3 * 'very'` evaluates first because `*` has higher precedence than `+`.
    # 2. Concatenations `+` then combine strings from left to right.
    if with_spaces:
        return "You are " + 3 * "very " + "cool!"
    return "You are" + 3 * "very" + "cool!"


def classify_positive_or_negative(var1: str | int) -> str:
    """Properly cast `int(var1)` before testing `>= 0`."""
    # Converting str -> int prevents `TypeError: '>=' not supported between 'str' and 'int'`.
    if int(var1) >= 0:
        return "positive"
    return "negative"


def list_reserved_keywords() -> list[str]:
    """Return the official Python 3 reserved keyword list."""
    return list(keyword.kwlist)


def run_interactive_mode() -> None:
    """Safe interactive prompt guarded against EOF or empty input."""
    try:
        raw = input("Enter an integer to classify (default 10): ").strip()
    except (EOFError, OSError):
        raw = ""
    value = raw if raw else "10"
    try:
        result = classify_positive_or_negative(value)
    except ValueError:
        print(f"Input '{value}' is not an integer; falling back to 10.")
        result = classify_positive_or_negative(10)
    print(f"Classification: {result}")


def main() -> None:
    print("=== Chapter 3: Logic, Syntax, Keywords, and Indentation ===\n")

    print("1) The 3 Algorithm Types:")
    print("  - Type 1 (input -> output):", algorithm_input_to_output(5, 2))
    print("  - Type 2 (no input -> output):", algorithm_no_input_to_output())
    internal_log: list[str] = []
    algorithm_input_no_visible_output(internal_log, "event_saved")
    print("  - Type 3 (input -> no visible output), internal state:", internal_log)

    logic_error, math_sum, syntax_note = demonstrate_syntax_vs_logic()
    print("\n2) Syntax vs. Logic:")
    print(f"  - '5' + '2' -> {logic_error!r} ({type(logic_error).__name__}, logic error)")
    print(f"  -  5  +  2  -> {math_sum!r} ({type(math_sum).__name__}, true math sum)")
    print(f"  - Invalid syntax: {syntax_note}")

    kws = list_reserved_keywords()
    print(f"\n3) Reserved Keywords in Python 3.10 ({len(kws)} keywords):")
    print("  " + ", ".join(kws))
    print("  Update note: the book lists 31 classic keywords (Python 2 era, including print/exec).")
    print("  In Python 3, print and exec are built-in functions and kwlist has 35 entries.")

    print("\n4) Lexical Analysis:")
    print("  - Without spaces:", lexical_analysis_compliment(False))
    print("  - With spaces:   ", lexical_analysis_compliment(True))

    print("\n5) Mandatory Indentation (positive/negative check):")
    for sample in ("15", "-3", "0"):
        print(f"  - int({sample!r}) >= 0 -> {classify_positive_or_negative(sample)}")

    if "--interactive" in sys.argv:
        run_interactive_mode()


if __name__ == "__main__":
    main()
