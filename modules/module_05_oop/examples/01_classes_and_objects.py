"""Module 5 (Ch. 21) — Classes, Objects, Class vs. Instance Attributes, and self.

Methodology: Line-by-line Reverse Engineering of how Python classes work in memory.
"""


class Car:
    """Blueprint representing a car (conceptual class / 'super variable')."""

    # Class attribute: shared across all instances of Car.
    wheels = 4

    def __init__(self, model: str, color: str) -> None:
        # Instance attributes: stored exclusively in each object's __dict__.
        self.model = model
        self.color = color

    def action1(self) -> str:
        """Simulates the object's first action using self attributes."""
        return f"The {self.color} {self.model} started its engine on {self.wheels} wheels."


class User:
    """Classic book example: User class with __init__ and welcome()."""

    platform = "Python from Zero to OOP"

    def __init__(self, name: str, role: str = "Student") -> None:
        self.name = name
        self.role = role

    def welcome(self) -> str:
        """Returns a personalized greeting for the current instance."""
        return f"Hello, {self.name}! Role '{self.role}' is active on {self.platform}."


def demonstrate_classes_and_objects() -> None:
    """Walks line by line through native types, instances, shadowing, and self."""
    print("=== 1. Python is natively object-oriented ===")
    # Reverse engineering: integer and string literals are already class instances!
    print("type(42) ->", type(42))
    print("type('Python') ->", type("Python"))

    print("\n=== 2. Instantiating Car and comparing class vs. instance attributes ===")
    car_a = Car("Beetle", "Blue")
    car_b = Car("Uno", "White")

    print("car_a.action1() ->", car_a.action1())
    print("car_b.action1() ->", car_b.action1())
    print("car_a.__dict__ ->", car_a.__dict__)
    print("car_b.__dict__ ->", car_b.__dict__)

    # Reverse engineering shadowing: assigning on an instance creates a local key
    # inside car_a.__dict__ without altering Car.wheels for car_b.
    car_a.wheels = 3
    print(
        f"After car_a.wheels = 3 -> car_a.wheels={car_a.wheels}, "
        f"car_b.wheels={car_b.wheels}, Car.wheels={Car.wheels}"
    )
    print("car_a.__dict__ after shadowing ->", car_a.__dict__)

    print("\n=== 3. User class and explicit self call equivalence ===")
    user1 = User("Mariana", "Developer")
    msg_instance = user1.welcome()
    msg_explicit = User.welcome(user1)
    print("Via instance:", msg_instance)
    print("Via Class(self):", msg_explicit)
    assert msg_instance == msg_explicit


if __name__ == "__main__":
    demonstrate_classes_and_objects()
