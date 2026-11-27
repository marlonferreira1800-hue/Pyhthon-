"""Module 4 — Chapter 19: Builtins and Pre-allocated Libraries.

Inspects dir(__builtins__) / dir(builtins), classifies built-in exceptions,
functions, and __...__ dunders, and contrasts 'import math' vs 'from math import pi'.
"""

import builtins
import math
from math import pi


def analyze_builtins() -> dict:
    """Categorize symbols in builtins into dunders, exceptions, and functions/types."""
    names = dir(builtins)
    dunders = [n for n in names if n.startswith("__") and n.endswith("__")]
    exceptions = [
        n
        for n in names
        if not n.startswith("__")
        and isinstance(getattr(builtins, n), type)
        and issubclass(getattr(builtins, n), BaseException)
    ]
    functions_and_types = [
        n for n in names if n not in dunders and n not in exceptions
    ]
    return {
        "total": len(names),
        "dunders": dunders,
        "exceptions": exceptions,
        "functions_and_types": functions_and_types,
    }


def calculate_circle_area(radius: float) -> float:
    """Compute circle area (pi * radius ** 2) using 'from math import pi'."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return pi * radius ** 2


def compare_math_imports(radius: float) -> dict:
    """Compare 'from math import pi' against qualified 'import math'."""
    area_from = pi * radius ** 2
    area_module = math.pi * math.pow(radius, 2)
    return {
        "area_from": area_from,
        "area_module": area_module,
        "equal": math.isclose(area_from, area_module),
    }


def main() -> None:
    """Run Chapter 19 demonstration."""
    info = analyze_builtins()
    print("=== CH. 19: dir(__builtins__) / builtins ===")
    print("Total built-in symbols:", info["total"])
    print("Sample dunders:", info["dunders"][:6])
    print(
        "Sample exceptions:",
        [e for e in ("NameError", "TypeError", "ValueError") if e in info["exceptions"]],
    )
    print(
        "Sample functions:",
        [f for f in ("print", "len", "dir", "help") if f in info["functions_and_types"]],
    )
    print("In __main__, __builtins__ type:", type(__builtins__).__name__)
    print("Circle area (radius=5):", round(calculate_circle_area(5), 4))
    print("Math import comparison:", compare_math_imports(5))


if __name__ == "__main__":
    main()
