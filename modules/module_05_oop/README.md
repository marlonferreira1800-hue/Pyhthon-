# Module 5 — Object-Oriented Programming and Final Remarks

> **Book Reference:** *Python from Zero to Object-Oriented Programming* (*Python do ZERO à Programação Orientada a Objetos*, Updated & Expanded Edition), by Fernando Feltrin — **Chapters 21 and 23**.  
> **Methodology:** Self-taught learning through **line-by-line Reverse Engineering** — we don't just run code; we take each line apart to trace what the Python interpreter does in memory, on the call stack, and inside the object model.

---

## Module Roadmap

| Book Chapter | Topics Covered | Practical Example |
|---|---|---|
| **Ch. 21 — OOP (Part 1)** | Classes as blueprints / "super variables", Python natively OO, `PascalCase`, class vs. instance attributes, `__init__` and `self`, `User` & `welcome()` | [01_classes_and_objects.py](examples/01_classes_and_objects.py) |
| **Ch. 21 — OOP (Part 2)** | Direct attribute mutation, `setattr()`, `getattr()`, `hasattr()`, and `delattr()` | [02_instances_and_dynamic_attributes.py](examples/02_instances_and_dynamic_attributes.py) |
| **Ch. 21 — OOP (Part 3)** | Recursion, base case (stopping condition), book's recursive counter, call stack trace, and OOP hierarchy traversal | [03_recursion.py](examples/03_recursion.py) |
| **Ch. 21 — OOP (Part 4)** | Inheritance (`Cars` → `Gol`, `Corsa`), `super().__init__()`, Errata fix (`__int__` vs `__init__`), Polymorphism (overriding and extending) | [04_inheritance_and_polymorphism.py](examples/04_inheritance_and_polymorphism.py) |
| **Ch. 21 — OOP (Part 5)** | Encapsulation (medicine capsule analogy), `_protected`, `__private` (*name mangling*), `@property`, and dunder `__name__` clarification | [05_encapsulation_and_properties.py](examples/05_encapsulation_and_properties.py) |
| **Ch. 23 — Final Remarks** | Journey synthesis from Zero to OOP and bridge to Data Science, Machine Learning, and Software Engineering | [06_final_journey_industry_bridge.py](examples/06_final_journey_industry_bridge.py) |

Supporting materials for this module:
- Progressive practice challenges: [exercises.md](exercises.md)
- Annotated, testable solutions: [solutions/solved_exercises.py](solutions/solved_exercises.py)
- Capstone project integrating all 5 modules: [Final Project — AutoPy System](../../final_project/README.md)

---

## 1. Chapter 21 — Object-Oriented Programming (OOP)

### 1.1 Classes: the "Blueprint" and the "Super Variable"

Up through Module 4, we structured programs with standalone variables, lists, dictionaries, and functions. As systems grow, keeping raw data (such as `model`, `color`, `speed`) separated from the functions that operate on that data quickly turns brittle.

**Object-Oriented Programming (OOP)** solves this by bundling **state** (attributes/data) and **behavior** (methods/actions) into one cohesive unit:
- **Class (`class`)**: the **blueprint** (a house plan or cake mold). In the book, Fernando Feltrin also describes a class as a **"super variable"** capable of holding both data and its own actions.
- **Object (or instance)**: a concrete entity built from that blueprint (an actual house constructed from the plan).

> **Fundamental Fact:** Python is **natively object-oriented**. Even when you write `age = 30` or `name = "Ana"`, Python instantiates the built-in `int` and `str` classes. Running `type(30)` prints `<class 'int'>`.

#### Naming Convention: `PascalCase`
By Python community convention (PEP 8), class names use **PascalCase** (each word starts with an uppercase letter, no underscores):
- Preferred: `class Car:`, `class Person:`, `class BankAccount:`
- Avoid for classes: `class car:` or `class bank_account:` (keep `snake_case` for variables, functions, and methods).

#### Class Attributes vs. Instance Attributes and Methods

```python
class Car:
    wheels = 4  # Class attribute (shared across the blueprint)

    def __init__(self, model: str, color: str) -> None:
        self.model = model  # Instance attribute (unique to this object)
        self.color = color  # Instance attribute

    def action1(self) -> str:  # Method (behavior bound to an instance)
        return f"The {self.color} {self.model} started its engine!"
```

#### Reverse Engineering — line by line

