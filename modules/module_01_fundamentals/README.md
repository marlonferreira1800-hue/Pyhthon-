# Module 1 — Fundamentals, Logic, and First Commands

> **Book Reference:** Chapters **1 to 8** of *"Python from Zero to Object-Oriented Programming"* (*Python do ZERO à Programação Orientada a Objetos*, Updated and Expanded Edition) by **Fernando Feltrin**.  
> **Methodology:** Self-taught learning through **Line-by-Line Reverse Engineering** — before merely copying code, you will understand *what* each line does, *in what order* Python evaluates it, and *why* it succeeds (or fails).

**Quick Navigation:** [Course Home](../../README.md) | [Full Syllabus](../../SYLLABUS.md) | [Environment Guide](../../ENVIRONMENT_GUIDE.md) | [Module 1 Exercises](exercises.md) | [Solved Exercises](solutions/solved_exercises.py) | [Next: Module 2](../module_02_control_flow_strings/README.md)

---

## Table of Contents

1. [Chapter 1 — Introduction to Python and Its Philosophy](#chapter-1--introduction-to-python-and-its-philosophy)
2. [Chapter 2 — Programming Environment and Computing Layers](#chapter-2--programming-environment-and-computing-layers)
3. [Chapter 3 — Programming Logic, Syntax, Keywords, and Indentation](#chapter-3--programming-logic-syntax-keywords-and-indentation)
4. [Chapter 4 — Basic Program Structure ("Batteries Included")](#chapter-4--basic-program-structure-batteries-included)
5. [Chapter 5 — Core Data Types](#chapter-5--core-data-types)
6. [Chapter 6 — Comments and Documentation](#chapter-6--comments-and-documentation)
7. [Chapter 7 — Variables and Objects in Memory](#chapter-7--variables-and-objects-in-memory)
8. [Chapter 8 — Basic Functions, Formatting, and Type Conversion](#chapter-8--basic-functions-formatting-and-type-conversion)
9. [Example Scripts Map](#example-scripts-map)

---

## Chapter 1 — Introduction to Python and Its Philosophy

### Why Program, and Why Choose Python?

Programming is the craft of translating human problem-solving into exact instructions a computer can execute. **Python** stands out both as a beginner-friendly entry point and as an industry powerhouse because it combines **syntactic simplicity** with **expressive depth**.

Compare the classic **"Hello World"** across three major languages:

```c
/* C (compiled, requires header include, main function, braces, and semicolons) */
#include <stdio.h>

int main() {
    printf("Hello World!\n");
    return 0;
}
```

```java
// Java (strictly object-oriented boilerplate with class and verbose entry point)
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

```python
# Python (interpreted, direct, and readable)
print('Hello World!')
```

**Line-by-Line Reverse Engineering:**
- In C and Java, before expressing your intent ("display text"), you must write ceremonial scaffolding (`#include`, `public class`, `static void main`, `{ }`, and `;`).
- In Python — a **high-level, interpreted language** — you jump straight to the problem logic. The Python interpreter reads your `.py` file, compiles it internally to **bytecode**, and runs it on the Python Virtual Machine without requiring a manual binary build step.
- Thanks to this clarity paired with high-performance C/Rust-backed libraries, Python leads fields such as **Data Science**, **Machine Learning / AI**, automation, backend web engineering, scientific computing, and **blockchain** tooling.

### A Brief History and Guido van Rossum

| Milestone | What Happened |
| :--- | :--- |
| **1989** | **Guido van Rossum** conceives Python during Christmas break at CWI (Netherlands), inspired by the ABC language and named after *Monty Python's Flying Circus*. |
| **1991** | First public release (`0.9.0`), already featuring functions, exception handling, and core types like `list` and `str`. |
| **1994** | Official **Python 1.0** release, adding functional tools such as `lambda`, `map`, `filter`, and `reduce`. |
| **2000 / 2008** | **Python 2.0** (cycle-detecting GC, list comprehensions) and **Python 3.0** (modern Unicode-first architecture). |
| **2009 (Licensing milestone)** | Consolidation of open-source distribution under an **OSI / MIT-compatible** permissive license model (PSF License), accelerating enterprise, academic, and open-source adoption. |

### Python's Philosophy: The 19 Principles of *The Zen of Python*

Written by **Tim Peters**, *The Zen of Python* is built right into Python: running `import this` reveals all **19 aphorisms** that shape Pythonic design.

| # | Principle | Practical Meaning |
| :-: | :--- | :--- |
| 1 | *Beautiful is better than ugly.* | Clean structure makes software easier to understand and maintain. |
| 2 | *Explicit is better than implicit.* | Make intent unmistakable rather than hiding magic behavior. |
| 3 | *Simple is better than complex.* | Prefer straightforward solutions over over-engineered ones. |
| 4 | *Complex is better than complicated.* | When a domain is inherently complex, keep parts organized rather than tangled. |
| 5 | *Flat is better than nested.* | Avoid deep chains of nested `if` blocks. |
| 6 | *Sparse is better than dense.* | Give code visual breathing room instead of cramming logic onto one line. |
| 7 | *Readability counts.* | Code is read by humans far more often than it is written. |
| 8 | *Special cases aren't special enough to break the rules.* | Consistency beats ad-hoc exceptions. |
| 9 | *Although practicality beats purity.* | Real-world usefulness outweighs rigid dogma. |
| 10 | *Errors should never pass silently.* | Never hide failures without handling them. |
| 11 | *Unless explicitly silenced.* | Suppress only specific, expected errors intentionally. |
| 12 | *In the face of ambiguity, refuse the temptation to guess.* | Ask or validate explicitly instead of assuming. |
| 13 | *There should be one-- and preferably only one --obvious way to do it.* | Idiomatic conventions prevent fragmented dialects. |
| 14 | *Although that way may not be obvious at first unless you're Dutch.* | A lighthearted nod to Guido van Rossum. |
| 15 | *Now is better than never.* | Ship progress rather than stalling indefinitely. |
| 16 | *Although never is often better than \*right\* now.* | Think carefully before rushing broken code out the door. |
| 17 | *If the implementation is hard to explain, it's a bad idea.* | Difficulty explaining code signals poor design. |
| 18 | *If the implementation is easy to explain, it may be a good idea.* | Clarity is a strong indicator of solid design. |
| 19 | *Namespaces are one honking great idea -- let's do more of those!* | Isolate names cleanly using modules, classes, and scopes. |

### Companies Using Python and the Future

Major organizations rely on Python in production:
- **Google** and **YouTube** (infrastructure, automation, web services, and AI pipelines);
- **Instagram** (massive Django/Python web backend);
- **Dropbox** (desktop client and synchronization services);
- **Spotify** (backend services, data analysis, recommendations);
- **Reddit** (core web platform powered by Python);
- **Blender 3D** (built-in scripting and 3D pipeline automation);
- **Industrial Light & Magic (ILM)** (cinema visual effects orchestration).

**Will Python be the limit?** As the "universal glue" orchestrating native C/C++/Rust engines (NumPy, PyTorch, Polars), Python continues to expand across AI engineering, data platforms, and automation.

> Practice with: [ch01_introduction_zen.py](examples/ch01_introduction_zen.py)

---

## Chapter 2 — Programming Environment and Computing Layers

### Backend vs. Frontend

- **Frontend:** everything the end user sees and interacts with directly (browser UI with HTML/CSS/JavaScript, mobile apps, desktop GUIs).
- **Backend:** the behind-the-scenes layer executing business logic, validating inputs, querying databases, and powering APIs. Python excels in **backend development**, data pipelines, and automation.

### High-Level, Low-Level, and Machine Languages

| Layer | Examples | How It Works |
| :--- | :--- | :--- |
| **High-level** | Python, Java, C# | Close to human language; abstracts away CPU registers and raw memory addresses. |
| **Low-level (Intermediate / Symbolic)** | **Bytecode** (`.pyc` on the PVM) and **Assembly** (`MOV`, `ADD`) | Python compiles source code to **bytecode** run by the **Python Virtual Machine (PVM)**; Assembly maps almost 1-to-1 to CPU instructions. |
| **Machine language** | **Binary** (`01001000...`) | Sequences of `0`s and `1`s corresponding to electrical voltage states inside CPU **transistors**. |

### Main IDEs and Tools

1. **PyCharm:** Dedicated Python IDE with strong refactoring, debugging, and virtual environment integration.
2. **VS Code:** Lightweight, extensible code editor with first-class Python tooling.
3. **Anaconda:** Data Science distribution bundling Python, `conda`, and scientific libraries.
4. **Jupyter (Notebook / Lab):** Cell-based interactive environment combining live code, Markdown notes, and visualizations.
5. **Terminal / REPL:** Direct command-line execution (`python script.py` or interactive prompt `python`).

For detailed setup and IDE installation steps on your system, see the [Environment Guide](../../ENVIRONMENT_GUIDE.md).

> Practice with: [ch02_environment_levels.py](examples/ch02_environment_levels.py)

---

## Chapter 3 — Programming Logic, Syntax, Keywords, and Indentation

### Algorithms: The Cake Recipe Analogy

An **algorithm** is a finite, ordered, unambiguous sequence of steps to solve a problem — just like a **cake recipe** (measure ingredients, mix in the right sequence, bake for the right duration). Changing the order or skipping a step breaks the outcome.

Algorithms fall into **3 categories** based on input and output:

1. **Input -> Output:** accepts data, processes it, and returns/displays a result (e.g., adding two user-provided numbers).
2. **No Input -> Output:** takes no external data yet produces output (e.g., printing `'Hello World!'` or current system date).
3. **Input -> No Visible Output:** receives data and performs an internal state update or silent storage without printing directly to screen.

### Syntax vs. Logic

Distinguishing **syntax errors** from **logic errors** saves hours of debugging:

```python
# Case 1: LOGIC error (valid syntax, wrong intent for math)
print('5' + '2')   # Output: '52' (string concatenation instead of addition!)

# Case 2: CORRECT logic for arithmetic addition
print(5 + 2)       # Output: 7

# Case 3: SYNTAX error (grammar violation prevents execution)
# Print(5) + 2 =   # SyntaxError! (dangling '=' and uppercase 'Print')
```

**Line-by-Line Reverse Engineering:**
- Line 1: `'5'` and `'2'` are quoted, making them `str` objects. Applying `+` to strings performs **concatenation**, yielding `'52'`. Python raises no error because the syntax is valid, even though the math intent failed.
- Line 2: `5` and `2` are `int` values, so `+` performs numeric addition and returns `7`.
- Line 3 (commented out): `Print(5) + 2 =` breaks Python grammar with a trailing `=` and fails before execution (`SyntaxError`). Also, `Print` with an uppercase `P` would trigger `NameError` because Python is case-sensitive.

### Reserved Keywords

Reserved keywords carry built-in grammatical meaning and **cannot** be used as variable or function names.

> **Version Update Note (Book vs. Python 3.10+):**  
> The book lists **31 classic keywords** (from the Python 2 era, when `print` and `exec` were statements).  
> In **Python 3 (including Python 3.10.11)**, there are **35 official keywords** accessible via `keyword.kwlist`, because `print()` and `exec()` became **built-in functions**, while `nonlocal`, `async`, `await`, `True`, `False`, and `None` are keywords. Python 3.10 also introduces 3 contextual *soft keywords* in `keyword.softkwlist`: `match`, `case`, and `_`.

### Lexical Analysis and Evaluation Order

Python reads scripts **top-to-bottom** and evaluates expressions **left-to-right** (respecting parentheses and operator precedence):

```python
print('You are ' + 3 * 'very ' + 'cool!')
```

**Reverse Engineering this line:**
1. Multiplication `*` has higher precedence than `+`.
2. `3 * 'very '` runs first, producing `'very very very '`.
3. Concatenation `+` proceeds left-to-right: `'You are ' + 'very very very ' + 'cool!'`.
4. Final output: `You are very very very cool!`. *(Without trailing spaces, `'You are' + 3 * 'very' + 'cool!'` glues words together into `'You areveryveryverycool!'`.)*

### Mandatory Indentation and Optional Semicolons

Instead of curly braces `{ }`, Python enforces **indentation** (PEP 8 standard: **4 spaces**) to define code blocks. A trailing semicolon `;` is syntactically optional (often seen as a C/Java habit), but unpythonic.

Corrected positive/negative check from the book:

```python
var1 = '10'
if int(var1) >= 0:
    print('The number is positive (or zero).')
else:
    print('The number is negative.')
```

**Reverse Engineering:**
- Because `input()` always returns a `str`, we wrap `var1` with `int(var1)` **before** comparing `>= 0`. Comparing `'10' >= 0` directly raises `TypeError`.
- The colon `:` opens the conditional block, and the 4-space indentation binds the `print(...)` statement to its branch.

> Practice with: [ch03_logic_syntax_indentation.py](examples/ch03_logic_syntax_indentation.py)

---

## Chapter 4 — Basic Program Structure ("Batteries Included")

Python's **"Batteries included"** philosophy means its standard library ships ready-to-use modules (`math`, `datetime`, `keyword`, `os`, `sys`, etc.) out of the box without installing external packages.

The minimal Python program calls `print()` with arguments inside parentheses:

```python
print('Hello World!!!')
print('Python', 'Batteries', 'Included', sep=' - ', end='!\n')
```

**Reverse Engineering:**
- `print` names the built-in output function.
- Parentheses `( )` invoke the function (mandatory in Python 3).
- Inside parentheses go **arguments**: `'Hello World!!!'` is a positional argument, whereas `sep` and `end` are keyword arguments customizing the separator and line ending.

> Practice with: [ch04_basic_structure.py](examples/ch04_basic_structure.py)

---

## Chapter 5 — Core Data Types

Every value in Python has a concrete type:

| Type | Name | Example | Key Trait |
| :--- | :--- | :--- | :--- |
| `int` | Integer | `42`, `-7`, `0` | Whole numbers with arbitrary precision. |
| `float` | Floating-point | `1.89`, `-0.5`, `3.14` | Decimal numbers using a dot `.` separator. |
| `bool` | Boolean | `True`, `False` | Logical truth values (capitalized). |
| `str` | String | `'Maria'`, `"Python"`, `"""..."""` | Immutable sequence of characters; triple quotes allow **multiline** text. |
| `list` | List | `[1, 'two', 3.0]` | Ordered, **mutable** collection in square brackets `[ ]`. |
| `dict` | Dictionary | `{'name': 'Maria', 'age': 32}` | Key-value mapping in curly braces `{ }`. |
| `tuple` | Tuple | `(10, 20, 30)` | Ordered, **immutable** collection in parentheses `( )`. |

Multiline string example:

```python
note = """Line 1: learning Python
Line 2: inspecting core types
Line 3: preserving line breaks."""
```

> Practice with: [ch05_data_types.py](examples/ch05_data_types.py)

---

## Chapter 6 — Comments and Documentation

Comments exist for human readers; Python ignores `#` annotations at runtime.

1. **Single-line comment (`#`):** everything after `#` on that line is ignored. Very useful for explaining *why* or **commenting out lines to isolate tests**:
   ```python
   var1 = 10
   var2 = 20
   # total = var1 + var2  # Temporarily disabled while testing another calculation
   ```
2. **Triple quotes (`'''...'''` or `"""..."""`):**
   - Placed standalone as the first statement of a module, function, or class, they serve as **docstrings** (official documentation).
   - **Important distinction:** when assigned to a variable (`notice = """Text..."""`), it is **not** a comment — it becomes a real `str` object stored in memory!

> Practice with: [ch06_comments.py](examples/ch06_comments.py)

---

## Chapter 7 — Variables and Objects in Memory

Think of a **variable** as a label attached to a **"memory drawer"** holding an object (you can inspect an object's memory identity with `id()`).

### Key Properties

- **Dynamic typing:** variables don't lock onto a single type forever (`x = 10`, later `x = 'ten'`).
- **Case sensitivity:** `NAME` and `name` are two completely distinct identifiers.

### Naming Rules

| Category | Examples | Notes |
| :--- | :--- | :--- |
| **Allowed and recommended** | `student_name`, `score1`, `tax_rate`, `_internal` | Start with a letter or `_`; follow PEP 8 `snake_case`. |
| **Allowed, discouraged** | `salário` (accents), `NAME` (for regular variables), `a` | Non-ASCII letters hurt portability; ALL_CAPS is reserved by convention for **constants**. |
| **Forbidden (`SyntaxError`)** | `1score`, `my name`, `total-price`, `class` | Cannot start with a digit, contain spaces/hyphens/symbols, or match a keyword. |

### Multiple Assignment and Chained Assignment

```python
# Multiple assignment (tuple unpacking on a single line)
name, age, gender, height = 'Maria', 32, 'F', 1.89

# Chained assignment (multiple labels pointing to the same initial value)
num1 = x = a1 = 10
```

**Reverse Engineering:**
- In multiple assignment, the right-hand values pair positionally with the left-hand variables (`name='Maria'`, `age=32`, `gender='F'`, `height=1.89`).
- In chained assignment, `num1`, `x`, and `a1` all initially reference the integer object `10`. Because integers are immutable, reassigning `x = 20` later simply moves `x`'s label without affecting `num1` or `a1`.

> Practice with: [ch07_variables_objects.py](examples/ch07_variables_objects.py)

---

## Chapter 8 — Basic Functions, Formatting, and Type Conversion

### `print()`, `input()`, and String Formatting Evolution

`input('Prompt: ')` reads user text from standard input and **always returns a `str`**, even when digits are typed.

Python supports three generations of output formatting:

```python
name = 'Maria'
age = 32

# 1. Legacy C-style % placeholders
print('Name: %s | Age: %d' % (name, age))

# 2. .format() method
print('Name: {} | Age: {}'.format(name, age))

# 3. f-strings (Python 3.6+, modern standard)
print(f'Name: {name} | Age: {age}')
```

### Line Breaks `\n` in Practice (Overdue Invoice)

The escape sequence `\n` inserts a newline character:

```python
invoice = f"Customer: {name}\nAmount Due: $250.00\nDue Date: 05/10"
```

### Variable Interaction, `type()`, and Explicit Casting

- **Implicit numeric promotion:** adding `int + float` automatically yields `float` (e.g., `10 + 2.5 -> 12.5`) so fractional precision isn't lost.
- **Inspecting types with `type()`:** `type(12.5)` returns `<class 'float'>`.
- **Explicit casting:** `str()`, `int()`, `float()`.
  - Classic error: `'Age: ' + 15` raises `TypeError` because Python enforces strong typing and refuses to add `str` and `int`. Fix it with `'Age: ' + str(15)` or `f'Age: {15}'`.
  - Curly braces gotcha: `{5}` creates a **`set`**, `{}` creates an empty **`dict`**, and `{'key': 5}` creates a **`dict`**!

> Practice with: [ch08_basic_functions_casting.py](examples/ch08_basic_functions_casting.py)

---

## Example Scripts Map

Every script below can be executed directly with `python <path>` and safely imported without blocking on `input()`:

1. [ch01_introduction_zen.py](examples/ch01_introduction_zen.py) — History, C/Java/Python comparison, 19 Zen of Python principles, companies.
2. [ch02_environment_levels.py](examples/ch02_environment_levels.py) — Backend/Frontend, High-level / Bytecode (`dis`) / Machine binary, IDEs.
3. [ch03_logic_syntax_indentation.py](examples/ch03_logic_syntax_indentation.py) — 3 algorithm types, `'5' + '2'` vs `5 + 2`, 35 keywords (`keyword.kwlist`), lexical analysis, indentation.
4. [ch04_basic_structure.py](examples/ch04_basic_structure.py) — "Batteries included", `print('Hello World!!!')`, `sep` and `end`.
5. [ch05_data_types.py](examples/ch05_data_types.py) — Practical showcase of the 7 core types and multiline strings.
6. [ch06_comments.py](examples/ch06_comments.py) — `#`, standalone vs variable-assigned triple quotes, isolating code.
7. [ch07_variables_objects.py](examples/ch07_variables_objects.py) — Memory drawers (`id()`), dynamic typing, case sensitivity, naming rules, multiple & chained assignment.
8. [ch08_basic_functions_casting.py](examples/ch08_basic_functions_casting.py) — `print()`, safe `input()`, `%s`, `.format()`, `f-strings`, `\n` invoice, `int + float`, `type()`, `{5}` vs `{k: v}`, `str(15)`.

Continue to [Module 1 Exercises](exercises.md) and verify your solutions in [Solved Exercises](solutions/solved_exercises.py).
