# Python from Zero to Object-Oriented Programming — Hands-On Course

A complete, self-paced, hands-on **Python 3** course in English, based on the book **"Python do ZERO à Programação Orientada a Objetos"** (Updated and Expanded Edition, by **Fernando Feltrin**).

> **Course Mission:** Turn all 23 chapters of the book into an executable learning repository featuring line-by-line reverse-engineering lessons, runnable example scripts, 3-tier exercises, testable solutions, an integrated OOP final project, an interactive web landing page, and automated `pytest` verification.

- **Interactive Course Showcase:** [Open Landing Page (`index.html`)](index.html)
- **Official GitHub Repository:** [github.com/marlonferreira1800-hue/Pyhthon-](https://github.com/marlonferreira1800-hue/Pyhthon-.git)
- **Full 23-Chapter Map:** [Complete Syllabus (`SYLLABUS.md`)](SYLLABUS.md)
- **Setup & IDEs:** [Programming Environment Guide (`ENVIRONMENT_GUIDE.md`)](ENVIRONMENT_GUIDE.md)

---

## Methodology: "Reverse Engineering" & Guided Practice

Following the book's pedagogical philosophy, this course uses a **reverse-engineering** workflow:

1. **Read real code first:** Instead of memorizing dry definitions upfront, start by seeing a complete working script.
2. **Dissect line by line:** Each module's `README.md` and `examples/*.py` scripts break down why every keyword, operator, data type, and indentation rule works the way it does.
3. **Preserve the book + modernize for Python 3.10+:** The curriculum stays faithful to the book's progression while adding practical Python 3.10+ clarifications (e.g., `keyword.kwlist`, `match/case`, `is` vs. `==`, `*args` as `tuple`, `__init__` inheritance fixes, and safe `try/except/else/finally` patterns).
4. **Practice and verify automatically:** Solve progressive tasks in `exercises.md` (Basic, Intermediate, Challenge), compare against `solutions/`, and verify behavior with `pytest`.

---

## Quick Start

1. **Set up your tools:** Read the [Environment Guide](ENVIRONMENT_GUIDE.md) (Backend vs. Frontend, language levels, Python 3.10+ installation, PyCharm, VS Code, Anaconda/Jupyter, and terminal usage).
2. **Browse the full curriculum:** Review the [Complete Syllabus](SYLLABUS.md) covering the Preface and Chapters 1–23.
3. **Explore via the course CLI:**
   ```powershell
   python course_cli.py --list
   python course_cli.py --check
   ```

---

## Complete Learning Track (5 Modules + Final Project)

| Module | Book Chapters | What You Will Master | Direct Links |
| :--- | :--- | :--- | :--- |
| **Module 1** | Ch. 1–8 | Python's history & Zen, environment, logic & lexical analysis, program structure, data types, comments, variables/objects, and basic I/O (`print`, `input`, conversions) | [Module 1 Lesson](modules/module_01_fundamentals/README.md) · [Examples](modules/module_01_fundamentals/examples/) · [Exercises](modules/module_01_fundamentals/exercises.md) · [Solutions](modules/module_01_fundamentals/solutions/) |
| **Module 2** | Ch. 9–12 | Assignment, arithmetic, logical, truth tables, membership, relational, and identity operators; `if/elif/else`; `while`/`for` loops; string methods, ANSI colors, and formatting | [Module 2 Lesson](modules/module_02_control_flow_strings/README.md) · [Examples](modules/module_02_control_flow_strings/examples/) · [Exercises](modules/module_02_control_flow_strings/exercises.md) · [Solutions](modules/module_02_control_flow_strings/solutions/) |
| **Module 3** | Ch. 13–17 | Lists, tuples, LIFO stacks, dictionaries, sets, string interpolation (`%`, `.format()`, `f-strings`), and functions (`def`, `return`, `*args`, `**kwargs`) | [Module 3 Lesson](modules/module_03_data_structures_functions/README.md) · [Examples](modules/module_03_data_structures_functions/examples/) · [Exercises](modules/module_03_data_structures_functions/exercises.md) · [Solutions](modules/module_03_data_structures_functions/solutions/) |
| **Module 4** | Ch. 18–20 & 22 | Runtime introspection (`dir`, `help`), `__builtins__`, standard libraries (`math`), modularization with modules and packages, and `try/except/else/finally` | [Module 4 Lesson](modules/module_04_modules_exceptions/README.md) · [Examples](modules/module_04_modules_exceptions/examples/) · [Exercises](modules/module_04_modules_exceptions/exercises.md) · [Solutions](modules/module_04_modules_exceptions/solutions/) |
| **Module 5** | Ch. 21 & 23 | Object-Oriented Programming: classes, `__init__`, `self`, `setattr`/`delattr`, recursion, inheritance, polymorphism, encapsulation, and closing synthesis | [Module 5 Lesson](modules/module_05_oop/README.md) · [Examples](modules/module_05_oop/examples/) · [Exercises](modules/module_05_oop/exercises.md) · [Solutions](modules/module_05_oop/solutions/) |
| **Final Project** | Integration (Ch. 1–23) | **AutoPy Fleet & Rental System**: modular Python package combining OOP, collections, an undo stack, recursion, custom exceptions, and a dual-mode CLI | [Project README](final_project/README.md) · [Entrypoint (`main.py`)](final_project/main.py) · [`autopy/` Package](final_project/autopy/) |

---

## Repository Structure

```text
curso-python-do-zero-a-poo/
├── README.md                  # Course home portal (this file)
├── SYLLABUS.md                # Full mapping of all 23 chapters and subtopics
├── ENVIRONMENT_GUIDE.md       # Chapter 2 guide: Backend/Frontend, IDEs, Python 3, terminal
├── course_cli.py              # Standard-library CLI navigator (--list, --module, --check)
├── pyproject.toml             # Project metadata and pytest config (Python >= 3.10)
├── index.html                 # Interactive landing page (course overview & reverse-engineering lab)
├── modules/
│   ├── module_01_fundamentals/
│   │   ├── README.md
│   │   ├── examples/
│   │   ├── exercises.md
│   │   └── solutions/
│   ├── module_02_control_flow_strings/
│   │   ├── README.md
│   │   ├── examples/
│   │   ├── exercises.md
│   │   └── solutions/
│   ├── module_03_data_structures_functions/
│   │   ├── README.md
│   │   ├── examples/
│   │   ├── exercises.md
│   │   └── solutions/
│   ├── module_04_modules_exceptions/
│   │   ├── README.md
│   │   ├── examples/
│   │   ├── exercises.md
│   │   └── solutions/
│   └── module_05_oop/
│       ├── README.md
│       ├── examples/
│       ├── exercises.md
│       └── solutions/
├── final_project/
│   ├── README.md
│   ├── main.py
│   └── autopy/
└── tests/
    ├── test_modules_01_02.py
    ├── test_modules_03_04.py
    └── test_module_05_and_project.py
```

---

## Useful Commands: Navigate, Run Examples & Test

Run all commands from the repository root directory:

### 1. Browse and validate the course with `course_cli.py`

```powershell
# List all discovered modules, chapters, and completion status
python course_cli.py --list

# Inspect details, example scripts, solutions, and commands for Module N (1–5)
python course_cli.py --module 1
python course_cli.py --module 5

# Inspect the Final Project layout and commands
python course_cli.py --final

# Check structural integrity across portal, modules, final project, and tests
python course_cli.py --check
```

### 2. Run module examples and solutions

```powershell
# Discover exact script paths in Module 1
python course_cli.py --module 1

# Run any example or solution script directly with Python
python modules/module_01_fundamentals/examples/<example_script>.py
```

### 3. Run the Final Project ("AutoPy")

```powershell
# Non-blocking automated demo mode (prints formatted fleet/rental report and exits 0)
python final_project/main.py --demo

# Interactive terminal menu mode
python final_project/main.py
```

### 4. Run the automated `pytest` suite

Configuration in [pyproject.toml](pyproject.toml) automatically sets `testpaths = ["tests"]` and adds the root directory to `PYTHONPATH`:

```powershell
# Run the complete test suite
python -m pytest -v

# Run tests for individual module groups
python -m pytest tests/test_modules_01_02.py -v
python -m pytest tests/test_modules_03_04.py -v
python -m pytest tests/test_module_05_and_project.py -v
```

*(Test suites: [test_modules_01_02.py](tests/test_modules_01_02.py), [test_modules_03_04.py](tests/test_modules_03_04.py), and [test_module_05_and_project.py](tests/test_module_05_and_project.py).)*