1. `class Car:` — Creates a class object named `Car` in memory and opens its namespace for attributes and methods.
2. `wheels = 4` — Defined directly inside the `class` body (outside any `def`), so it belongs to the **class**. Every instance sees `4` unless overridden locally.
3. `def __init__(self, model: str, color: str) -> None:` — Defines the special initializer method. Python invokes it automatically right after allocating a blank object in memory.
4. `self.model = model` — Writes the `"model"` key into that specific instance's internal dictionary (`instance.__dict__`). Two separate `Car` objects hold independent `model` values.
5. `def action1(self) -> str:` — Every instance method receives `self` as its first parameter. When you call `my_car.action1()`, Python internally translates it into `Car.action1(my_car)`.

> **Classic Pitfall (Attribute Shadowing):** If you run `car1.wheels = 3`, Python does **not** change `Car.wheels`! Instead, it creates a local `wheels` entry inside `car1.__dict__`, shadowing the class attribute only for `car1`. To update the shared default for all instances without a local override, modify `Car.wheels = 3`.

---

### 1.2 Defining a Class: `__init__`, `self`, and `class User`

In the book, one of the core introductory examples builds a `User` (`Usuario`) class with `__init__` and a `welcome` (`boas_vindas`) method:

```python
class User:
    system = "Python Portal"

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def welcome(self) -> str:
        return f"Hello, {self.name}! Welcome to {self.system}."


user1 = User("Mariana", "mariana@example.com")
print(user1.welcome())
```

#### Reverse Engineering — what happens during `User("Mariana", ...)`

1. Python calls `User.__new__(User)` to allocate a fresh, empty instance in memory.
2. Next, it automatically invokes `User.__init__(empty_instance, "Mariana", "mariana@example.com")`.
3. Inside `__init__`, `self` refers to that exact `empty_instance`.
4. `self.name = name` and `self.email = email` populate `user1`'s personal storage (`user1.__dict__`).
5. Calling `user1.welcome()` makes Python look up `welcome` in `user1.__dict__` (not found), climb to `User.__dict__` (found!), bind `user1` as `self`, and evaluate the f-string.
6. When `{self.system}` is evaluated, Python checks `user1.__dict__` (not found), climbs to `User.system`, and retrieves `"Python Portal"`.

Run and inspect this behavior in [01_classes_and_objects.py](examples/01_classes_and_objects.py).

---

### 1.3 Modifying and Inspecting Instance Data (`setattr`, `getattr`, `hasattr`, `delattr`)

Once an object exists, its attributes can be read, updated, added, or deleted at runtime:

1. **Direct assignment** (when the attribute name is fixed in source code):
   ```python
   user1.name = "Mariana Silva"
   ```
2. **Built-in dynamic attribute functions** (essential when attribute names come from strings, JSON payloads, config files, or user input):
   - `hasattr(obj, "attr_name")` → returns `True` or `False` indicating whether the attribute exists on the object (or its class hierarchy).
   - `getattr(obj, "attr_name", default)` → retrieves an attribute value by string name; passing `default` prevents `AttributeError` if missing.
   - `setattr(obj, "attr_name", new_value)` → updates an existing attribute **or creates** a new one dynamically.
   - `delattr(obj, "attr_name")` → deletes the attribute from the instance. Accessing it afterward raises `AttributeError`.

#### Reverse Engineering — why these built-ins matter

```python
field = "plan"
setattr(user1, field, "Pro")
if hasattr(user1, "plan"):
    print(getattr(user1, "plan"))
delattr(user1, "plan")
```

- Writing `user1.field = "Pro"` would create an attribute literally named `field`, **not** `plan`.
- `setattr(user1, field, "Pro")` evaluates the variable `field` (`"plan"`) and assigns `user1.__dict__["plan"] = "Pro"`.
- `delattr(user1, "plan")` removes `"plan"` from `user1.__dict__`. Any subsequent `user1.plan` lookup fails with `AttributeError` (unless a class attribute named `plan` exists).

See the runnable walkthrough in [02_instances_and_dynamic_attributes.py](examples/02_instances_and_dynamic_attributes.py).

---

### 1.4 Applying Recursion

**Recursion** happens when a function or method calls **itself** on a smaller subproblem until it reaches a **stopping condition (base case)**.

Without a base case, recursive calls keep piling onto the call stack until Python halts with `RecursionError: maximum recursion depth exceeded`.

#### Book Pattern: recursive counter (`print_numbers(maximum, current)`)

```python
def print_numbers(maximum: int, current: int = 1) -> None:
    if current > maximum:  # Stopping condition (base case)
        return
    print(current)
    print_numbers(maximum, current + 1)  # Recursive step toward base case
```

#### Reverse Engineering — tracing the Call Stack

