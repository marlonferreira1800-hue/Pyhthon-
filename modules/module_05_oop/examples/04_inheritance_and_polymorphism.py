"""Module 5 (Ch. 21) — Inheritance and Polymorphism (Cars -> Gol, Corsa).

Includes explanation and fix for the book's classic `__int__` typo in Corsa
(corrected to `__init__`), `super().__init__()`, MRO inspection, and
polymorphism via overriding and extension.
"""


class Cars:
    """Superclass representing attributes and actions shared by cars."""

    def __init__(self, name: str, color: str, base_daily_rate: float = 100.0) -> None:
        self.name = name
        self.color = color
        self.base_daily_rate = base_daily_rate

    def describe(self) -> str:
        return f"{self.name} in {self.color}"

    def calculate_daily_rate(self, days: int) -> float:
        return round(self.base_daily_rate * days, 2)


class Gol(Cars):
    """Subclass inheriting from Cars and extending behavior via super()."""

    def __init__(self, name: str, color: str, engine: str = "1.0") -> None:
        super().__init__(name, color, base_daily_rate=110.0)
        self.engine = engine

    def describe(self) -> str:
        # Polymorphism via extension: reuses superclass output with super()
        return f"{super().describe()} | Engine {self.engine} (Hatchback)"


class Corsa(Cars):
    """Subclass with corrected __init__ (not __int__!).

    Book Errata Note:
        Some printings of the Portuguese book contain `def __int__(self, nome, cor):`
        inside Corsa. `__int__` is the magic method called by `int(obj)`, never the
        object initializer! Here we use the proper `def __init__` with `super().__init__`.
    """

    def __init__(self, name: str, color: str, doors: int = 4) -> None:
        super().__init__(name, color, base_daily_rate=120.0)
        self.doors = doors

    def describe(self) -> str:
        return f"{super().describe()} | {self.doors} doors (Compact/Sedan)"

    def calculate_daily_rate(self, days: int) -> float:
        # Polymorphism via override + super(): 5% discount for 5+ days
        total = super().calculate_daily_rate(days)
        if days >= 5:
            total *= 0.95
        return round(total, 2)


def demonstrate_inheritance_and_polymorphism() -> None:
    gol = Gol("Gol G6", "White", engine="1.6")
    corsa = Corsa("Corsa Classic", "Silver", doors=4)

    print("=== 1. Inheritance inspection (isinstance, issubclass, MRO) ===")
    print("isinstance(gol, Cars):", isinstance(gol, Cars))
    print("issubclass(Corsa, Cars):", issubclass(Corsa, Cars))
    print("Corsa MRO:", [cls.__name__ for cls in Corsa.__mro__])

    print("\n=== 2. Polymorphism in action (shared interface, distinct rules) ===")
    fleet: list[Cars] = [Cars("Standard Model", "Black"), gol, corsa]
    for car in fleet:
        print(f"- {car.describe()} -> 5 days: $ {car.calculate_daily_rate(5):.2f}")


if __name__ == "__main__":
    demonstrate_inheritance_and_polymorphism()
