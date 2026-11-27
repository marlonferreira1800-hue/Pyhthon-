"""Domain models for AutoPy applying full OOP (Ch. 21).

Defines the Vehicle inheritance hierarchy (Vehicle -> EconomyCar, ExecutiveCar,
UtilityVehicle), Client (connecting Ch. 21 User), and RentalRecord (connecting
Ch. 20 sales), with encapsulation, @property, name mangling, super(), and
polymorphism.
"""

from __future__ import annotations

from .exceptions import InvalidDataError


class Vehicle:
    """Base class (blueprint) for every vehicle in the AutoPy fleet."""

    # Class attributes
    CATEGORY: str = "General"
    total_vehicles_created: int = 0

    def __init__(
        self,
        plate: str,
        model: str,
        color: str,
        base_daily_rate: float,
        chassis: str,
        mileage: float = 0.0,
    ) -> None:
        cleaned_plate = plate.strip().upper()
        if len(cleaned_plate) < 7:
            raise InvalidDataError(
                f"Invalid plate '{plate}': provide at least 7 characters."
            )
        if not model.strip():
            raise InvalidDataError("Vehicle model cannot be empty.")
        if not chassis.strip() or len(chassis.strip()) < 6:
            raise InvalidDataError("Chassis number must have at least 6 characters.")

        self._plate = cleaned_plate
        self.model = model.strip()
        self.color = color.strip() or "Unspecified"
        self._base_daily_rate = 0.0
        self._mileage = 0.0
        self._available = True
        # Private attribute with name mangling (_Vehicle__chassis)
        self.__chassis = chassis.strip().upper()

        # Run @property setter validation right at construction
        self.base_daily_rate = base_daily_rate
        self.mileage = mileage

        Vehicle.total_vehicles_created += 1

    @property
    def plate(self) -> str:
        return self._plate

    @property
    def base_daily_rate(self) -> float:
        return self._base_daily_rate

    @base_daily_rate.setter
    def base_daily_rate(self, value: float) -> None:
        if value <= 0:
            raise InvalidDataError("Base daily rate must be greater than zero.")
        self._base_daily_rate = round(float(value), 2)

    @property
    def mileage(self) -> float:
        return self._mileage

    @mileage.setter
    def mileage(self, new_mileage: float) -> None:
        if new_mileage < 0:
            raise InvalidDataError("Mileage cannot be negative.")
        if new_mileage < self._mileage:
            raise InvalidDataError(
                "Mileage cannot be rolled back below the current reading."
            )
        self._mileage = round(float(new_mileage), 1)

    @property
    def available(self) -> bool:
        return self._available

    @property
    def masked_chassis(self) -> str:
        """Exposes only the last 4 characters of private __chassis."""
        return f"***{self.__chassis[-4:]}"

    def mark_rented(self) -> None:
        self._available = False

    def mark_available(self, miles_driven: float = 0.0) -> None:
        if miles_driven < 0:
            raise InvalidDataError("Miles driven cannot be negative.")
        self.mileage = self._mileage + miles_driven
        self._available = True

    def calculate_daily_rate(self, days: int) -> float:
        """Computes gross rental cost before progressive discounts."""
        if days <= 0:
            raise InvalidDataError("Number of rental days must be positive.")
        return round(self._base_daily_rate * days, 2)

    def describe(self) -> str:
        status = "Available" if self._available else "Rented"
        return (
            f"[{self.CATEGORY}] {self.model} ({self.color}) | "
            f"Plate: {self._plate} | Daily rate: $ {self._base_daily_rate:.2f} | "
            f"Mileage: {self._mileage:.1f} | {status}"
        )

    def summary_tuple(self) -> tuple[str, str, str, float]:
        """Returns an immutable tuple snapshot of core vehicle specs (Ch. 13)."""
        return (self._plate, self.model, self.CATEGORY, self._base_daily_rate)

    def __str__(self) -> str:
        return self.describe()


class EconomyCar(Vehicle):
    """Subclass for compact/economy cars (e.g., Gol, Onix, Uno)."""

    CATEGORY = "Economy"

    def __init__(
        self,
        plate: str,
        model: str,
        color: str,
        base_daily_rate: float,
        chassis: str,
        mileage: float = 0.0,
        engine: str = "1.0",
    ) -> None:
        super().__init__(plate, model, color, base_daily_rate, chassis, mileage)
        self.engine = engine

    def calculate_daily_rate(self, days: int) -> float:
        """Polymorphism: applies a 5% economy bonus on rentals of 7+ days."""
        gross = super().calculate_daily_rate(days)
        if days >= 7:
            return round(gross * 0.95, 2)
        return gross

    def describe(self) -> str:
        return f"{super().describe()} | Engine: {self.engine}"