When calling `print_numbers(3, 1)`:
1. Frame 1: `maximum=3, current=1`. `1 > 3` is `False`. Prints `1`. Calls `print_numbers(3, 2)` and **pauses**.
2. Frame 2: `maximum=3, current=2`. `2 > 3` is `False`. Prints `2`. Calls `print_numbers(3, 3)` and **pauses**.
3. Frame 3: `maximum=3, current=3`. `3 > 3` is `False`. Prints `3`. Calls `print_numbers(3, 4)` and **pauses**.
4. Frame 4: `maximum=3, current=4`. `4 > 3` is `True` → **base case reached!** Executes `return`.
5. Frame 4 unwinds back to Frame 3, then Frame 2, then Frame 1, completing execution cleanly.

In OOP, recursion shines when traversing **tree or hierarchical structures** (like nested fleet categories, organizational charts, or folder trees) and cumulative calculations (such as progressive multi-day discounts).

Explore both the book's counter and recursive OOP tree traversal in [03_recursion.py](examples/03_recursion.py).

---

### 1.5 Inheritance (`Cars` → `Gol`, `Corsa`, `super()`)

**Inheritance** lets you define a child class (**subclass**) from a parent class (**superclass**), automatically reusing attributes and methods without duplicating code (DRY principle).

Syntax: `class Subclass(Superclass):`

```python
class Cars:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def describe(self) -> str:
        return f"Car: {self.name} | Color: {self.color}"


class Gol(Cars):
    def __init__(self, name: str, color: str, engine: str = "1.0") -> None:
        super().__init__(name, color)
        self.engine = engine


class Corsa(Cars):
    def __init__(self, name: str, color: str, doors: int = 4) -> None:
        super().__init__(name, color)
        self.doors = doors
```

> **Watch Out / Book Errata Note (`__init__` vs `__int__`):**  
> In the original Portuguese edition of the book, the `Corsa` class contains a famous typo: `def __int__(self, name, color):` instead of `def __init__(self, name, color):` (missing the second `i`!).  
> **What goes wrong if you type `__int__`?**  
> In Python, `__int__` is **not** the class initializer — it is the special magic method invoked by `int(obj)`! If `Corsa` defines `__int__` instead of `__init__`:
> 1. Instantiating `Corsa("Corsa Wind", "Silver", 2)` falls back to the inherited `Cars.__init__` (which only accepts `name` and `color`), raising a `TypeError` if extra parameters are passed — or silently skipping `Corsa`'s custom setup!
> 2. Calling `int(corsa_instance)` would trigger that method instead of initialization.  
> **Always verify:** the initializer has **two `i`s** → **`__init__`**.

#### Reverse Engineering — how `super()` works

1. Instantiating `Gol("Gol G5", "White", "1.6")` enters `Gol.__init__`.
2. `super().__init__(name, color)` locates the next `__init__` along the **MRO** (*Method Resolution Order*, inspectable via `Gol.__mro__`), which is `Cars.__init__`.
3. `Cars.__init__` writes `self.name` and `self.color` onto the **same `self` instance** (which is a `Gol`).
4. Control returns to `Gol.__init__`, which stores `self.engine = engine`.
5. `isinstance(gol, Gol)` is `True` and `isinstance(gol, Cars)` is also `True`. `issubclass(Gol, Cars)` is `True`.

---

### 1.6 Polymorphism (Overriding and Extending with `super()`)

**Polymorphism** means "many forms": distinct classes respond to the **same method interface** with specialized behavior.

There are two primary ways subclasses implement polymorphism:
1. **Complete Override:** the subclass replaces the parent method completely while preserving its name and signature.
2. **Extension with `super()`:** the subclass calls `super().method(...)` to reuse the parent logic and adds specialized behavior on top.

```python
class BaseVehicle:
    def __init__(self, model: str, base_rate: float) -> None:
        self.model = model
        self.base_rate = base_rate

    def calculate_daily_rate(self) -> float:
        return self.base_rate


class EconomyCar(BaseVehicle):
    def calculate_daily_rate(self) -> float:
        # Override with a 10% economy discount
        return round(self.base_rate * 0.90, 2)


class ExecutiveCar(BaseVehicle):
    def calculate_daily_rate(self) -> float:
        # Extension via super() + fixed executive fee
        return round(super().calculate_daily_rate() + 45.0, 2)
```

Code iterating over `fleet = [EconomyCar(...), ExecutiveCar(...)]` simply calls `vehicle.calculate_daily_rate()` inside a `for` loop — **zero `if/elif` chains checking vehicle types**!

Run and inspect MRO and polymorphism in [04_inheritance_and_polymorphism.py](examples/04_inheritance_and_polymorphism.py).

---

### 1.7 Encapsulation, *Name Mangling*, and `@property`

In the book, Fernando Feltrin introduces **encapsulation** using the **medicine capsule analogy**: a capsule protects the active ingredients from contamination or improper handling while giving the user a safe, controlled interface. In OOP, encapsulation shields internal object state from invalid mutations and exposes safe public accessors.

