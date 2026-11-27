"""Automated test suite for Module 5 (OOP) and the AutoPy Final Project."""

from __future__ import annotations

import io
import runpy
import subprocess
import sys
from contextlib import redirect_stdout
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from final_project.autopy import (  # noqa: E402
    AutoPyError,
    AutoPyRentalService,
    Client,
    ClientNotFoundError,
    DuplicateVehicleError,
    EconomyCar,
    ExecutiveCar,
    InvalidDataError,
    InvalidOperationError,
    UtilityVehicle,
    Vehicle,
    VehicleNotFoundError,
    VehicleUnavailableError,
    calculate_progressive_discount,
    count_available_recursively,
)
from final_project.autopy.cli import (  # noqa: E402
    create_demo_service,
    main as cli_main,
    run_demo,
    run_interactive_menu,
)
from modules.module_05_oop.solutions.solved_exercises import (  # noqa: E402
    BankAccount,
    Cars,
    CategoryNode,
    Corsa,
    Developer,
    Employee,
    Gol,
    Salesperson,
    User,
    calculate_total_payroll,
    recursive_sequence,
    recursive_sum,
    update_and_clean_profile,
)


# ===========================================================================
# 1. Module 5 Examples — Runnable & Non-Blocking Verification
# ===========================================================================
EXAMPLE_FILES = sorted((ROOT_DIR / "modules" / "module_05_oop" / "examples").glob("*.py"))


def test_module_05_examples_exist() -> None:
    assert len(EXAMPLE_FILES) == 6


@pytest.mark.parametrize("script_path", EXAMPLE_FILES, ids=lambda p: p.name)
def test_module_05_examples_run_cleanly(script_path: Path) -> None:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        runpy.run_path(str(script_path), run_name="__main__")
    assert buffer.getvalue().strip() != ""


# ===========================================================================
# 2. Module 5 Solved Exercises
# ===========================================================================
def test_exercise_1_user_class_and_shadowing() -> None:
    u1 = User("Alice", "alice@example.com")
    u2 = User("Bob", "bob@example.com")

    assert "Alice" in u1.welcome()
    assert "Python Academy" in u1.welcome()

    # Attribute shadowing on u1 must not alter User.platform or u2.platform
    u1.platform = "Custom Academy"
    assert u1.platform == "Custom Academy"
    assert u2.platform == "Python Academy"
    assert User.platform == "Python Academy"


def test_exercise_2_dynamic_attributes() -> None:
    u = User("Carol", "carol@example.com")
    result = update_and_clean_profile(
        u,
        updates={"city": "Seattle", "name": "Carol Danvers"},
        remove=["email", "non_existent_field"],
    )
    assert result == {"name": "Carol Danvers", "city": "Seattle"}
    assert not hasattr(u, "email")
    assert getattr(u, "city") == "Seattle"


def test_exercise_3_recursion() -> None:
    assert recursive_sequence(5) == [1, 2, 3, 4, 5]
    assert recursive_sequence(3, 5) == []
    assert recursive_sum([2, 4, 6, 8]) == 20
    assert recursive_sum([]) == 0


def test_exercise_4_inheritance_and_init_fix() -> None:
    gol = Gol("Gol G6", "White", engine="1.6")
    corsa = Corsa("Corsa Classic", "Silver", doors=4)

    assert isinstance(gol, Cars)
    assert isinstance(corsa, Cars)
    assert issubclass(Corsa, Cars)
    # Verify Corsa defines __init__ directly (not the book's __int__ typo)
    assert "__init__" in Corsa.__dict__
    assert "__int__" not in Corsa.__dict__
    assert gol.describe() == "Gol G6 (White) - Engine 1.6"
    assert corsa.describe() == "Corsa Classic (Silver) - 4 doors"


def test_exercise_5_polymorphic_payroll() -> None:
    staff: list[Employee] = [
        Employee("Base", 2000.0),
        Developer("Dev", 5000.0, project_bonus=1200.0),
        Salesperson("Rep", 3000.0, total_sales=10000.0, commission_rate=0.10),
    ]
    assert calculate_total_payroll(staff) == 12200.0