class ExecutiveCar(Vehicle):
    """Subclass for executive/sedan vehicles (e.g., Corsa Sedan, Corolla, Civic)."""

    CATEGORY = "Executive"

    def __init__(
        self,
        plate: str,
        model: str,
        color: str,
        base_daily_rate: float,
        chassis: str,
        mileage: float = 0.0,
        daily_insurance_fee: float = 35.0,
        automatic_transmission: bool = True,
    ) -> None:
        super().__init__(plate, model, color, base_daily_rate, chassis, mileage)
        if daily_insurance_fee < 0:
            raise InvalidDataError("Daily insurance fee cannot be negative.")
        self.daily_insurance_fee = round(float(daily_insurance_fee), 2)
        self.automatic_transmission = bool(automatic_transmission)

    def calculate_daily_rate(self, days: int) -> float:
        """Polymorphism via super(): adds executive daily insurance coverage."""
        base = super().calculate_daily_rate(days)
        return round(base + (self.daily_insurance_fee * days), 2)

    def describe(self) -> str:
        transmission = "Automatic" if self.automatic_transmission else "Manual"
        return (
            f"{super().describe()} | Transmission: {transmission} | "
            f"Insurance/day: $ {self.daily_insurance_fee:.2f}"
        )


class UtilityVehicle(Vehicle):
    """Subclass for cargo/utility vehicles (e.g., Fiorino, Strada)."""

    CATEGORY = "Utility"

    def __init__(
        self,
        plate: str,
        model: str,
        color: str,
        base_daily_rate: float,
        chassis: str,
        mileage: float = 0.0,
        cargo_capacity_kg: float = 650.0,
    ) -> None:
        super().__init__(plate, model, color, base_daily_rate, chassis, mileage)
        if cargo_capacity_kg <= 0:
            raise InvalidDataError("Cargo capacity must be positive.")
        self.cargo_capacity_kg = round(float(cargo_capacity_kg), 1)

    def calculate_daily_rate(self, days: int) -> float:
        """Polymorphism: adds a flat $ 50.00 cargo-prep fee per rental."""
        base = super().calculate_daily_rate(days)
        return round(base + 50.0, 2)

    def describe(self) -> str:
        return f"{super().describe()} | Cargo: {self.cargo_capacity_kg:.0f} kg"


class Client:
    """Represents a rental customer (connecting the User class from Ch. 21)."""

    def __init__(self, name: str, document: str, driver_license: str) -> None:
        if not name.strip():
            raise InvalidDataError("Client name cannot be empty.")
        cleaned_doc = "".join(ch for ch in document if ch.isalnum())
        if len(cleaned_doc) < 5:
            raise InvalidDataError("Invalid client document ID.")
        if not driver_license.strip():
            raise InvalidDataError("Driver license is required.")

        self.name = name.strip()
        self.__document = cleaned_doc
        self.driver_license = driver_license.strip().upper()
        self.rentals_completed = 0

    @property
    def document(self) -> str:
        return self.__document

    @property
    def masked_document(self) -> str:
        return f"***{self.__document[-4:]}"

    def welcome(self) -> str:
        return (
            f"Hello, {self.name}! AutoPy profile active "
            f"(Doc: {self.masked_document} | License: {self.driver_license})."
        )

    def __str__(self) -> str:
        return f"{self.name} ({self.masked_document})"


class RentalRecord:
    """Rental contract binding a Client, Vehicle, and financial breakdown."""

    def __init__(
        self,
        code: int,
        client: Client,
        vehicle: Vehicle,
        days: int,
        gross_amount: float,
        discount_rate: float,
        total_amount: float,
    ) -> None:
        self.code = code
        self.client = client
        self.vehicle = vehicle
        self.days = days
        self.gross_amount = round(float(gross_amount), 2)
        self.discount_rate = round(float(discount_rate), 4)
        self.total_amount = round(float(total_amount), 2)
        self.active = True

    def summary(self) -> str:
        status = "ACTIVE" if self.active else "CLOSED"
        discount_pct = self.discount_rate * 100
        return (
            f"#{self.code:03d} [{status}] {self.vehicle.plate} "
            f"({self.vehicle.model}) -> {self.client.name} | "
            f"{self.days}d | Gross: $ {self.gross_amount:.2f} | "
            f"Disc: {discount_pct:.0f}% | Total: $ {self.total_amount:.2f}"
        )
