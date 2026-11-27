"""Testable solutions for all 8 exercises in Module 4 (Chapters 18, 19, 20, and 22)."""

import builtins
import math
import sys
from math import pi
from pathlib import Path
from typing import Any

# Ensure direct execution from repository root resolves `modules.*` without PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules.module_04_modules_exceptions.examples import addition, greetings  # noqa: E402
from modules.module_04_modules_exceptions.examples.sales.price_calc import (  # noqa: E402
    increase_price as apply_increase,
)


def inspect_attributes(obj: Any) -> dict[str, Any]:
    """Exercise 1: use dir() to separate public methods and special dunders."""
    all_attrs = dir(obj)
    special = [name for name in all_attrs if name.startswith("__") and name.endswith("__")]
    public = [
        name for name in all_attrs if not (name.startswith("__") and name.endswith("__"))
    ]
    return {
        "type": type(obj).__name__,
        "total": len(all_attrs),
        "public": public,
        "special": special,
    }


def explore_builtins_and_area(radius: float) -> dict[str, Any]:
    """Exercise 2: inspect builtins and calculate circle area via pi * radius ** 2."""
    if radius < 0:
        raise ValueError("Radius must be non-negative.")

    symbols = set(dir(builtins))
    expected = {"ValueError", "TypeError", "NameError", "print", "__name__"}
    builtins_verified = expected <= symbols

    return {
        "area": pi * radius ** 2,
        "builtins_verified": builtins_verified,
        "total_builtins": len(symbols),
    }


def safe_divide(numerator: Any, denominator: Any) -> dict[str, Any]:
    """Exercise 3: division catching ValueError, TypeError, and ZeroDivisionError explicitly."""
    result: float | None = None
    error: str | None = None
    error_type: str | None = None

    try:
        a = float(numerator)
        b = float(denominator)
        value = a / b
    except ValueError as exc:
        error_type = "ValueError"
        error = f"Non-numeric value provided: {exc}"
    except TypeError as exc:
        error_type = "TypeError"
        error = f"Invalid type for numeric conversion: {exc}"
    except ZeroDivisionError as exc:
        error_type = "ZeroDivisionError"
        error = f"Division by zero is not allowed: {exc}"
    else:
        result = value

    return {
        "ok": error is None,
        "result": result,
        "error": error,
        "error_type": error_type,
    }


def diagnose_modules_and_paths() -> dict[str, Any]:
    """Exercise 4: inspect __name__, sys.path, and example modules."""
    return {
        "current_module": __name__,
        "greetings_module": greetings.__name__,
        "addition_module": addition.__name__,
        "sys_path_count": len(sys.path),
        "first_sys_path": sys.path[0] if sys.path else "",
        "greeting": greetings.greet("Student"),
        "sample_sum": addition.add(7, 8),
    }


def compute_price_table(
    prices: list[float], percentage: float
) -> list[dict[str, float]]:
    """Exercise 5: use sales.price_calc package via the apply_increase alias."""
    table = []
    for price in prices:
        table.append(
            {
                "original_price": float(price),
                "percentage": float(percentage),
                "updated_price": apply_increase(price, percentage),
            }
        )
    return table


def safe_sum_inputs(value1: Any, value2: Any) -> dict[str, Any]:
    """Exercise 6: correct try/except/else/finally pattern fixing book p. 213 bug."""
    total: int | None = None
    error: str | None = None
    error_type: str | None = None
    finalized = False

    try:
        num1 = int(value1)
        num2 = int(value2)
    except ValueError as exc:
        error_type = "ValueError"
        error = str(exc)
    except TypeError as exc:
        error_type = "TypeError"
        error = str(exc)
    else:
        total = num1 + num2
    finally:
        finalized = True

    return {
        "ok": error is None,
        "sum": total,
        "error": error,
        "error_type": error_type,
        "finalized": finalized,
    }


def convert_and_divide_pairs(pairs: list[tuple[Any, Any]]) -> dict[str, Any]:
    """Exercise 7: divide (a, b) pairs while logging successes, failures, and finally count."""
    successes: list[float] = []
    failures: list[dict[str, Any]] = []
    finalized_attempts = 0

    for index, pair in enumerate(pairs):
        try:
            raw_a, raw_b = pair
            quotient = int(raw_a) / int(raw_b)
        except (ValueError, TypeError, ZeroDivisionError) as exc:
            failures.append(
                {
                    "index": index,
                    "input": pair,
                    "error_type": type(exc).__name__,
                    "message": str(exc),
                }
            )
        else:
            successes.append(quotient)
        finally:
            finalized_attempts += 1

    return {
        "successes": successes,
        "failures": failures,
        "finalized_attempts": finalized_attempts,
    }


def process_sales_batch(
    items: list[dict[str, Any]], default_rate: float = 10.0
) -> dict[str, Any]:
    """Exercise 8: combine sales.price_calc, math.fsum, and per-item exception handling."""
    processed: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    updated_values: list[float] = []
    audit_completed = False

    try:
        for index, item in enumerate(items):
            try:
                product = str(item["product"])
                price_float = float(item["price"])
                rate_float = float(item.get("markup", default_rate))
                new_price = apply_increase(price_float, rate_float)
            except (KeyError, ValueError, TypeError) as exc:
                errors.append(
                    {
                        "index": index,
                        "item": item,
                        "error_type": type(exc).__name__,
                        "message": str(exc),
                    }
                )
            else:
                updated_values.append(new_price)
                processed.append(
                    {
                        "product": product,
                        "original_price": price_float,
                        "markup": rate_float,
                        "updated_price": new_price,
                    }
                )
    finally:
        audit_completed = True

    return {
        "processed": processed,
        "errors": errors,
        "total_updated": round(math.fsum(updated_values), 2),
        "audit_completed": audit_completed,
    }


def main() -> None:
    """Demonstrate all Module 4 exercise solutions."""
    print("Ex. 1:", inspect_attributes([1, 2])["type"])
    print("Ex. 2:", explore_builtins_and_area(3.0))
    print("Ex. 3:", safe_divide("10", "2"), safe_divide("10", 0))
    print("Ex. 4:", diagnose_modules_and_paths())
    print("Ex. 5:", compute_price_table([100.0, 250.0], 10.0))
    print("Ex. 6:", safe_sum_inputs("8", "12"), safe_sum_inputs("x", "12"))
    print("Ex. 7:", convert_and_divide_pairs([("10", "2"), ("10", "0"), ("abc", "2")]))
    print(
        "Ex. 8:",
        process_sales_batch(
            [
                {"product": "Notebook", "price": "50.0", "markup": 10},
                {"product": "Broken", "price": "abc"},
            ]
        ),
    )


if __name__ == "__main__":
    main()
