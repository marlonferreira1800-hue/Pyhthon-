"""Example module (Ch. 20): greetings.py.

Demonstrates a simple reusable module protected by if __name__ == "__main__".
"""


def greet(name: str = "student") -> str:
    """Return a personalized welcome greeting."""
    return f"Hello, {name}! Welcome to modular Python."


def main() -> None:
    """Run direct execution demo."""
    print(f"[Running directly] __name__ = {__name__!r}")
    print(greet("Fernando"))


if __name__ == "__main__":
    main()
