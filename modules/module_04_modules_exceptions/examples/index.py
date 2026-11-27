"""Entry point (Ch. 20): index.py.

Demonstrates importing local modules (greetings, addition), subfolder packages
(sales/price_calc.py), import aliases (import ... as ...), and sys.path.
"""

import sys

# Support both direct execution (`python index.py`) and package import
if __package__:
    from . import addition as add_module
    from . import greetings
    from .sales import price_calc as pc
    from .sales.price_calc import increase_price as apply_markup
else:
    import addition as add_module
    import greetings
    import sales.price_calc as pc
    from sales.price_calc import increase_price as apply_markup


def run_modularization_demo() -> dict:
    """Run an end-to-end demo combining local modules and the sales package."""
    greeting_msg = greetings.greet("Maria")
    sum_result = add_module.add(15, 27)
    marked_up_price = apply_markup(200.0, 12.5)
    discounted_price = pc.discount_price(200.0, 10.0)

    return {
        "greeting_msg": greeting_msg,
        "sum_result": sum_result,
        "marked_up_price": marked_up_price,
        "discounted_price": discounted_price,
        "addition_module_name": add_module.__name__,
        "first_sys_path": sys.path[0],
        "sys_path_count": len(sys.path),
    }


def main() -> None:
    """Run Chapter 20 demonstration."""
    print("=== CH. 20: MODULES, PACKAGES, ALIASES & sys.path ===")
    for key, value in run_modularization_demo().items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
