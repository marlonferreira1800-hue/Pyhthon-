# Exercises — Module 4: Introspection, Builtins, Modules, Packages, and Exceptions

These **8 progressive exercises** reinforce Chapters 18, 19, 20, and 22 of the book. Solve each problem yourself before comparing with [solutions/solved_exercises.py](solutions/solved_exercises.py).

---

## Basic Level

### Exercise 1 — Object Introspection with `dir()` (Ch. 18)
Implement `inspect_attributes(obj)` using `dir(obj)` and returning a dict with:
- `"type"`: class name (`type(obj).__name__`)
- `"total"`: total number of attributes/methods
- `"public"`: list of names that do **not** start and end with `__`
- `"special"`: list of dunder identifiers (`__...__`)

### Exercise 2 — Builtins and Circle Area with `math.pi` (Ch. 19)
Implement `explore_builtins_and_area(radius)` that:
1. Inspects the `builtins` module (equivalent to `dir(__builtins__)` in REPL) and checks whether `"ValueError"`, `"TypeError"`, `"NameError"`, `"print"`, and `"__name__"` are present.
2. Validates `radius`: if `radius < 0`, raises `ValueError("Radius must be non-negative.")`.
3. Computes circle area using `from math import pi` (`pi * radius ** 2`).
4. Returns `{"area", "builtins_verified", "total_builtins"}`.

### Exercise 3 — Specific Exception Handling (Ch. 22)
Implement `safe_divide(numerator, denominator)` that converts both inputs to `float` and divides them, explicitly catching:
- `ValueError` (non-numeric string)
- `TypeError` (invalid type such as `None` or `list`)
- `ZeroDivisionError` (divisor equals zero)

Return `{"ok": True, "result": value, "error": None, "error_type": None}` on success, or `{"ok": False, "result": None, "error": message, "error_type": exception_name}` on failure.

---

## Intermediate Level

### Exercise 4 — Module Diagnostics, `__name__`, and `sys.path` (Ch. 20)
Implement `diagnose_modules_and_paths()` that:
1. Imports example modules `greetings` and `addition`.
2. Records `__name__` of the current module and the imported modules (showing imported modules do not have `__name__ == "__main__"`).
3. Inspects `sys.path`, reporting the path count and the first path entry.
4. Calls `greetings.greet("Student")` and `addition.add(7, 8)`.

### Exercise 5 — Subfolder Packages and Aliases (Ch. 20)
Implement `compute_price_table(prices, percentage)` importing `increase_price` from `sales.price_calc` **using an alias** (`from ...sales.price_calc import increase_price as apply_increase`).  
For each price in `prices`, return a dict `{"original_price", "percentage", "updated_price"}`.

### Exercise 6 — Correct `try` / `except` / `else` / `finally` Pattern (Ch. 22)
Based on the fix for page 213 of the book, implement `safe_sum_inputs(value1, value2)` where:
- `try` only converts `num1 = int(value1)` and `num2 = int(value2)`.
- `except` catches `ValueError` and `TypeError` separately, setting `error_type` and `error`.
- `else` computes `total = num1 + num2` only when no exception occurred.
- `finally` sets `"finalized": True` **without referencing `num1` or `num2`** (ensuring `NameError` can never happen).

---

## Challenge Level

### Exercise 7 — Batch Pair Division with Exception Audit (Ch. 18, 19, 22)
Implement `convert_and_divide_pairs(pairs)` accepting a list of `(a, b)` tuples, computing `int(a) / int(b)` per pair with `try` / `except` / `else` / `finally`, and returning:
- `"successes"`: list of valid float results
- `"failures"`: list of dicts `{"index", "input", "error_type", "message"}`
- `"finalized_attempts"`: total iterations counted inside `finally`

### Exercise 8 — Integrative Challenge: Sales Batch Processor with `sales` Package (Ch. 18, 19, 20, 22)
Implement `process_sales_batch(items, default_rate=10.0)` accepting a list of dicts (e.g., `[{"product": "Book", "price": "80.0", "markup": 15}]`):
1. Use `increase_price` imported from `sales.price_calc` via alias.
2. Convert `"price"` to `float` and `"markup"` (falling back to `default_rate` if missing).
3. Catch `KeyError`, `ValueError`, and `TypeError` per item so one bad record never aborts the batch.
4. Sum updated prices accurately using `math.fsum` and return `{"processed", "errors", "total_updated", "audit_completed"}`.
