# Module 2 — Operators, Control Flow, and Strings

> **Book Reference:** Chapters **9 to 12** of *"Python from Zero to Object-Oriented Programming"* (*Python do ZERO à Programação Orientada a Objetos*, Updated and Expanded Edition) by **Fernando Feltrin**.  
> **Methodology:** Self-taught learning through **Line-by-Line Reverse Engineering** — dissecting precedence, memory identity, control branches, loop state, and string immutability.

**Quick Navigation:** [Course Home](../../README.md) | [Full Syllabus](../../SYLLABUS.md) | [Previous: Module 1](../module_01_fundamentals/README.md) | [Module 2 Exercises](exercises.md) | [Solved Exercises](solutions/solved_exercises.py) | [Next: Module 3](../module_03_data_structures_functions/README.md)

---

## Table of Contents

1. [Chapter 9 — Operators, Precedence, Truth Tables, and `is` vs. `==`](#chapter-9--operators-precedence-truth-tables-and-is-vs-)
2. [Chapter 10 — Conditional Structures (`if`, `elif`, `else`, `match/case`)](#chapter-10--conditional-structures-if-elif-else-matchcase)
3. [Chapter 11 — Repetition Structures (`while`, `for`, `for...else`)](#chapter-11--repetition-structures-while-for-forelse)
4. [Chapter 12 — Strings, ANSI Colors, Alignment, and Numeric Formatting](#chapter-12--strings-ansi-colors-alignment-and-numeric-formatting)
5. [Example Scripts Map](#example-scripts-map)

---

## Chapter 9 — Operators, Precedence, Truth Tables, and `is` vs. `==`

### Assignment (`=`) and Compound Assignment Operators

The single equal sign `=` **assigns** a value to a variable (it does *not* test equality). You can update a variable from its previous value or from user input:

```python
balance = 100.0
balance = balance + 50.0  # Reassigns balance -> 150.0
```

Compound assignment operators provide a concise shorthand:

| Operator | Example | Equivalent To | Meaning |
| :-: | :--- | :--- | :--- |
| `+=` | `x += 5` | `x = x + 5` | Add and assign |
| `-=` | `x -= 3` | `x = x - 3` | Subtract and assign |
| `*=` | `x *= 2` | `x = x * 2` | Multiply and assign |
| `/=` | `x /= 4` | `x = x / 4` | Float divide and assign |
| `//=` | `x //= 4` | `x = x // 4` | Floor divide and assign |
| `%=` | `x %= 3` | `x = x % 3` | Modulo (remainder) and assign |
| `**=` | `x **= 2` | `x = x ** 2` | Exponentiate and assign |

### Arithmetic Operators and Precedence

| Operator | Name | Example | Result |
| :-: | :--- | :--- | :--- |
| `+` | Addition | `7 + 2` | `9` |
| `-` | Subtraction | `7 - 2` | `5` |
| `*` | Multiplication | `7 * 2` | `14` |
| `/` | True division (always `float`) | `7 / 2` | `3.5` |
| `**` | Exponentiation | `2 ** 3` | `8` |
| `//` | Floor (integer) division | `7 // 2` | `3` |
| `%` | Modulo (remainder) | `7 % 2` | `1` |

**Precedence order (highest to lowest):**
1. Parentheses `( )`
2. Exponentiation `**` (right-to-left)
3. Unary signs `+x`, `-x`
4. `*`, `/`, `//`, `%` (left-to-right)
5. `+`, `-` (left-to-right)

### Logical Operators, Truth Tables, and Bitwise Operators

Logical operators (`and`, `or`, `not`) combine boolean conditions. Python also provides bitwise operators (`&`, `|`, `^`) that act bit-by-bit on integers (and on `bool`, since `bool` subclasses `int`).

| `A` | `B` | `A and B` (AND) | `A or B` (OR) | `A ^ B` / `A != B` (XOR) | `not A` (NOT) |
| :-: | :-: | :-: | :-: | :-: | :-: |
| `True` | `True` | `True` | `True` | `False` | `False` |
| `True` | `False` | `False` | `True` | `True` | `False` |
| `False` | `True` | `False` | `True` | `True` | `True` |
| `False` | `False` | `False` | `False` | `False` | `True` |

**Bitwise vs. Logical:**
- `and` / `or` use **short-circuit evaluation** and work on truthiness of any Python object.
- `&` (bitwise AND), `|` (bitwise OR), and `^` (bitwise XOR) evaluate both operands and operate on binary bits (e.g., `6 & 3 -> 2` because `110 & 011 == 010`, `6 | 3 -> 7`, `6 ^ 3 -> 5`).

**Reverse Engineering the Financial Goal Expression:**

```python
goal = balance > 0 and salary - expenses >= 0.2 * salary
```

Step-by-step evaluation order:
1. Arithmetic runs before comparisons: `0.2 * salary` and `salary - expenses` are computed first.
2. Relational operators evaluate next: `balance > 0` becomes a `bool`, and `salary - expenses >= 0.2 * salary` becomes a `bool`.
3. `and` evaluates last: `goal` is `True` only if **both** the balance is positive *and* remaining income is at least 20% of salary.

### Membership (`in`, `not in`) and Relational (`>`, `>=`, `<`, `<=`, `==`, `!=`)

- **Membership:** `'py' in 'python'` -> `True`; `'java' not in ['python', 'c']` -> `True`.
- **Relational:** compare values and always return `bool` (`True` or `False`).

### Identity (`is`, `is not`) vs. Equality (`==`)

Consider the book's `rent` and `utilities` (`aluguel` / `energia`) comparison:

```python
rent = 1000
utilities = 1000
print(rent == utilities)  # True  (same value)
print(rent is utilities)  # Checks memory identity, NOT value!
```

> **Crucial Pedagogical Note:**  
> - `==` checks **value equality** ("do these two objects hold equal values?").  
> - `is` checks **object identity in memory** (`id(a) == id(b)` — "are these two names pointing to the *exact same* object in RAM?").  
> - CPython caches ("interns") small integers (`-5` to `256`) and certain compile-time constants within the same code block, which can make `is` appear to match `==` on small numbers or literals by coincidence — yet fail across dynamically created values (`int("1000") is int("1000")` -> `False`!).  
> - **Rule:** Always use `==` / `!=` to compare numbers, strings, or collections; reserve `is` / `is not` for `None` (e.g., `if result is None:`) or explicit identity checks!

> Practice with: [ch09_operators.py](examples/ch09_operators.py)

---

## Chapter 10 — Conditional Structures (`if`, `elif`, `else`, `match/case`)

### `if`, `elif`, and `else`

Conditionals let a program branch according to runtime state.

#### 1. The `go_to_the_market` Algorithm
Translating the book's everyday decision flow into Python:
- If an item is needed and budget allows (plus checking weather/umbrella), buy it; otherwise skip or choose an alternative.

#### 2. Grade Classification (`>= 9`, `>= 7`, `>= 5`, `else`)

```python
if grade >= 9:
    status = "Excellent (A)"
elif grade >= 7:
    status = "Good (B)"
elif grade >= 5:
    status = "Recovery (C)"
else:
    status = "Failed (F)"
```

**Line-by-Line Reverse Engineering:**
- Conditions are evaluated top-to-bottom; the **first** matching branch runs and the rest are skipped.
- That is why checking `>= 9` *before* `>= 7` and `>= 5` is mandatory — reversing the order would trap `9.5` inside `>= 5`!

### `and` / `or` Inside Conditionals & Nested Conditionals

- **Combined conditions:** `if age >= 18 and has_ticket:` requires both; `if is_student or age >= 60:` requires at least one.
- **Nested conditionals:** placing an `if` inside another `if` enables multi-stage checks (e.g., first verify `balance >= total`, and inside that block check `is_vip` for an extra discount).

### Simulating `switch/case` (and Python 3.10+ `match/case`)

Before Python 3.10, Python had no `switch` statement. The book teaches clean equivalents:
1. **`class Color` constants + `if / elif / else`:**
   ```python
   class Color:
       RED = 1
       GREEN = 2
       BLUE = 3
   ```
2. **Dictionary dispatch (`dict.get`):** maps option keys directly to values or functions in `O(1)` lookup.
3. **Modern Python 3.10+ (`match` / `case`):** structural pattern matching added natively in Python 3.10!

> Practice with: [ch10_conditionals.py](examples/ch10_conditionals.py)

---

## Chapter 11 — Repetition Structures (`while`, `for`, `for...else`)

### `while` Loops, Increments, and `break`

A `while` loop repeats as long as its condition remains `True`. Always update the loop state (e.g., `counter += 1`) or provide a `break` exit to avoid infinite loops:

```python
counter = 1
while counter <= 5:
    if counter == 4:
        break
    print(counter)
    counter += 1
```

### `for` Loops, `range()`, `for...else`, and Nested Loops

- **Iterating lists:** `for item in groceries:` visits each element in `groceries` directly without manual indexing.
- **`range()`:** `range(0, 6)` and `range(6)` both yield integers `0, 1, 2, 3, 4, 5` (start inclusive, stop exclusive).
- **`for ... else`:** the `else` block runs **only if the loop finished normally without hitting `break`** — ideal for search loops ("not found").
- **Nested `for` multiplication table (`0x0` through `10x10`):**

```python
for factor_a in range(11):
    for factor_b in range(11):
        print(f"{factor_a} x {factor_b} = {factor_a * factor_b}")
```

**Reverse Engineering:**
- The outer loop picks `factor_a` (`0..10`). For *each* value of `factor_a`, the inner loop runs all 11 iterations of `factor_b` (`0..10`), producing `11 * 11 = 121` total products from `0 x 0 = 0` to `10 x 10 = 100`.

> Practice with: [ch11_loops.py](examples/ch11_loops.py)

---

## Chapter 12 — Strings, ANSI Colors, Alignment, and Numeric Formatting

### Single vs. Double Quotes and Multiline Strings

Python allows mixing quote styles cleanly without backslash clutter:
- Double outer quotes allow single apostrophes inside: `"Bob's watermark"` or `"It's water's edge"`.
- Single outer quotes allow double quotes inside: `'It was a "veeeery" cold day'`.
- Triple quotes (`"""..."""`) preserve multiple lines.

### `.lower()`, `.upper()`, and String Immutability

Strings in Python are **immutable**: calling `text.upper()` returns a **new** uppercase string and leaves `text` untouched unless you **permanently reassign** `text = text.upper()`.

### Searching (`in`) and Splitting (`.split()`)

- Case-insensitive search: `'python' in sentence.lower()`.
- `.split()` divides a string on whitespace by default, or on a specific delimiter like `.split(',')`.

### ANSI Terminal Colors

ANSI escape sequences style terminal output (`\033[<code_here>m ... \033[0m`). Always terminate colored text with the reset sequence `\033[0m` so color doesn't bleed into later terminal lines!

| Foreground Code | Color | Background Code | Color | Style Code | Effect |
| :-: | :--- | :-: | :--- | :-: | :--- |
| `30` / `90` | Black / Bright Black | `40` / `100` | Black / Bright Black | `0` | Reset / Normal |
| `31` / `91` | Red / Bright Red | `41` / `101` | Red / Bright Red | `1` | Bold |
| `32` / `92` | Green / Bright Green | `42` / `102` | Green / Bright Green | `4` | Underline |
| `33` / `93` | Yellow / Bright Yellow | `43` / `103` | Yellow / Bright Yellow | `7` | Reverse video |
| `34` / `94` | Blue / Bright Blue | `44` / `104` | Blue / Bright Blue | — | — |
| `35` / `95` | Magenta / Bright Magenta | `45` / `105` | Magenta / Bright Magenta | — | — |
| `36` / `96` | Cyan / Bright Cyan | `46` / `106` | Cyan / Bright Cyan | — | — |
| `37` / `97` | White / Bright White | `47` / `107` | White / Bright White | — | — |

### Display Alignment (`.center()`, `.ljust()`, `.rjust()`)

- `title.center(30, '=')` centers the text inside a 30-character width padded with `=`.
- `label.ljust(20, '.')` pads on the right (left-aligned text).
- `price.rjust(10)` pads on the left (right-aligned numbers).

### Formatting Numbers Inside Strings

Compare classic `%` precision formatting with modern f-strings using `from math import pi`:

```python
from math import pi

legacy_2 = "Pi (2 decimals): %.2f" % pi
legacy_5 = "Pi (5 decimals): %.5f" % pi
modern_2 = f"Pi (2 decimals): {pi:.2f}"
modern_5 = f"Pi (5 decimals): {pi:.5f}"
```

> Practice with: [ch12_strings_ansi.py](examples/ch12_strings_ansi.py)

---

## Example Scripts Map

Every script below can be executed directly with `python <path>` and safely imported without blocking on `input()`:

1. [ch09_operators.py](examples/ch09_operators.py) — Assignment, compound assignment, arithmetic precedence, truth tables, bitwise, financial goal, `in`, relational, and `is` vs. `==`.
2. [ch10_conditionals.py](examples/ch10_conditionals.py) — `if/elif/else`, `go_to_the_market`, grade classification, `and`/`or`, nested conditionals, `switch/case` via `class Color`, `dict`, and `match/case`.
3. [ch11_loops.py](examples/ch11_loops.py) — `while` + `break`, `for` with `groceries`, `range(0, 6)` vs `range(6)`, `for...else`, and nested `0x0`–`10x10` multiplication table.
4. [ch12_strings_ansi.py](examples/ch12_strings_ansi.py) — Quote styles, immutability with `.lower()`/`.upper()`, `in`, `.split()`, ANSI table, alignment methods, and `pi` formatting (`%.2f`, `%.5f`, `f'{pi:.2f}'`).

Continue to [Module 2 Exercises](exercises.md), review [Solved Exercises](solutions/solved_exercises.py), or advance to [Module 3 — Data Structures & Functions](../module_03_data_structures_functions/README.md).
