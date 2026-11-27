"""Core fleet & rental services for AutoPy (integrating Modules 1–5).

Combines dictionaries for fleet & clients, sets for category analytics,
a LIFO stack (.append()/.pop()) for undo operations, recursive calculations,
*args/**kwargs, setattr/hasattr, and full try/except/else/finally blocks.
"""

from __future__ import annotations

from typing import Any

from .exceptions import (
    AutoPyError,
    ClientNotFoundError,
    DuplicateVehicleError,
    InvalidDataError,
    InvalidOperationError,
    VehicleNotFoundError,
    VehicleUnavailableError,
)
from .models import Client, RentalRecord, Vehicle


def calculate_progressive_discount(
    days: int,
    cap: float = 0.20,
    daily_step: float = 0.02,
) -> float:
    """Computes a progressive discount using pure recursion (Ch. 21).

    Rules:
    - 1 day (or less): 0% (stopping condition / base case).
    - Each additional day adds `daily_step` (2%) up to `cap` (20%).
    - Durations outside 1..365 raise InvalidDataError to protect stack depth.
    """
    if days < 0 or days > 365:
        raise InvalidDataError("Rental duration must be between 1 and 365 days.")
    if days <= 1:
        return 0.0
    previous_discount = calculate_progressive_discount(
        days - 1, cap=cap, daily_step=daily_step
    )
    return round(min(cap, previous_discount + daily_step), 4)


def count_available_recursively(vehicles: list[Vehicle], index: int = 0) -> int:
    """Counts available vehicles by recursively traversing a list (Ch. 21)."""
    if index >= len(vehicles):  # Base case
        return 0
    current = 1 if vehicles[index].available else 0
    return current + count_available_recursively(vehicles, index + 1)


