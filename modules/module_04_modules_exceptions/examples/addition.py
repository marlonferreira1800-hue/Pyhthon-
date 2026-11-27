"""Example module (Ch. 20): addition.py.

Demonstrates arithmetic helper functions and __name__ behavior when run
directly vs. imported by another module.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference a - b."""
    return a - b


def main() -> None:
    """Run direct execution demo."""
    print(f"[addition.py] Running as main program (__name__ = {__name__!r})")
    print("Example add(10, 25) =", add(10, 25))


if __name__ == "__main__":
    main()
