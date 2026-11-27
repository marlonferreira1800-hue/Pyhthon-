"""Chapter 1 — Introduction to Python, History, and the 19 Zen of Python Principles.

Run:
    python modules/module_01_fundamentals/examples/ch01_introduction_zen.py
"""

# ---------------------------------------------------------------------------
# LINE-BY-LINE REVERSE ENGINEERING
# ---------------------------------------------------------------------------
# 1. We store the 19 aphorisms of Tim Peters' Zen of Python in an immutable
#    tuple so both the CLI walkthrough and automated tests can inspect them.
# ---------------------------------------------------------------------------

ZEN_OF_PYTHON: tuple[str, ...] = (
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
)

PYTHON_HISTORY: dict[int, str] = {
    1989: "Guido van Rossum conceives Python at CWI (Netherlands).",
    1991: "First public release (Python 0.9.0).",
    1994: "Python 1.0 officially released.",
    2009: "Open-source OSI/MIT-compatible PSF licensing milestone solidifies adoption.",
}

COMPANIES_USING_PYTHON: list[str] = [
    "Google",
    "YouTube",
    "Instagram",
    "Dropbox",
    "Spotify",
    "Reddit",
    "Blender 3D",
    "Industrial Light & Magic",
]


def compare_hello_world() -> dict[str, str]:
    """Compare 'Hello World' verbosity across C, Java, and Python."""
    return {
        "C": '#include <stdio.h>\nint main() { printf("Hello World!\\n"); return 0; }',
        "Java": (
            'public class HelloWorld { public static void main(String[] args) '
            '{ System.out.println("Hello World!"); } }'
        ),
        "Python": "print('Hello World!')",
    }


def get_zen_of_python() -> tuple[str, ...]:
    """Return all 19 principles of The Zen of Python by Tim Peters."""
    return ZEN_OF_PYTHON


def main() -> None:
    print("=== Chapter 1: Why Python? ===\n")

    print("1) 'Hello World' Comparison (less boilerplate, direct expression):")
    for language, code in compare_hello_world().items():
        print(f"--- {language} ---\n{code}\n")

    print("2) Historical Milestones:")
    for year, event in PYTHON_HISTORY.items():
        print(f"  - {year}: {event}")

    print("\n3) Companies and Studios Using Python:")
    print("  " + ", ".join(COMPANIES_USING_PYTHON))

    zen = get_zen_of_python()
    print(f"\n4) All {len(zen)} Principles of The Zen of Python (Tim Peters):")
    for index, principle in enumerate(zen, start=1):
        print(f"  {index:02d}. {principle}")


if __name__ == "__main__":
    main()