class AutoPyRentalService:
    """Central service managing fleet inventory, clients, rentals, and reports."""

    def __init__(self, name: str = "AutoPy Fleet & Rentals") -> None:
        self.name = name
        self._fleet: dict[str, Vehicle] = {}
        self._clients: dict[str, Client] = {}
        self._rentals: list[RentalRecord] = []
        # LIFO stack for undoing the latest registration or rental (Ch. 13)
        self._operation_stack: list[dict[str, Any]] = []
        self._audit_log: list[str] = []
        self._next_rental_code = 1

    # ------------------------------------------------------------------
    # Data structure queries (dict, list, set, recursion)
    # ------------------------------------------------------------------
    @property
    def fleet(self) -> dict[str, Vehicle]:
        return dict(self._fleet)

    @property
    def clients(self) -> dict[str, Client]:
        return dict(self._clients)

    @property
    def rentals(self) -> list[RentalRecord]:
        return list(self._rentals)

    @property
    def undo_stack_size(self) -> int:
        return len(self._operation_stack)

    @property
    def audit_log(self) -> list[str]:
        return list(self._audit_log)

    def registered_categories(self) -> set[str]:
        """Returns the set of all vehicle categories registered in the fleet."""
        return {vehicle.CATEGORY for vehicle in self._fleet.values()}

    def available_categories(self) -> set[str]:
        """Returns the set of categories with at least one available unit."""
        return {
            vehicle.CATEGORY
            for vehicle in self._fleet.values()
            if vehicle.available
        }

    def sold_out_categories(self) -> set[str]:
        """Uses set difference (Ch. 15) to identify categories with no free units."""
        return self.registered_categories() - self.available_categories()

    def total_available_vehicles(self) -> int:
        """Uses recursive counting across the fleet list."""
        return count_available_recursively(list(self._fleet.values()))

    # ------------------------------------------------------------------
    # Registrations and dynamic mutation (setattr / **kwargs)
    # ------------------------------------------------------------------
    def register_vehicle(self, vehicle: Vehicle) -> Vehicle:
        if vehicle.plate in self._fleet:
            raise DuplicateVehicleError(
                f"A vehicle with plate {vehicle.plate} is already registered."
            )
        self._fleet[vehicle.plate] = vehicle
        self._operation_stack.append(
            {"type": "REGISTER_VEHICLE", "plate": vehicle.plate}
        )
        self._audit_log.append(f"REGISTER_VEHICLE:{vehicle.plate}")
        return vehicle

    def find_vehicle(self, plate: str) -> Vehicle:
        key = plate.strip().upper()
        vehicle = self._fleet.get(key)
        if vehicle is None:
            raise VehicleNotFoundError(
                f"Vehicle with plate '{key}' was not found in the fleet."
            )
        return vehicle

    def update_vehicle(self, plate: str, **fields: Any) -> Vehicle:
        """Updates allowed attributes using **kwargs (Ch. 17) and setattr (Ch. 21)."""
        vehicle = self.find_vehicle(plate)
        allowed_fields = {"model", "color", "base_daily_rate", "mileage"}
        for key, value in fields.items():
            if key not in allowed_fields or not hasattr(vehicle, key):
                raise InvalidDataError(
                    f"Attribute '{key}' cannot be updated dynamically."
                )
            setattr(vehicle, key, value)
        self._audit_log.append(f"UPDATE_VEHICLE:{vehicle.plate}")
        return vehicle

    def register_client(self, client: Client) -> Client:
        if client.document in self._clients:
            raise InvalidDataError(
                f"Client with document {client.masked_document} is already registered."
            )
        self._clients[client.document] = client
        self._audit_log.append(f"REGISTER_CLIENT:{client.masked_document}")
        return client

    def find_client(self, document: str) -> Client:
        cleaned = "".join(ch for ch in document if ch.isalnum())
        client = self._clients.get(cleaned)
        if client is None:
            raise ClientNotFoundError(
                f"Client with document '{document}' is not registered."
            )
        return client

    # ------------------------------------------------------------------
    # Rentals, returns, LIFO undo, and try/except/else/finally auditing
    # ------------------------------------------------------------------
    def rent_vehicle(self, plate: str, client_document: str, days: int) -> RentalRecord:
        """Creates a rental record using polymorphic rates and recursive discounts."""
        if days <= 0 or days > 365:
            raise InvalidDataError("Rental days must be between 1 and 365.")

        vehicle = self.find_vehicle(plate)
        if not vehicle.available:
            raise VehicleUnavailableError(
                f"Vehicle {vehicle.model} ({vehicle.plate}) is currently rented out."
            )
        client = self.find_client(client_document)

        # Polymorphism: each subclass computes its own specialized daily total
        gross_amount = vehicle.calculate_daily_rate(days)
        discount = calculate_progressive_discount(days)
        total_amount = round(gross_amount * (1.0 - discount), 2)

        vehicle.mark_rented()
        client.rentals_completed += 1

        record = RentalRecord(
            code=self._next_rental_code,
            client=client,
            vehicle=vehicle,
            days=days,
            gross_amount=gross_amount,
            discount_rate=discount,
            total_amount=total_amount,
        )
        self._next_rental_code += 1
        self._rentals.append(record)
        self._operation_stack.append(
            {
                "type": "RENTAL",
                "code": record.code,
                "plate": vehicle.plate,
                "document": client.document,
            }
        )
        self._audit_log.append(f"RENTAL:#{record.code}:{vehicle.plate}")
        return record

    def try_rent_with_audit(
        self, plate: str, client_document: str, days: int
    ) -> tuple[bool, RentalRecord | None, str]:
        """Demonstrates full try / except / else / finally flow from Module 4 (Ch. 22)."""
        final_status = ""
        try:
            record = self.rent_vehicle(plate, client_document, days)
        except AutoPyError as err:
            final_status = f"BUSINESS_ERROR:{type(err).__name__}"
            return (False, None, f"Operation rejected: {err}")
        else:
            final_status = f"SUCCESS:#{record.code}"
            return (True, record, f"Rental #{record.code} confirmed!")
        finally:
            self._audit_log.append(f"AUDIT:{plate.strip().upper()}:{final_status}")

    def return_vehicle(self, plate: str, miles_driven: float = 0.0) -> RentalRecord:
        """Closes an active rental and updates vehicle mileage."""
        vehicle = self.find_vehicle(plate)
        if vehicle.available:
            raise InvalidOperationError(
                f"Vehicle {vehicle.plate} does not have an active rental."
            )
        active_record: RentalRecord | None = None
        for rec in reversed(self._rentals):
            if rec.vehicle.plate == vehicle.plate and rec.active:
                active_record = rec
                break
        if active_record is None:
            raise InvalidOperationError(
                f"No active contract found for {vehicle.plate}."
            )

        vehicle.mark_available(miles_driven=miles_driven)
        active_record.active = False
        self._audit_log.append(f"RETURN:#{active_record.code}:{vehicle.plate}")
        return active_record

    def undo_last_operation(self) -> str:
        """Pops the top action from the LIFO stack (.pop()) and reverts state."""
        if not self._operation_stack:
            raise InvalidOperationError("No operations left on the stack to undo.")

        latest = self._operation_stack.pop()
        op_type = latest["type"]

        if op_type == "REGISTER_VEHICLE":
            plate = latest["plate"]
            vehicle = self._fleet.get(plate)
            if vehicle is not None and not vehicle.available:
                self._operation_stack.append(latest)
                raise InvalidOperationError(
                    f"Cannot undo registration of {plate} while it is rented out."
                )
            self._fleet.pop(plate, None)
            self._audit_log.append(f"UNDONE:REGISTER_VEHICLE:{plate}")
            return f"Vehicle registration for {plate} undone (LIFO)."

        if op_type == "RENTAL":
            code = latest["code"]
            plate = latest["plate"]
            document = latest["document"]
            for idx in range(len(self._rentals) - 1, -1, -1):
                if self._rentals[idx].code == code:
                    rec = self._rentals.pop(idx)
                    if rec.active:
                        rec.vehicle.mark_available(miles_driven=0.0)
                    client = self._clients.get(document)
                    if client is not None and client.rentals_completed > 0:
                        client.rentals_completed -= 1
                    break
            self._audit_log.append(f"UNDONE:RENTAL:#{code}:{plate}")
            return f"Rental #{code} for vehicle {plate} undone (LIFO)."

        raise InvalidOperationError(f"Unknown operation type: {op_type}")

    def calculate_total_revenue(self) -> float:
        return round(sum(rec.total_amount for rec in self._rentals), 2)

    # ------------------------------------------------------------------
    # Formatted report (Module 2 string methods + Module 3 f-strings)
    # ------------------------------------------------------------------
    def generate_report(self, *highlights: str) -> str:
        """Builds a consolidated f-string fleet report supporting *args highlights."""
        width = 72
        lines = [
            "=" * width,
            f" {self.name.upper()} — CONSOLIDATED FLEET REPORT ".center(width, "="),
            "=" * width,
            f"Total vehicles in fleet    : {len(self._fleet)}",
            f"Available (recursive)      : {self.total_available_vehicles()}",
            f"Registered categories      : {sorted(self.registered_categories())}",
            f"Available categories       : {sorted(self.available_categories())}",
            f"Sold-out categories        : {sorted(self.sold_out_categories())}",
            f"Registered clients         : {len(self._clients)}",
            f"Recorded rentals           : {len(self._rentals)}",
            f"Total revenue              : $ {self.calculate_total_revenue():.2f}",
            f"Undo stack size (LIFO)     : {self.undo_stack_size}",
            "-" * width,
            "CURRENT FLEET:",
        ]

        if not self._fleet:
            lines.append("  (No vehicles registered)")
        else:
            for vehicle in self._fleet.values():
                lines.append(f"  - {vehicle.describe()}")

        lines.append("-" * width)
        lines.append("RENTAL CONTRACTS:")
        if not self._rentals:
            lines.append("  (No active or closed rentals)")
        else:
            for rec in self._rentals:
                lines.append(f"  - {rec.summary()}")

        if highlights:
            lines.append("-" * width)
            lines.append("HIGHLIGHTS (*args):")
            for item in highlights:
                lines.append(f"  * {item}")

        lines.append("=" * width)
        return "\n".join(lines)
