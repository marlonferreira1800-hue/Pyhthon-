# Complete Course Syllabus — Python from Zero to OOP

This syllabus maps **all 23 chapters and subtopics** from the book *"Python do ZERO à Programação Orientada a Objetos"* (Updated and Expanded Edition, by **Fernando Feltrin**) to the modular, hands-on, and test-verified structure of this English course repository.

> Quick links: [Course Portal](README.md) · [Environment Guide](ENVIRONMENT_GUIDE.md) · [Final Project (AutoPy)](final_project/README.md) · [Interactive Landing Page](index.html)

---

## 1. Learning Path Overview (5 Modules + Final Project)

| Stage | Book Chapters | Core Focus | Course Materials |
| :--- | :--- | :--- | :--- |
| **Setup** | Preface & Ch. 2 | Reverse-Engineering Methodology, Python 3 setup, and IDEs | [Environment Guide](ENVIRONMENT_GUIDE.md) · [Course Portal](README.md) |
| **Module 1** | Ch. 1–8 | Fundamentals, logic, syntax, data types, comments, variables, and basic I/O | [Lesson](modules/module_01_fundamentals/README.md) · [Examples](modules/module_01_fundamentals/examples/) · [Exercises](modules/module_01_fundamentals/exercises.md) · [Solutions](modules/module_01_fundamentals/solutions/) |
| **Module 2** | Ch. 9–12 | Operators, truth tables, conditionals, loops, and string manipulation | [Lesson](modules/module_02_control_flow_strings/README.md) · [Examples](modules/module_02_control_flow_strings/examples/) · [Exercises](modules/module_02_control_flow_strings/exercises.md) · [Solutions](modules/module_02_control_flow_strings/solutions/) |
| **Module 3** | Ch. 13–17 | Lists, tuples, stacks, dictionaries, sets, interpolation, and functions | [Lesson](modules/module_03_data_structures_functions/README.md) · [Examples](modules/module_03_data_structures_functions/examples/) · [Exercises](modules/module_03_data_structures_functions/exercises.md) · [Solutions](modules/module_03_data_structures_functions/solutions/) |
| **Module 4** | Ch. 18–20 & Ch. 22 | Introspection (`dir`/`help`), builtins, modules/packages, and exceptions | [Lesson](modules/module_04_modules_exceptions/README.md) · [Examples](modules/module_04_modules_exceptions/examples/) · [Exercises](modules/module_04_modules_exceptions/exercises.md) · [Solutions](modules/module_04_modules_exceptions/solutions/) |
| **Module 5** | Ch. 21 & Ch. 23 | Full Object-Oriented Programming and final considerations | [Lesson](modules/module_05_oop/README.md) · [Examples](modules/module_05_oop/examples/) · [Exercises](modules/module_05_oop/exercises.md) · [Solutions](modules/module_05_oop/solutions/) |
| **Final Project** | Integration (Ch. 1–23) | **AutoPy Fleet & Rental System** (`autopy` package + `--demo` CLI) | [Project Docs](final_project/README.md) · [Entrypoint (`main.py`)](final_project/main.py) · [`autopy/` Package](final_project/autopy/) |

> **Pedagogical ordering note:** In the original book, Chapter 21 introduces Object-Oriented Programming and Chapter 22 covers tracebacks and exception handling (`try`/`except`/`finally`). In this course, **Chapter 22** is grouped into **Module 4** alongside modules, packages, and builtins so that **Module 5** is dedicated exclusively to OOP (Chapter 21) and the closing synthesis (Chapter 23), flowing straight into the integrated Final Project.

---

## 2. Detailed Chapter-by-Chapter Book Mapping (All 23 Chapters)

### Preface & Methodology
- **Book subtopics:**
  - Why program? And why in Python?
  - Methodology ("reverse engineering")
- **Where covered:** [Course Portal (`README.md`)](README.md) and [Module 1 — Fundamentals](modules/module_01_fundamentals/README.md)
- **Learning outcome:** Read complete working programs top-to-bottom, execute them, and dissect every line before memorizing abstract syntax rules.

---

### Module 1 — Fundamentals, Logic & First Commands (Chapters 1 to 8)

> Module resources: [Lesson](modules/module_01_fundamentals/README.md) · [Examples](modules/module_01_fundamentals/examples/) · [Exercises](modules/module_01_fundamentals/exercises.md) · [Solutions](modules/module_01_fundamentals/solutions/) · [Tests](tests/test_modules_01_02.py)

