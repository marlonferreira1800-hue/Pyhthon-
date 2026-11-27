"""AutoPy Package — Capstone Project for Python from Zero to OOP."""

from .cli import create_demo_service, main, run_demo
from .exceptions import (
    AutoPyError,
    ClientNotFoundError,
    DuplicateVehicleError,
    InvalidDataError,
    InvalidOperationError,
    VehicleNotFoundError,
    VehicleUnavailableError,
)
from .models import (
    Client,
    EconomyCar,
    ExecutiveCar,
    RentalRecord,
    UtilityVehicle,
    Vehicle,
)
from .services import (
    AutoPyRentalService,
    calculate_progressive_discount,
    count_available_recursively,
)

__version__ = "1.0.0"

__all__ = [
    "__version__",
    "AutoPyError",
    "ClientNotFoundError",
    "DuplicateVehicleError",
    "InvalidDataError",
    "InvalidOperationError",
    "VehicleNotFoundError",
    "VehicleUnavailableError",
    "Vehicle",
    "EconomyCar",
    "ExecutiveCar",
    "UtilityVehicle",
    "Client",
    "RentalRecord",
    "AutoPyRentalService",
    "calculate_progressive_discount",
    "count_available_recursively",
    "create_demo_service",
    "run_demo",
    "main",
]
