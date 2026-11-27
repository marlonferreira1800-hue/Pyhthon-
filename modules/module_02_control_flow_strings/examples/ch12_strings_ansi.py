"""Chapter 12 — Strings, Immutability, ANSI Colors, Alignment, and Numeric Formatting.

Covers:
- Single vs double quotes (`"Bob's watermark"`, `'It was a "veeeery" cold day'`) and multiline
- `.lower()` and `.upper()` (immutability vs permanent reassignment)
- Searching with `in` and splitting with `.split()`
- ANSI escape colors (`\\033[91m`, `\\033[0m`, foreground/background codes)
- `.center()`, `.ljust()`, `.rjust()`
- Numeric precision formatting with `math.pi` (`%.2f`, `%.5f`, and modern `f'{num:.2f}'`)

Run:
    python modules/module_02_control_flow_strings/examples/ch12_strings_ansi.py
"""

from math import pi

ANSI_COLORS: dict[str, str] = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
    "bg_blue_white": "\033[44;97m",
}


def demonstrate_quotes_and_immutability(sample: str = "Python OOP") -> dict[str, object]:
    """Show quote combinations and prove `.upper()` returns a new string."""
    single_inside_double = "Bob's watermark"
    double_inside_single = 'It was a "veeeery" cold day'
    multiline = """Line A
Line B"""

    # Calling .upper() without reassigning does NOT mutate `sample`:
    upper_preview = sample.upper()
    still_original = sample == "Python OOP"

    # Permanent update requires explicit reassignment:
    reassigned = sample.upper()

    return {
        "single_inside_double": single_inside_double,
        "double_inside_single": double_inside_single,
        "multiline": multiline,
        "upper_preview": upper_preview,
        "original_unchanged": still_original,
        "reassigned_lower": reassigned.lower(),
    }


def search_and_split(sentence: str, keyword: str, sep: str | None = None) -> dict[str, object]:
    """Perform case-insensitive membership search and `.split()` tokenization."""
    found = keyword.lower() in sentence.lower()
    tokens = sentence.split(sep)
    return {"found": found, "tokens": tokens}


def colorize_ansi(text: str, color_name: str) -> str:
    """Wrap text in ANSI color escape codes followed by reset `\\033[0m`."""
    code = ANSI_COLORS.get(color_name, "")
    if not code:
        return text
    return f"{code}{text}{ANSI_COLORS['reset']}"


def format_alignment_table(title: str, item: str, price: str) -> list[str]:
    """Align strings cleanly with `.center()`, `.ljust()`, and `.rjust()`."""
    return [
        title.center(32, "="),
        f"{item.ljust(20, '.')}{price.rjust(12)}",
    ]


def format_pi_variants() -> dict[str, str]:
    """Compare legacy `%` formatting against modern f-strings using `math.pi`."""
    return {
        "legacy_2": "%.2f" % pi,
        "legacy_5": "%.5f" % pi,
        "modern_2": f"{pi:.2f}",
        "modern_5": f"{pi:.5f}",
    }


def main() -> None:
    print("=== Chapter 12: Strings, ANSI Colors, and Formatting ===\n")

    info = demonstrate_quotes_and_immutability()
    print("1) Quotes & Immutability:")
    print("  -", info["single_inside_double"])
    print("  -", info["double_inside_single"])
    print("  - Original unchanged after .upper() without reassignment?", info["original_unchanged"])

    print("\n2) Search (`in`) and `.split()`:")
    print("  -", search_and_split("Python,Strings,ANSI,Formatting", "ansi", sep=","))

    print("\n3) ANSI Terminal Colors:")
    print("  -", colorize_ansi("ALERT: Check syntax carefully", "red"))
    print("  -", colorize_ansi("SUCCESS: All checks green", "green"))
    print("  -", colorize_ansi("HEADER: Python Course", "bg_blue_white"))

    print("\n4) Text Alignment (.center / .ljust / .rjust):")
    for row in format_alignment_table(" RECEIPT ", "Python Book", "$39.90"):
        print("  ", row)

    print("\n5) Numeric Formatting (`math.pi`):")
    for name, rendered in format_pi_variants().items():
        print(f"   {name:10s} -> {rendered}")


if __name__ == "__main__":
    main()
