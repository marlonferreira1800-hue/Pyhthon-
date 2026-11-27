"""CLI interface for AutoPy supporting --demo and interactive mode."""

from __future__ import annotations

import argparse
from typing import Callable

from .exceptions import AutoPyError
from .models import Client, EconomyCar, ExecutiveCar, UtilityVehicle
from .services import AutoPyRentalService, calculate_progressive_discount


def create_demo_service() -> AutoPyRentalService:
    """Seeds an AutoPyRentalService with classic course vehicles and clients."""
    service = AutoPyRentalService("AutoPy Fleet — OOP Edition")

    # Connecting classic book cars (Gol, Corsa) + Utility vehicle
    service.register_vehicle(
        EconomyCar("ABC1D23", "Gol G6", "White", 110.0, "9BWZZZ377VT004251", 25400.0, engine="1.6")
    )
    service.register_vehicle(
        ExecutiveCar(
            "EFG4H56",
            "Corsa Sedan",
            "Silver",
            150.0,
            "9BGXH68G09C102938",
            18200.0,
            daily_insurance_fee=35.0,
        )
    )
    service.register_vehicle(
        UtilityVehicle(
            "IJK7L89",
            "Fiorino Endurance",
            "White",
            160.0,
            "9BD265122P9221045",
            10500.0,
            cargo_capacity_kg=650.0,
        )
    )

    service.register_client(Client("Mariana Costa", "12345678900", "DL998877"))
    service.register_client(Client("Rafael Lima", "98765432100", "DL112233"))
    return service


def run_demo(output_fn: Callable[[str], None] = print) -> AutoPyRentalService:
    """Runs a complete non-blocking demonstration integrating all 5 modules."""
    service = create_demo_service()

    output_fn(">>> Starting AutoPy Final Project automated demo (--demo)...")

    # 1. Polymorphism + recursive progressive discount
    ok1, rec1, msg1 = service.try_rent_with_audit("ABC1D23", "12345678900", 7)
    output_fn(f"[1] Economy Gol rental (7 days): ok={ok1} | {msg1}")
    if rec1:
        output_fn(f"    Summary: {rec1.summary()}")

    # 2. Invalid double-rent attempt caught via try/except/else/finally
    ok_err, _, msg_err = service.try_rent_with_audit("ABC1D23", "98765432100", 3)
    output_fn(f"[2] Expected duplicate-rental guard: ok={ok_err} | {msg_err}")

    # 3. Executive rental + LIFO stack (.append/.pop) undo
    ok2, _, msg2 = service.try_rent_with_audit("EFG4H56", "98765432100", 4)
    output_fn(f"[3] Executive Corsa rental (4 days): ok={ok2} | {msg2}")
    undo_msg = service.undo_last_operation()
    output_fn(f"[4] LIFO stack undo: {undo_msg}")

    # 4. Utility rental + Gol return with mileage increment
    service.rent_vehicle("IJK7L89", "98765432100", 5)
    returned = service.return_vehicle("ABC1D23", miles_driven=320.5)
    output_fn(f"[5] Vehicle return processed: {returned.summary()}")

    # 5. Dynamic attribute update via **kwargs + setattr
    service.update_vehicle("EFG4H56", color="Midnight Black")
    discount_10d = calculate_progressive_discount(10) * 100

    report = service.generate_report(
        f"Recursive progressive discount for 10 days: {discount_10d:.0f}%",
        "Encapsulation active: chassis protected via name mangling and @property",
        "LIFO undo stack verified without blocking",
    )
    output_fn(report)
    return service


def run_interactive_menu(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> None:
    """Runs the interactive terminal menu for AutoPy."""
    service = create_demo_service()
    output_fn("=== Welcome to AutoPy Interactive CLI ===")

    while True:
        output_fn(
            "\nChoose an option:\n"
            "1 - Show fleet & report\n"
            "2 - Rent a vehicle\n"
            "3 - Return a vehicle\n"
            "4 - Undo last operation (LIFO)\n"
            "0 - Exit"
        )
        try:
            choice = input_fn("Option: ").strip()
        except (EOFError, KeyboardInterrupt):
            output_fn("\nClosing AutoPy...")
            break

        if choice == "0":
            output_fn("Thank you for using AutoPy!")
            break
        elif choice == "1":
            output_fn(service.generate_report())
        elif choice == "2":
            try:
                plate = input_fn("Vehicle plate: ")
                doc = input_fn("Client document: ")
                days = int(input_fn("Rental days: "))
                rec = service.rent_vehicle(plate, doc, days)
                output_fn(f"Success: {rec.summary()}")
            except (AutoPyError, ValueError) as err:
                output_fn(f"Rental error: {err}")
        elif choice == "3":
            try:
                plate = input_fn("Vehicle plate: ")
                miles = float(input_fn("Miles driven: "))
                rec = service.return_vehicle(plate, miles_driven=miles)
                output_fn(f"Returned: {rec.summary()}")
            except (AutoPyError, ValueError) as err:
                output_fn(f"Return error: {err}")
        elif choice == "4":
            try:
                output_fn(service.undo_last_operation())
            except AutoPyError as err:
                output_fn(f"Notice: {err}")
        else:
            output_fn("Invalid option. Please try again.")


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="autopy",
        description="AutoPy — Fleet & Rental System (Final OOP Capstone Project).",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run a complete automated simulation without waiting for input().",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)
    if args.demo:
        run_demo()
        return 0
    run_interactive_menu()
    return 0
