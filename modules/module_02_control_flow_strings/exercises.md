# Exercises — Module 2 (Operators, Control Flow, and Strings)

Solve the progressive exercises below covering Chapters 9 to 12.  
Compare your implementation against [solutions/solved_exercises.py](solutions/solved_exercises.py) and review the lesson in [README.md](README.md).

---

## Basic Level

### Exercise 1 — Compound Assignment & Financial Goal (Ch. 9)
Write `ex01_financial_goal_and_compound(initial_balance: float, deposit: float, salary: float, expenses: float) -> dict[str, object]` that:
1. Updates `balance` starting from `initial_balance` using `+= deposit`.
2. Evaluates `goal = balance > 0 and salary - expenses >= 0.2 * salary`.
3. Returns `{"updated_balance": balance, "savings_margin": round(salary - expenses, 2), "goal_met": goal}`.

### Exercise 2 — Truth Tables & Bitwise Operators (Ch. 9)
Write `ex02_truth_and_bitwise_summary(a: bool, b: bool, int_x: int, int_y: int) -> dict[str, object]` that returns:
- `"logical"`: `{"and": a and b, "or": a or b, "xor": a ^ b, "not_a": not a}`
- `"bitwise"`: `{"and": int_x & int_y, "or": int_x | int_y, "xor": int_x ^ int_y}`

### Exercise 3 — Identity (`is`) vs. Value Equality (`==`) (Ch. 9)
Write `ex03_compare_identity_and_equality(rent_value: int, utilities_value: int) -> dict[str, object]` that:
1. Compares `rent_value == utilities_value`.
2. Creates an alias `alias = rent_value` and checks `rent_value is alias`.
3. Creates two distinct runtime integers `int(str(rent_value))` and `int(str(utilities_value))` (e.g. `1000`) and reports `==` vs `is` to prove why `==` must be used for value comparisons.

---

## Intermediate Level

### Exercise 4 — Grade Classification & Market Budget Check (Ch. 10)
Write `ex04_classify_grade_and_market(grade: float, budget: float, price: float) -> dict[str, str]` that:
1. Validates `0 <= grade <= 10` (raising `ValueError` otherwise).
2. Classifies `grade` using `if / elif / else`: `>= 9` (`"Excellent"`), `>= 7` (`"Good"`), `>= 5` (`"Recovery"`), else `"Failed"`.
3. Evaluates market affordability (`"Bought"` if `budget >= price` else `"Insufficient budget"`).

### Exercise 5 — Simulating `switch/case` Three Ways (Ch. 10)
Write `ex05_dispatch_color_switch(code: int) -> dict[str, str]` that maps `1 -> "Red"`, `2 -> "Green"`, `3 -> "Blue"`, and any other integer to `"Unknown"` using:
1. `if / elif / else` with `Color` constants,
2. a dictionary lookup,
3. Python 3.10+ `match / case`,
returning `{"if_elif": ..., "dict": ..., "match_case": ...}`.

### Exercise 6 — `while` + `break` & `for...else` Search (Ch. 11)
Write `ex06_while_break_and_for_search(items: list[str], target: str, limit: int, stop_at: int) -> dict[str, object]` that:
1. Uses a `while` loop with `+= 1` and `break` at `stop_at` to collect integers from `0` up to `limit` (exclusive).
2. Searches `target` in `items` with `for ... else` returning `"found"` or `"not_found"`.

---

## Challenge Level

### Exercise 7 — Complete Multiplication Table (`0x0` to `10x10`) (Ch. 11)
Write `ex07_multiplication_table(start: int = 0, end: int = 10) -> list[str]` that:
1. Validates `0 <= start <= end` (raising `ValueError` otherwise).
2. Uses nested `for` loops to return strings formatted as `"{a} x {b} = {a * b}"` for every pair `(a, b)` in `[start, end]`.

### Exercise 8 — String Pipeline, Immutability, ANSI, Alignment & `pi` Formatting (Ch. 12)
Write `ex08_string_pipeline_ansi(raw_csv: str, search_term: str, value: float) -> dict[str, object]` that:
1. Calls `.upper()` without reassigning `raw_csv` to verify `raw_csv` stays unchanged, then returns the split tokens from `raw_csv.split(",")`.
2. Checks case-insensitive membership of `search_term` via `in`.
3. Builds a centered header with `.center(30, "-")` and an ANSI-colored tag `f"\033[91m{search_term}\033[0m"`.
4. Formats `value` using `"%.2f" % value`, `"%.5f" % value`, and `f"{value:.2f}"`.