def test_exercise_6_encapsulation_and_name_mangling() -> None:
    with pytest.raises(ValueError):
        BankAccount("Bad", -10.0)

    acc = BankAccount("Mariana", 100.0)
    assert acc.balance == 100.0
    assert "_BankAccount__balance" in acc.__dict__

    with pytest.raises(AttributeError):
        acc.balance = 999.0  # type: ignore[misc]

    assert acc.deposit(50.0) == 150.0
    assert acc.withdraw(40.0) == 110.0

    with pytest.raises(ValueError):
        acc.deposit(0.0)
    with pytest.raises(ValueError):
        acc.withdraw(500.0)


def test_exercise_7_recursive_category_tree() -> None:
    root = CategoryNode("Courses", ["Intro Python"])
    data = CategoryNode("Data", ["Pandas", "NumPy"])
    ml = CategoryNode("ML", ["Scikit-Learn", "Python Deep Learning"])
    data.add_child(ml)
    root.add_child(data)

    assert root.count_items_recursive() == 5
    assert root.search_item_recursive("python") == ["Courses", "ML"]


# ===========================================================================
# 3. AutoPy Final Project — Models, Encapsulation, Polymorphism
# ===========================================================================
def test_vehicle_encapsulation_and_polymorphism() -> None:
    econ = EconomyCar("abc1d23", "Gol G6", "White", 100.0, "9BWZZZ377VT004251", 1000.0)
    exec_car = ExecutiveCar(
        "efg4h56", "Corsa Sedan", "Silver", 150.0, "9BGXH68G09C102938", 500.0, daily_insurance_fee=35.0
    )
    util = UtilityVehicle(
        "ijk7l89", "Fiorino", "White", 160.0, "9BD265122P9221045", 200.0, cargo_capacity_kg=650.0
    )

    # Plate normalized to uppercase & masked chassis uses name-mangled __chassis
    assert econ.plate == "ABC1D23"
    assert econ.masked_chassis == "***4251"
    assert "_Vehicle__chassis" in econ.__dict__
    assert econ.summary_tuple() == ("ABC1D23", "Gol G6", "Economy", 100.0)

    # Mileage cannot decrease
    with pytest.raises(InvalidDataError):
        econ.mileage = 500.0

    # Polymorphic daily rate calculation
    assert econ.calculate_daily_rate(3) == 300.0
    assert econ.calculate_daily_rate(7) == 665.0  # 5% discount for 7+ days
    assert exec_car.calculate_daily_rate(4) == 740.0  # 150*4 + 35*4
    assert util.calculate_daily_rate(2) == 370.0  # 160*2 + 50 flat fee


def test_vehicle_and_client_validation_errors() -> None:
    with pytest.raises(InvalidDataError):
        EconomyCar("BAD", "Gol", "White", 100.0, "123456")
    with pytest.raises(InvalidDataError):
        EconomyCar("ABC1234", "Gol", "White", -50.0, "123456")
    with pytest.raises(InvalidDataError):
        Client(" ", "123456", "DL123")


def test_recursive_discount_and_availability() -> None:
    assert calculate_progressive_discount(1) == 0.0
    assert calculate_progressive_discount(2) == 0.02
    assert calculate_progressive_discount(6) == 0.10
    assert calculate_progressive_discount(15) == 0.20  # Capped at 20%

    with pytest.raises(InvalidDataError):
        calculate_progressive_discount(500)

    v1 = EconomyCar("AAA1111", "Gol", "White", 100.0, "CHASSIS1")
    v2 = EconomyCar("BBB2222", "Uno", "Black", 100.0, "CHASSIS2")
    v2.mark_rented()
    assert count_available_recursively([v1, v2]) == 1


