"""Module 5 (Ch. 21) — Encapsulation, Name Mangling, @property, and Dunders.

Covers the book's medicine capsule analogy, `_protected`, `__private`
(`_ClassName__attr`), `@property` validation, and the technical distinction
between `__dunder__` protocol methods and `__private` name mangling.
"""


class ProtectedVehicle:
    """Demonstrates encapsulation with protected, private, and @property attributes."""

    def __init__(self, model: str, chassis: str, mileage: float = 0.0) -> None:
        self.model = model           # Public
        self._mileage = 0.0          # Protected (by convention)
        self.__chassis = chassis     # Private (name mangling -> _ProtectedVehicle__chassis)
        self.mileage = mileage       # Triggers setter validation on creation

    @property
    def masked_chassis(self) -> str:
        """Exposes only the last 4 characters of the private chassis number."""
        return f"***{self.__chassis[-4:]}"

    @property
    def mileage(self) -> float:
        return self._mileage

    @mileage.setter
    def mileage(self, new_mileage: float) -> None:
        if new_mileage < 0:
            raise ValueError("Mileage cannot be negative.")
        if new_mileage < self._mileage:
            raise ValueError("Mileage cannot be rolled back (tamper protection).")
        self._mileage = float(new_mileage)

    def __str__(self) -> str:
        # __str__ is a dunder (__name__) reserved by Python's data model (no mangling!)
        return f"{self.model} | Mileage: {self._mileage:.1f} | Chassis: {self.masked_chassis}"


def demonstrate_encapsulation() -> None:
    car = ProtectedVehicle("Gol 1.0", "9BWZZZ377VT004251", mileage=12500.0)
    print("Initial state:", car)

    # Valid update through @property setter
    car.mileage = 12800.5
    print("After valid update:", car)

    # Invalid mutation blocked by the "capsule" (@setter)
    try:
        car.mileage = 1000.0
    except ValueError as err:
        print(f"Validation blocked tampering: {err}")

    # Reverse engineering name mangling:
    # `car.__chassis` raises AttributeError because Python mangled it to `_ProtectedVehicle__chassis`.
    try:
        _ = car.__chassis  # type: ignore[attr-defined]
    except AttributeError as err:
        print(f"Direct access to __chassis failed ({err})")

    print("Actual keys in __dict__:", list(car.__dict__.keys()))
    print("Mangled attribute value:", car._ProtectedVehicle__chassis)  # type: ignore[attr-defined]
    print("Safe public access via property:", car.masked_chassis)


if __name__ == "__main__":
    demonstrate_encapsulation()
