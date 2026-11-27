# Module 4 — Introspection, Builtins, Modules, Packages, and Exceptions

**Book chapters covered:** Chapters 18, 19, 20, and 22 (*Python from Zero to Object-Oriented Programming*, updated and expanded edition, by Fernando Feltrin).

In this module you learn how to inspect any Python object on your own (`dir()` and `help()`), understand what Python preloads at startup (`__builtins__`), organize growing codebases into clean **modules and packages**, and read **tracebacks** while handling **exceptions** safely.

---

## Table of Contents

1. [Chapter 18 — `dir()` and `help()` Introspection](#chapter-18--dir-and-help-introspection)
2. [Chapter 19 — Builtins and Pre-allocated Libraries](#chapter-19--builtins-and-pre-allocated-libraries)
3. [Chapter 20 — Modules and Packages](#chapter-20--modules-and-packages)
4. [Chapter 22 — Tracebacks and Exception Handling](#chapter-22--tracebacks-and-exception-handling)
5. [How to Run Examples and Exercises](#how-to-run-examples-and-exercises)

---

## Chapter 18 — `dir()` and `help()` Introspection

Whenever you forget a method name or want to explore what a data type supports, ask the Python interpreter directly:

```python
list2 = [10, 20, 30]
attributes = dir(list2)
help(list2)
```

### Reverse Engineering — Line by Line

- **`list2 = [10, 20, 30]`**: creates an instance of `list`.
- **`dir(list2)`**: **introspection** function that returns a list of strings naming every attribute and method on `list2` — including internal dunder methods like `'__len__'` and public methods like `'append'`, `'pop'`, and `'reverse'`.
- **`help(list2)`** (or `help(list2.append)`): displays the built-in documentation (*docstring*) explaining signatures, parameters, and behavior.
- **Practical tip:** filter out internal dunder names when scanning available public methods:
  ```python
  public_methods = [name for name in dir(list2) if not name.startswith("__")]
  ```

---

## Chapter 19 — Builtins and Pre-allocated Libraries

Before you write a single line of code, Python automatically preloads its core namespace called **`__builtins__`** (the `builtins` module).

```python
import builtins
from math import pi
import math

builtin_names = dir(__builtins__)  # In __main__/REPL, equivalent to dir(builtins)
radius = 5
circle_area = pi * radius ** 2
circle_area_qualified = math.pi * math.pow(radius, 2)
```

### Reverse Engineering — Line by Line

- **`dir(__builtins__)`**: lists everything globally available without an `import`. These fall into three groups:
  1. **Preloaded exceptions** (*PascalCase*): `ValueError`, `TypeError`, `NameError`, `ZeroDivisionError`, `KeyError`, `IndexError`, etc.
  2. **Built-in functions and types** (*lowercase*): `print`, `input`, `len`, `int`, `float`, `str`, `list`, `dict`, `set`, `tuple`, `dir`, `help`, `sum`.
  3. **Special dunder identifiers (`__...__`)**: `__name__`, `__doc__`, `__package__`, `__loader__`. Double underscores indicate names reserved for Python internals.
  > **Technical Note:** In `__main__` (or the interactive REPL), `__builtins__` references the `builtins` module directly, whereas inside an imported module `__builtins__` is a `dict`. Using `import builtins; dir(builtins)` inside reusable `.py` files reliably returns all built-in symbols in both contexts.
- **`import math` vs. `from math import pi`**:
  - **`import math`** imports the whole module under the `math` namespace (`math.pi`, `math.sqrt(16)`), preventing name collisions.
  - **`from math import pi`** binds only `pi` into your local namespace, making formulas like **`pi * radius ** 2`** concise and clear.
  - Avoid `from math import *` in production code so variable origins stay explicit.

---

## Chapter 20 — Modules and Packages

As projects grow, putting everything into a single script becomes unmanageable. **Modularization** splits code into individual `.py` files (**modules**) and structured subfolders (**packages**).

### 3.1 Real Example Package Structure (`examples/`)

```text
examples/
├── greetings.py           # Greeting helper module
├── addition.py            # Arithmetic helper module
├── index.py               # Entry script importing local modules and the sales package
└── sales/                 # Python package (subfolder with __init__.py)
    ├── __init__.py
    └── price_calc.py      # Commercial pricing module with increase_price(price, percentage)
```

### 3.2 `if __name__ == "__main__":` and Module Lookup (`sys.path`)

```python
# In sales/price_calc.py
def increase_price(price, percentage):
    return round(price + (price * percentage / 100), 2)


# In index.py
import sys
import greetings
import addition as add_mod
from sales.price_calc import increase_price as apply_markup

if __name__ == "__main__":
    print(greetings.greet("Ana"))
    print(add_mod.add(10, 5))
    print(apply_markup(100.0, 15.0))
    print("Primary search path:", sys.path[0])
```

#### Reverse Engineering — Line by Line

- **What are `__name__` and `"__main__"`?**  
  Every Python module has a built-in `__name__` variable:
  - When executed directly (`python addition.py`), Python sets `__name__ = "__main__"`.
  - When imported (`import addition`), `__name__` inside `addition.py` becomes `"addition"` (or its dotted package path).
  - Wrapping script entry points in **`if __name__ == "__main__":`** ensures demo or CLI code never runs accidentally during an `import`.
- **Aliases with `as`**:
  - `import addition as add_mod`: gives the imported module a shorter or collision-free local name.
  - `from sales.price_calc import increase_price as apply_markup`: imports a specific function from inside a package under a contextual alias.
- **How does Python locate modules?**  
  Python searches entries in **`sys.path`** in order:
  1. First, the **script directory / current working directory** (`sys.path[0]`).
  2. Next, directories listed in the `PYTHONPATH` environment variable.
  3. Finally, Python's standard library and third-party `site-packages`.

---

## Chapter 22 — Tracebacks and Exception Handling

When a runtime error occurs, Python stops normal execution and prints a **Traceback**.

### 4.1 Reading a Traceback (always bottom-up!)

```text
Traceback (most recent call last):
  File "example.py", line 4, in <module>
    value = int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
```

1. **Bottom line (what happened):** exception type (`ValueError`) and exact message (`'abc'` cannot be parsed as base-10 integer).
2. **Line right above (where):** file path, line number (`line 4`), and the failing expression.
3. **Lines above that (how execution got there):** the call stack leading to the failure.

#### Common Beginner Exceptions

- **`NameError`**: referencing an undefined variable or misspelled identifier.
- **`ValueError`**: the type is right, but the value itself is invalid (e.g., `int("abc")`).
- **`TypeError`**: applying an operation to incompatible types (e.g., `"10" + 5` or `len(123)`).
- **`ZeroDivisionError`**: dividing by zero (`10 / 0`).

### 4.2 `try`, `except` (Specific vs. Bare/Generic), `else`, and `finally`

**Why always specify the exception type in `except`?**  
Writing a bare `except:` (or catching broad `Exception` silently) masks unrelated bugs (like typos causing `NameError`) and prevents clear error messages. Always catch the exact exception classes you expect, such as `except ValueError:`.

### 4.3 Important Pedagogical Note on Page 213 of the Book (and the Correct Pattern)

In the book's example on page 213, `num1` and `num2` are assigned inside `try`, an error is caught in `except`, and **`finally`** attempts to compute `num1 + num2`:

```python
# ANTIPATTERN (book p. 213 bug):
# try:
#     num1 = int(input("Number 1: "))
#     num2 = int(input("Number 2: "))
# except ValueError:
#     print("Invalid input!")
# finally:
#     print(num1 + num2)  # If try failed on num1, num1 does NOT exist -> NameError!
```

Because `finally` **always executes**—even after an exception—it attempts to evaluate `num1 + num2` when those variables were never bound, crashing with a secondary `NameError`!

#### 100% Working Pattern (`try` / `except` / `else` / `finally`)

```python
def safe_add_inputs(text1: str, text2: str) -> dict:
    result = None
    error = None
    finalized = False

    try:
        num1 = int(text1)
        num2 = int(text2)
    except ValueError:
        error = "Please provide valid integer strings."
    except TypeError:
        error = "Incompatible types provided for integer conversion."
    else:
        # Runs ONLY when the try block completed with zero exceptions!
        result = num1 + num2
    finally:
        # Runs ALWAYS (success or error) and never depends on try-scoped variables!
        finalized = True

    return {"result": result, "error": error, "finalized": finalized}
```

- **`try`**: isolate only the risky lines (parsing `text1` and `text2`).
- **`except ValueError` / `except TypeError`**: specific, informative recovery per failure mode.
- **`else`**: guaranteed safe zone where `num1` and `num2` definitely exist.
- **`finally`**: unconditional cleanup/audit step with zero reliance on uninitialized variables.

---

## How to Run Examples and Exercises

From the repository root:

```bash
python modules/module_04_modules_exceptions/examples/ch18_introspection_dir_help.py
python modules/module_04_modules_exceptions/examples/ch19_builtins_and_math.py
python modules/module_04_modules_exceptions/examples/greetings.py
python modules/module_04_modules_exceptions/examples/addition.py
python modules/module_04_modules_exceptions/examples/sales/price_calc.py
python modules/module_04_modules_exceptions/examples/index.py
python modules/module_04_modules_exceptions/examples/ch22_tracebacks_exceptions.py
python modules/module_04_modules_exceptions/solutions/solved_exercises.py
```

Work through [exercises.md](exercises.md) first, then compare with [solutions/solved_exercises.py](solutions/solved_exercises.py).
