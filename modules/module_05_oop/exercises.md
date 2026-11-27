# Exercises — Module 5: Object-Oriented Programming (Chs. 21 & 23)

Work through these progressive exercises and compare your code with [solutions/solved_exercises.py](solutions/solved_exercises.py).  
Every class and function specifies a clear contract so you can verify your solution automatically using `pytest`.

---

## Beginner Level

### Exercise 1 — The `User` Blueprint, Class Attributes, and `self`
Create a `User` class featuring:
- A class attribute `platform = "Python Academy"`.
- An initializer `__init__(self, name: str, email: str)` storing `name` and `email` as instance attributes.
- A method `welcome(self) -> str` returning exactly:
  `f"Welcome, {self.name}! Your access on {self.platform} is active ({self.email})."`

> **Reverse Engineering Prompt:** Instantiate two users and override `platform` on only one of them (`u1.platform = "Custom"`) to observe attribute shadowing vs. `User.platform`.

---

### Exercise 2 — Dynamic Instance Mutation (`setattr`, `getattr`, `hasattr`, `delattr`)
Implement `update_and_clean_profile(obj: object, updates: dict[str, object], remove: list[str] | None = None) -> dict[str, object]` so that it:
1. Applies every `(key, value)` pair from `updates` onto `obj` via `setattr(obj, key, value)`.
2. When `remove` is provided, checks `hasattr(obj, field)` before deleting each attribute with `delattr(obj, field)` (safely ignoring non-existent fields).
3. Returns a dictionary mapping each key in `vars(obj)` to its value read via `getattr(obj, key)`.

---

## Intermediate Level

### Exercise 3 — Recursion and Base Case
Inspired by the recursive counter in Chapter 21:
1. Implement `recursive_sequence(maximum: int, current: int = 1) -> list[int]` returning the list of integers from `current` up to `maximum` using pure recursion (no `for`/`while` loops). Base case: when `current > maximum`, return `[]`.
2. Implement `recursive_sum(numbers: list[int | float]) -> int | float` summing a list recursively without `sum()`. Base case: an empty list returns `0`.

---

### Exercise 4 — Inheritance and the Book Errata Fix (`Cars` → `Gol`, `Corsa`)
Build the classic inheritance hierarchy while fixing the book's `__int__` typo:
- Superclass `Cars` with `__init__(self, name: str, color: str)` and `describe(self) -> str` returning `f"{self.name} ({self.color})"`.
- Subclass `Gol(Cars)` with `__init__(self, name: str, color: str, engine: str = "1.0")` calling `super().__init__(name, color)` and extending `describe()` to `f"{super().describe()} - Engine {self.engine}"`.
- Subclass `Corsa(Cars)` with `__init__(self, name: str, color: str, doors: int = 4)` using **`__init__`** properly (watch out for the book's `__int__` typo!) and `super().__init__(name, color)`, extending `describe()` to `f"{super().describe()} - {self.doors} doors"`.

---

### Exercise 5 — Polymorphic Payroll Calculation
Model a payroll system without `if/elif` type checks:
- Base class `Employee(name: str, base_salary: float)` with `calculate_pay(self) -> float` returning `float(self.base_salary)`.
- Subclass `Developer(Employee)` accepting `project_bonus: float = 0.0` and overriding `calculate_pay()` via `super().calculate_pay() + self.project_bonus`.
- Subclass `Salesperson(Employee)` accepting `total_sales: float = 0.0` and `commission_rate: float = 0.05` and overriding `calculate_pay()` via `super().calculate_pay() + (self.total_sales * self.commission_rate)`.
- Function `calculate_total_payroll(staff: list[Employee]) -> float` returning the rounded sum (`2` decimal places) by calling `member.calculate_pay()` polymorphically.

---

## Challenge Level

### Exercise 6 — Encapsulation, `@property`, and *Name Mangling*
Implement `BankAccount(owner: str, initial_balance: float = 0.0)`:
- Store the balance in a private attribute `self.__balance` (triggering *name mangling*).
- Expose a read-only `@property def balance(self) -> float`.
- Reject negative `initial_balance` values with `ValueError`.
- Implement `deposit(self, amount: float) -> float` (reject `amount <= 0` with `ValueError` and return the updated balance).
- Implement `withdraw(self, amount: float) -> float` (reject `amount <= 0` or `amount > self.__balance` with `ValueError` and return the updated balance).

---

### Exercise 7 — OOP + Recursion in a Category Tree
Implement `CategoryNode(name: str, items: list[str] | None = None)`:
- Stores `self.name`, `self.items` (copy of `items` or empty list), and `self.children: list[CategoryNode] = []`.
- Method `add_child(self, child: CategoryNode) -> None`.
- Method `count_items_recursive(self) -> int`: returns the item count in this node plus recursively all items in descendant nodes.
- Method `search_item_recursive(self, term: str) -> list[str]`: traverses the tree recursively and returns the names of all categories containing an item matching `term` (case-insensitive substring match).
