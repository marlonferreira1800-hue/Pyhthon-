"""Custom domain exceptions for the AutoPy Fleet & Rental system (Modules 4 & 5)."""


class AutoPyError(Exception):
    """Base exception for all AutoPy domain errors."""


class InvalidDataError(AutoPyError, ValueError):
    """Raised when input data or attributes violate domain validation rules."""


class VehicleNotFoundError(AutoPyError, LookupError):
    """Raised when a requested license plate does not exist in the fleet."""


class DuplicateVehicleError(AutoPyError):
    """Raised when attempting to register a license plate already in the fleet."""


class VehicleUnavailableError(AutoPyError):
    """Raised when attempting to rent a vehicle that is currently rented out."""


class ClientNotFoundError(AutoPyError, LookupError):
    """Raised when a client document ID is not registered."""


class InvalidOperationError(AutoPyError):
    """Raised when an operation cannot be performed in the current state."""
