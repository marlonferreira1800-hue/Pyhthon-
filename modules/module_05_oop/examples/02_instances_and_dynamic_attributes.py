"""Module 5 (Ch. 21) — Modifying Instance Data and Dynamic Attribute Built-ins.

Covers direct assignment, setattr(), getattr(), hasattr(), and delattr()
with line-by-line reverse engineering.
"""


class SystemUser:
    """Represents a user whose attributes can be modified dynamically."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def summary(self) -> str:
        return f"SystemUser(name={self.name!r}, age={self.age!r})"


def demonstrate_dynamic_attributes() -> None:
    """Demonstrates direct mutation and setattr/getattr/hasattr/delattr."""
    user1 = SystemUser("Carlos", 28)
    print("Initial state:", user1.summary())

    # 1. Direct assignment: replaces the existing key in instance.__dict__.
    user1.name = "Carlos Eduardo"
    print("After direct assignment:", user1.summary())

    # 2. setattr(obj, attr_str, value): ideal when field names come from variables.
    dynamic_field = "city"
    setattr(user1, dynamic_field, "Curitiba")
    setattr(user1, "age", 29)
    print("After setattr -> __dict__:", user1.__dict__)

    # 3. hasattr() + getattr(): safe attribute lookup without AttributeError risk.
    for key in ("name", "city", "phone"):
        if hasattr(user1, key):
            value = getattr(user1, key)
            print(f"hasattr=True -> {key}: {value!r}")
        else:
            fallback = getattr(user1, key, "Not provided")
            print(f"hasattr=False -> {key} using fallback: {fallback!r}")

    # 4. delattr(obj, attr_str): removes the attribute from the instance.
    delattr(user1, "city")
    print("After delattr(user1, 'city') -> __dict__:", user1.__dict__)

    # Reverse engineering: accessing a deleted attribute raises AttributeError.
    try:
        _ = user1.city  # type: ignore[attr-defined]
    except AttributeError as err:
        print(f"Expected AttributeError caught after delattr: {err}")


if __name__ == "__main__":
    demonstrate_dynamic_attributes()
