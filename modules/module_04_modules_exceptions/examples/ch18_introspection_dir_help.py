"""Module 4 — Chapter 18: Introspection with dir() and help().

Demonstrates inspecting attributes and docstrings of Python objects at runtime.
"""

import contextlib
import io


def inspect_object(obj) -> dict:
    """Separate dunder attributes and public methods using dir(obj)."""
    all_attrs = dir(obj)
    dunders = [name for name in all_attrs if name.startswith("__") and name.endswith("__")]
    public = [
        name for name in all_attrs if not (name.startswith("__") and name.endswith("__"))
    ]
    return {
        "type": type(obj).__name__,
        "total": len(all_attrs),
        "dunders": dunders,
        "public": public,
    }


def capture_help_safely(obj) -> str:
    """Capture help(obj) output into a string without invoking an interactive pager."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        help(obj)
    return buffer.getvalue()


def main() -> None:
    """Run Chapter 18 demonstration."""
    list2 = [1, 2, 3]
    summary = inspect_object(list2)
    print("=== CH. 18: dir(list2) ===")
    print("Type:", summary["type"])
    print("Total attributes:", summary["total"])
    print("Public methods:", summary["public"])

    print("\n=== CH. 18: help(list2.append) ===")
    print(capture_help_safely(list2.append).strip())


if __name__ == "__main__":
    main()
