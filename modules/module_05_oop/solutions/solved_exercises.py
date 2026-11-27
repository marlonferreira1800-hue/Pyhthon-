"""Annotated, testable solutions for Module 5 OOP exercises."""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Exercise 1 — User class, class attribute, and self
# ---------------------------------------------------------------------------
class User:
    """Represents a user enrolled in the course platform."""

    platform = "Python Academy"

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def welcome(self) -> str:
        return (
            f"Welcome, {self.name}! "
            f"Your access on {self.platform} is active ({self.email})."
        )


# ---------------------------------------------------------------------------
# Exercise 2 — Dynamic attribute mutation via built-ins
# ---------------------------------------------------------------------------
def update_and_clean_profile(
    obj: object,
    updates: dict[str, object],
    remove: list[str] | None = None,
) -> dict[str, object]:
    """Updates attributes with setattr, deletes existing ones with delattr, reads via getattr."""
    for key, value in updates.items():
        setattr(obj, key, value)

    if remove:
        for field in remove:
            if hasattr(obj, field):
                delattr(obj, field)

    return {
        key: getattr(obj, key)
        for key in list(vars(obj).keys())
    }


# ---------------------------------------------------------------------------
# Exercise 3 — Recursion and stopping conditions
# ---------------------------------------------------------------------------
def recursive_sequence(maximum: int, current: int = 1) -> list[int]:
    """Recursively builds the integer sequence [current, ..., maximum]."""
    if current > maximum:
        return []
    return [current] + recursive_sequence(maximum, current + 1)


def recursive_sum(numbers: list[int | float]) -> int | float:
    """Recursively sums numeric elements without calling sum()."""
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])


# ---------------------------------------------------------------------------
# Exercise 4 — Inheritance (Cars -> Gol, Corsa with __init__ fixed)
# ---------------------------------------------------------------------------
class Cars:
    """Superclass representing common vehicle attributes and behavior."""

    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def describe(self) -> str:
        return f"{self.name} ({self.color})"


class Gol(Cars):
    """Subclass extending Cars via super()."""

    def __init__(self, name: str, color: str, engine: str = "1.0") -> None:
        super().__init__(name, color)
        self.engine = engine

    def describe(self) -> str:
        return f"{super().describe()} - Engine {self.engine}"


class Corsa(Cars):
    """Subclass defining __init__ properly (fixing the book's __int__ typo)."""

    def __init__(self, name: str, color: str, doors: int = 4) -> None:
        super().__init__(name, color)
        self.doors = doors

    def describe(self) -> str:
        return f"{super().describe()} - {self.doors} doors"


# ---------------------------------------------------------------------------
# Exercise 5 — Polymorphism in payroll calculation
# ---------------------------------------------------------------------------
class Employee:
    """Base class for polymorphic payroll computation."""

    def __init__(self, name: str, base_salary: float) -> None:
        self.name = name
        self.base_salary = float(base_salary)

    def calculate_pay(self) -> float:
        return round(self.base_salary, 2)


class Developer(Employee):
    """Receives base salary plus project bonus."""

    def __init__(
        self, name: str, base_salary: float, project_bonus: float = 0.0
    ) -> None:
        super().__init__(name, base_salary)
        self.project_bonus = float(project_bonus)

    def calculate_pay(self) -> float:
        return round(super().calculate_pay() + self.project_bonus, 2)


class Salesperson(Employee):
    """Receives base salary plus sales commission."""

    def __init__(
        self,
        name: str,
        base_salary: float,
        total_sales: float = 0.0,
        commission_rate: float = 0.05,
    ) -> None:
        super().__init__(name, base_salary)
        self.total_sales = float(total_sales)
        self.commission_rate = float(commission_rate)

    def calculate_pay(self) -> float:
        return round(
            super().calculate_pay() + (self.total_sales * self.commission_rate), 2
        )


def calculate_total_payroll(staff: list[Employee]) -> float:
    """Aggregates staff payroll polymorphically."""
    return round(sum(member.calculate_pay() for member in staff), 2)


# ---------------------------------------------------------------------------
# Exercise 6 — Encapsulation, @property, and name mangling
# ---------------------------------------------------------------------------
class BankAccount:
    """Account encapsulating balance inside a private __balance attribute."""

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.__balance = float(initial_balance)

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance = round(self.__balance + float(amount), 2)
        return self.__balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds for requested withdrawal.")
        self.__balance = round(self.__balance - float(amount), 2)
        return self.__balance


# ---------------------------------------------------------------------------
# Exercise 7 — Hierarchical category tree with recursive methods
# ---------------------------------------------------------------------------
class CategoryNode:
    """Tree node supporting recursive item counting and search."""

    def __init__(self, name: str, items: list[str] | None = None) -> None:
        self.name = name
        self.items: list[str] = list(items) if items is not None else []
        self.children: list[CategoryNode] = []

    def add_child(self, child: CategoryNode) -> None:
        self.children.append(child)

    def count_items_recursive(self) -> int:
        total = len(self.items)
        for child in self.children:
            total += child.count_items_recursive()
        return total

    def search_item_recursive(self, term: str) -> list[str]:
        normalized = term.strip().lower()
        matches: list[str] = []
        if normalized and any(normalized in item.lower() for item in self.items):
            matches.append(self.name)
        for child in self.children:
            matches.extend(child.search_item_recursive(term))
        return matches


if __name__ == "__main__":
    u = User("Ana", "ana@example.com")
    print(u.welcome())
    print("Updated profile:", update_and_clean_profile(u, {"city": "Austin"}, ["email"]))
    print("Recursive sequence:", recursive_sequence(5))
    print("Recursive sum:", recursive_sum([10, 20, 30]))
    print(Gol("Gol G7", "White", "1.6").describe())
    print(Corsa("Corsa Hatch", "Blue", 2).describe())
    staff = [Developer("Lucas", 6000, 1500), Salesperson("Clara", 3000, 20000, 0.05)]
    print("Total payroll:", calculate_total_payroll(staff))
    account = BankAccount("Mariana", 500.0)
    account.deposit(250.0)
    account.withdraw(100.0)
    print("Final balance:", account.balance)