| Ch. | Book Chapter | Subtopics Covered |
| :---: | :--- | :--- |
| **1** | **Introduction** | Why Python?; A brief history; Guido Van Rossum; The philosophy of Python (The Zen of Python); Companies using Python; The future of the language; Will Python be the limit? |
| **2** | **Programming Environment** | Backend vs. Frontend; High-level, low-level, and machine languages; Integrated Development Environments (IDEs); Main IDEs (PyCharm, Anaconda, VS Code, Jupyter). *(Expanded in [ENVIRONMENT_GUIDE.md](ENVIRONMENT_GUIDE.md).)* |
| **3** | **Programming Logic** | Algorithms (recipe analogy and input/output flows); Python syntax (syntax errors vs. logic errors); Reserved keywords (`keyword.kwlist`, modern Python 3's 35 keywords vs. the classic 31 list); Lexical analysis (top-to-bottom, left-to-right); Mandatory indentation. |
| **4** | **Basic Program Structure** | *Batteries included* philosophy, first `print('Hello World!!!')` program, and passing arguments inside parentheses. |
| **5** | **Data Types** | Core types (`int`, `float`, `bool`, `str`, `list`, `dict`, `tuple`) and multiline strings (`"""..."""`). |
| **6** | **Comments** | Single-line `#` comments, triple-quoted `'''...'''` / `"""..."""` blocks (and how assigning them creates a string), and commenting lines to isolate code during debugging. |
| **7** | **Variables / Objects** | Memory "drawers" analogy, dynamic typing, case sensitivity, naming conventions; Declaring a single variable; Declaring multiple variables (`a, b = ...`); Declaring multiple variables with the same type/value (`x = y = z = 10`). |
| **8** | **Basic Functions** | `print()`; `input()`; Exploring `print()` (`%s` masks, `.format()`, `f-strings`, newline `\n`); Variable interaction (`int + float`); `type()` and explicit data-type conversion (`int()`, `float()`, `str()`), plus distinguishing `{5}` (`set`) from `{k: v}` (`dict`). |

---

### Module 2 — Operators, Control Flow & Strings (Chapters 9 to 12)

> Module resources: [Lesson](modules/module_02_control_flow_strings/README.md) · [Examples](modules/module_02_control_flow_strings/examples/) · [Exercises](modules/module_02_control_flow_strings/exercises.md) · [Solutions](modules/module_02_control_flow_strings/solutions/) · [Tests](tests/test_modules_01_02.py)

| Ch. | Book Chapter | Subtopics Covered |
| :---: | :--- | :--- |
| **9** | **Operators** | Assignment (`=`); Augmented/special assignments (`+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`); Arithmetic (`+`, `-`, `*`, `/`, `**`, `//`, `%` and precedence); Logical (`and`, `or`, `not` and bitwise `&`, `\|`, `^`); Truth table; Membership (`in`, `not in`); Relational (`>`, `>=`, `<`, `<=`, `==`, `!=`); Operators using variables; Operators using conditionals; Identity (`is` vs. value equality `==`). |
| **10** | **Conditional Statements** | `if`, `elif`, and `else`; `and` and `or` inside conditionals; Nested conditionals; Simulating `switch/case` (via `if/elif`, dictionaries/class patterns, plus Python 3.10+ `match/case`). |
| **11** | **Repetition Structures (Loops)** | `while` (conditions, counters, and `break`); `for` (iterating sequences, `range(0, 6)` and `range(6)`, `for ... else`, and nested `for` loops such as a multiplication table). |
| **12** | **Strings** | Working with strings (single quotes, double quotes, multiline); Formatting a string; `.lower()` and `.upper()` (immutability vs. reassignment); Searching data (`in`); `.split()`; Terminal ANSI color codes (`\033[...]`); Display alignment (`.center()`, `.ljust()`, `.rjust()`); Formatting numbers inside strings (`%.2f`, `%.5f`, and `f"{num:.2f}"`). |

---

### Module 3 — Data Structures, Interpolation & Functions (Chapters 13 to 17)

> Module resources: [Lesson](modules/module_03_data_structures_functions/README.md) · [Examples](modules/module_03_data_structures_functions/examples/) · [Exercises](modules/module_03_data_structures_functions/exercises.md) · [Solutions](modules/module_03_data_structures_functions/solutions/) · [Tests](tests/test_modules_03_04.py)

| Ch. | Book Chapter | Subtopics Covered |
| :---: | :--- | :--- |
| **13** | **Lists** | Adding/removing elements manually and by index (`.append()`, `.remove()`, `del list[i]`); `.index()`; checking membership (`in`); formatting / `.reverse()`; nested lists (lists inside lists); Tuples (`()`, `tuple()`, immutability, single-item tuple `(1,)`, `.index()`, `.count()`); Stacks (LIFO concept: top, `.append()`, `.pop()`, size via `len()`). |
| **14** | **Dictionaries** | `{key: value}` mappings and nested values; `.get()`; `.keys()`; `.values()`; `.items()`; modifying existing keys, appending to nested lists, and adding new entries. |
| **15** | **Numerical Sets (`set`)** | Unordered unique collections without positional indexing; Union (`.union()` / `\|`); Intersection (`.intersection()` / `&`); Subset check (`<=`); Difference (`-`). |
| **16** | **String Interpolation** | Evolution across all three Python syntaxes: legacy `%` (`%s`, `%d`), `.format()` (positional and keyword), and `f-strings` (including inline expressions such as `{3 * age}`). |
| **17** | **Functions** | Predefined (built-in) vs. imported vs. custom functions (`def`); Simple functions without parameters (and implicit `None` return); Compound functions with parameters and `return`; `*args` (tuple of positional varargs) and `**kwargs` (dictionary of keyword arguments). |

---

### Module 4 — Introspection, Builtins, Modules, Packages & Exceptions (Chapters 18, 19, 20 & 22)

> Module resources: [Lesson](modules/module_04_modules_exceptions/README.md) · [Examples](modules/module_04_modules_exceptions/examples/) · [Exercises](modules/module_04_modules_exceptions/exercises.md) · [Solutions](modules/module_04_modules_exceptions/solutions/) · [Tests](tests/test_modules_03_04.py)

| Ch. | Book Chapter | Subtopics Covered |
| :---: | :--- | :--- |
| **18** | **`dir()` and `help()` Commands** | Runtime introspection of objects, data types, methods, and docstrings (`dir(obj)` and `help(obj)`). |
| **19** | **Builtins and Pre-allocated Libraries** | Inspecting `dir(__builtins__)`, preloaded built-in functions and exceptions, special `__...__` dunder names, and importing standard libraries (`import math`, `from math import pi`). |
| **20** | **Modules and Packages** | Code modularization across `.py` files, creating subpackages (`__init__.py` and nested modules), `if __name__ == "__main__":`, aliases (`import ... as ...`), selective imports (`from pkg.mod import fn as alias`), and `sys.path` resolution. |
| **22** | **Tracebacks / Exceptions** | Reading Python tracebacks (`NameError`, `ValueError`, `TypeError`, etc.); `try`, `except` (specific vs. generic handlers), `else`, and `finally` (highlighting the safe pattern that prevents `NameError` when `try` raises early). |

---

### Module 5 — Object-Oriented Programming & Final Considerations (Chapters 21 & 23)

> Module resources: [Lesson](modules/module_05_oop/README.md) · [Examples](modules/module_05_oop/examples/) · [Exercises](modules/module_05_oop/exercises.md) · [Solutions](modules/module_05_oop/solutions/) · [Tests](tests/test_module_05_and_project.py)

| Ch. | Book Chapter | Subtopics Covered |
| :---: | :--- | :--- |
| **21** | **Object-Oriented Programming** | **Classes** (blueprint/"super variable" metaphor, PascalCase, class vs. instance attributes, methods); **Defining a class** (`__init__(self, ...)` and the role of `self`); **Modifying instance attributes** (`setattr`, `getattr`, `hasattr`, `delattr`); **Applying recursion** (recursive functions/methods with base cases); **Inheritance** (parent and child classes using `super().__init__`, fixing the classic `__int__` typo from the book); **Polymorphism** (method overriding and extension with `super()`); **Encapsulation** (capsule analogy, `_protected`, `__private` name mangling, `@property`, and distinguishing Python data-model `__dunder__` methods). |
| **23** | **Final Considerations** | Synthesis of the journey from zero to OOP, ongoing engineering habits, and bridges into Data Science, Machine Learning, Backend APIs, and Software Engineering. |

---

### Final Project — "AutoPy" Fleet & Rental Management System

> Project resources: [Project README](final_project/README.md) · [Entrypoint (`main.py`)](final_project/main.py) · [`autopy/` Package](final_project/autopy/) · [Tests](tests/test_module_05_and_project.py)

The Final Project unifies classic themes from the book (`Car` subclasses, `User`/`Customer`, price calculation, and formatted reports) into a cohesive, modular application:
- **`autopy/` Package:** Clean separation between domain models, services, custom exceptions, and CLI interaction (Chapters 20, 21, and 22).
- **Applied OOP:** Inheritance, polymorphism, encapsulation with `@property`, and `super().__init__` (Chapter 21).
- **Combined Data Structures:** Lists, dictionaries, `set` of available vehicle categories, and an undo stack (`append`/`pop`) for operations (Chapters 13–15).
- **Recursion & Modern Formatting:** Recursive calculations, `f-string` reports, and resilient error handling (Chapters 16, 21, and 22).
- **Dual Execution Modes:** Non-blocking `--demo` run for instant output and automated testing, plus an interactive terminal menu.

---

## 3. Command-Line Navigation & Verification

Run [course_cli.py](course_cli.py) from the repository root to inspect modules or verify file completeness at any time:

```powershell
python course_cli.py --list
python course_cli.py --module 3
python course_cli.py --final
python course_cli.py --check
```