# ===========================================================================
# 4. AutoPy Services — Sets, LIFO Undo, **kwargs, try/except/else/finally
# ===========================================================================
def test_service_sets_rentals_returns_and_lifo_undo() -> None:
    service = create_demo_service()

    assert service.registered_categories() == {"Economy", "Executive", "Utility"}
    assert service.available_categories() == {"Economy", "Executive", "Utility"}
    assert service.sold_out_categories() == set()
    assert service.total_available_vehicles() == 3

    # Duplicate plate check
    with pytest.raises(DuplicateVehicleError):
        service.register_vehicle(
            EconomyCar("ABC1D23", "Duplicate", "Red", 90.0, "9BW000000")
        )

    # Rent only Utility vehicle -> Utility becomes sold-out category
    rec = service.rent_vehicle("IJK7L89", "12345678900", 5)
    assert rec.gross_amount == 850.0  # 160*5 + 50
    assert rec.discount_rate == 0.08  # (5-1)*2%
    assert rec.total_amount == 782.0
    assert service.sold_out_categories() == {"Utility"}
    assert service.total_available_vehicles() == 2

    # Audited double-rent failure (try/except/else/finally)
    ok, rented_obj, msg = service.try_rent_with_audit("IJK7L89", "98765432100", 2)
    assert ok is False
    assert rented_obj is None
    assert "rejected" in msg.lower()
    assert any("BUSINESS_ERROR:VehicleUnavailableError" in log for log in service.audit_log)

    # LIFO undo reverts the rental
    undo_msg = service.undo_last_operation()
    assert "undone" in undo_msg.lower()
    assert service.total_available_vehicles() == 3
    assert service.sold_out_categories() == set()
    assert len(service.rentals) == 0


def test_service_return_dynamic_update_and_edge_errors() -> None:
    service = create_demo_service()

    # Dynamic update via **kwargs + setattr
    updated = service.update_vehicle("EFG4H56", color="Graphite")
    assert updated.color == "Graphite"

    with pytest.raises(InvalidDataError):
        service.update_vehicle("EFG4H56", chassis="HACKED")

    with pytest.raises(VehicleNotFoundError):
        service.find_vehicle("ZZZ9999")

    with pytest.raises(ClientNotFoundError):
        service.find_client("00000000")

    # Rent and return with mileage increase
    service.rent_vehicle("ABC1D23", "12345678900", 2)
    closed = service.return_vehicle("ABC1D23", miles_driven=150.5)
    assert closed.active is False
    assert service.find_vehicle("ABC1D23").mileage == 25550.5

    with pytest.raises(InvalidOperationError):
        service.return_vehicle("ABC1D23")  # Already returned

    # Cannot undo a vehicle registration while it is rented out
    service_fresh = AutoPyRentalService()
    service_fresh.register_vehicle(
        EconomyCar("NEW1A23", "Onix", "Blue", 120.0, "CHASSIS99")
    )
    service_fresh.register_client(Client("Test User", "555666777", "DL555"))
    service_fresh.rent_vehicle("NEW1A23", "555666777", 1)
    # Undo rental first, then undo registration
    service_fresh.undo_last_operation()
    msg = service_fresh.undo_last_operation()
    assert "NEW1A23" in msg
    assert len(service_fresh.fleet) == 0

    with pytest.raises(InvalidOperationError):
        service_fresh.undo_last_operation()


# ===========================================================================
# 5. CLI --demo, Interactive Menu (mocked), and Subprocess Smoke Test
# ===========================================================================
def test_cli_demo_and_report() -> None:
    lines: list[str] = []
    service = run_demo(output_fn=lines.append)
    joined = "\n".join(lines)

    assert "CONSOLIDATED FLEET REPORT" in joined
    assert "Gol G6" in joined
    assert "Corsa Sedan" in joined
    assert "Fiorino Endurance" in joined
    assert service.calculate_total_revenue() > 0
    assert cli_main(["--demo"]) == 0


def test_cli_interactive_menu_non_blocking() -> None:
    inputs = iter(["1", "2", "ABC1D23", "12345678900", "3", "4", "0"])
    outputs: list[str] = []

    run_interactive_menu(
        input_fn=lambda _: next(inputs),
        output_fn=outputs.append,
    )
    joined = "\n".join(outputs)
    assert "CONSOLIDATED FLEET REPORT" in joined
    assert "Success:" in joined
    assert "undone (LIFO)" in joined
    assert "Thank you for using AutoPy!" in joined


def test_main_py_demo_subprocess() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT_DIR / "final_project" / "main.py"), "--demo"],
        cwd=str(ROOT_DIR),
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "CONSOLIDATED FLEET REPORT" in result.stdout
    assert "AutoPy Final Project automated demo" in result.stdout
