"""Module sales/price_calc.py (Ch. 20): commercial price calculations."""


def increase_price(price: float, percentage: float) -> float:
    """Increase price by the given percentage."""
    if price < 0 or percentage < 0:
        raise ValueError("Price and percentage must be non-negative.")
    return round(price + (price * (percentage / 100)), 2)


def discount_price(price: float, percentage: float) -> float:
    """Apply a percentage discount to price."""
    if price < 0 or percentage < 0 or percentage > 100:
        raise ValueError("Invalid values for discount calculation.")
    return round(price - (price * (percentage / 100)), 2)


def main() -> None:
    """Run direct execution demo."""
    print("Direct test price_calc.py -> increase_price(100, 15):", increase_price(100, 15))


if __name__ == "__main__":
    main()