#### Visibility Conventions and Mechanisms in Python

| Syntax | Technical Term | Actual Python Behavior |
|---|---|---|
| `self.model` | Public | Unrestricted access inside and outside the class. |
| `self._mileage` | Protected (convention) | Does **not** block external access, but signals to developers: *"internal/subclass detail; do not mutate directly"*. |
| `self.__chassis` | Private (*name mangling*) | Python rewrites the attribute internally to `self._ClassName__chassis`, preventing accidental outside access and name collisions in subclasses. |

#### Technical Clarification on `__object__` (Dunders) Mentioned in the Book

In some introductory explanations, the book mentions `__object__` (double underscores on both sides) when discussing access control. Here is the exact technical distinction so you never hit subtle bugs:
- **`__attribute`** (double leading underscores, **not** double trailing underscores) → triggers ***name mangling*** (`_ClassName__attribute`), Python's real mechanism for class-private attributes.
- **`__name__`** (double leading **and** double trailing underscores — called *dunders*, short for *double underscore*) → **does NOT trigger *name mangling***! That syntax is reserved by Python's **data model protocol** for special methods (`__init__`, `__str__`, `__repr__`, `__len__`). Never invent custom `__my_data__` names expecting privacy; use `_protected`, `__private`, and `@property`.

#### The Pythonic Way: `@property` + `@prop.setter`

Instead of Java-style `get_balance()` / `set_balance()` methods, Python lets you guard an internal attribute behind `@property` while keeping clean attribute syntax (`account.balance`):

```python
class FleetAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = 0.0
        self.balance = initial_balance  # Routed through the setter!

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = float(amount)
```

#### Reverse Engineering — what happens on `self.balance = initial_balance`

1. During `__init__`, Python sees that `balance` on the class is a `property` descriptor.
2. Instead of writing directly to `self.__dict__["balance"]`, it invokes the `@balance.setter` method.
3. Passing `-100` immediately triggers `ValueError`, guaranteeing that **no object can ever be constructed or left in an invalid state**.

See encapsulation and *name mangling* live in [05_encapsulation_and_properties.py](examples/05_encapsulation_and_properties.py).

---

## 2. Chapter 23 — Final Remarks: From Zero to Modern Engineering

We have reached the culmination of the book's roadmap:
1. **Module 1 (Chs. 1–8):** Programming logic, Python history & philosophy, variables, primitive types, comments, and basic functions.
2. **Module 2 (Chs. 9–12):** Operators, conditionals, `while`/`for` loops, and advanced string formatting.
3. **Module 3 (Chs. 13–17):** Lists, tuples, LIFO stacks, dictionaries, sets, modern f-string interpolation, and functions (`*args`, `**kwargs`).
4. **Module 4 (Chs. 18–20 & 22):** Introspection (`dir`, `help`), standard library builtins, modular packages, and safe exception handling (`try`/`except`/`else`/`finally`).
5. **Module 5 (Chs. 21 & 23):** Full Object-Oriented Programming (classes, instances, recursion, inheritance, polymorphism, and encapsulation).

### Bridge to Data Science, Machine Learning, and Software Engineering

Everything you mastered directly powers real-world Python ecosystems:

| Field | How OOP and this course's foundations show up |
|---|---|
| **Data Science** | In `pandas`, a `DataFrame` is a class: `df.shape` is a `@property`/attribute, and `df.groupby()` is a method returning chainable objects. |
| **Machine Learning & AI** | In `scikit-learn`, models (`LinearRegression`, `RandomForestClassifier`) share a polymorphic interface: `.fit()`, `.predict()`, `.score()`. In `PyTorch`, neural networks inherit from `nn.Module` via `super().__init__()` and override `forward()`. |
| **Software & Backend Engineering** | ORMs like Django and SQLAlchemy map database tables to **classes**; FastAPI validates JSON schemas with Pydantic classes; `pytest` enforces class and exception contracts automatically. |

Inspect a mini polymorphic ML-style pipeline in [06_final_journey_industry_bridge.py](examples/06_final_journey_industry_bridge.py).

---

## Running Examples and Tests

From the repository root:

```bash
# Run any example script directly
python modules/module_05_oop/examples/01_classes_and_objects.py
python modules/module_05_oop/examples/04_inheritance_and_polymorphism.py

# Run the Module 5 & Final Project test suite
python -m pytest tests/test_module_05_and_project.py -v
```

Next steps: tackle [exercises.md](exercises.md), verify against [solutions/solved_exercises.py](solutions/solved_exercises.py), and explore the [AutoPy Final Integrator Project](../../final_project/README.md)!
