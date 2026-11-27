# Exercises — Module 1 (Fundamentals, Logic, and First Commands)

Solve the progressive exercises below covering Chapters 1 to 8.  
Compare your implementation against [solutions/solved_exercises.py](solutions/solved_exercises.py) and review the lesson in [README.md](README.md).

---

## Basic Level

### Exercise 1 — Hello World & The Zen of Python (Chs. 1 & 4)
Write `ex01_hello_zen(index: int) -> dict[str, str]` that:
1. Accepts an integer `index` from `1` to `19`.
2. Validates the range (raising `ValueError` if outside `1..19` or if given a `bool`).
3. Returns `{"greeting": "Hello World!!!", "principle": <Zen of Python principle>}`.

### Exercise 2 — Syntax vs. Logic (`'5' + '2'` vs. `5 + 2`) (Ch. 3)
Write `ex02_compare_concat_and_sum(text_a: str, text_b: str) -> dict[str, object]` that:
1. Shows what string concatenation yields (`text_a + text_b`, e.g., `'5' + '2' -> '52'`).
2. Casts both inputs to `int` and computes the true arithmetic sum (`5 + 2 -> 7`).
3. Returns `{"concatenation": ..., "integer_sum": ...}`.

### Exercise 3 — Variable Name & Keyword Classifier (Chs. 3 & 7)
Write `ex03_classify_identifier(name: str) -> str` that classifies a candidate Python variable name into one of four exact categories:
- `"forbidden_keyword"`: if `name` is in `keyword.kwlist`.
- `"forbidden_syntax"`: if `not name.isidentifier()`.
- `"valid_discouraged"`: if syntactically valid, yet contains non-ASCII characters (like accents) or uppercase letters.
- `"valid_recommended"`: ASCII identifier without uppercase letters (PEP 8 `snake_case`).

---

## Intermediate Level

### Exercise 4 — Data Types & `{5}` vs. `{k: v}` Anatomy (Chs. 5 & 8)
Write `ex04_inspect_collections(number: int) -> dict[str, object]` that creates:
- a single-element set `{number}`,
- an empty dict `{}`,
- a populated dict `{"value": number}`,
- a list `[number]`,
- a single-element tuple `(number,)`,
and returns `{"values": ..., "types": ...}` mapping each key to its `type(...).__name__`.

### Exercise 5 — Multiple Assignment, Chained Assignment & Case Sensitivity (Ch. 7)
Write `ex05_multiple_registration(name: str, age: int, gender: str, height: float) -> dict[str, object]` that:
1. Uses single-line multiple assignment to unpack the 4 fields.
2. Uses chained assignment `s1 = s2 = s3 = 10` for three identical starting scores.
3. Proves `NAME = name.upper()` differs from `name` when lowercase letters exist, returning `{"summary": ..., "scores": (s1, s2, s3), "case_differs": bool}`.

### Exercise 6 — Overdue Invoice (`\n`) & 3 Formatting Styles (Ch. 8)
Write `ex06_generate_invoice_and_formats(customer: str, amount: float, due_date: str) -> dict[str, str]` that:
1. Builds a multiline invoice string using `\n` with the customer name, amount formatted to 2 decimal places (`$...`), and due date.
2. Produces a summary line in all three historical styles (`"percent"` with `%`, `"format"` with `.format()`, and `"fstring"` with an `f-string`).
3. Returns `{"invoice": ..., "percent": ..., "format": ..., "fstring": ...}`.

---

## Challenge Level

### Exercise 7 — Positive/Negative Check & `int + float` Coercion (Chs. 3 & 8)
Write `ex07_evaluate_positive_and_mixed_sum(input_str: str, decimal_addend: float) -> dict[str, object]` that:
1. Converts `input_str` via `int(input_str)` (allowing `ValueError` if invalid).
2. Classifies it as `"positive"` when `>= 0`, else `"negative"`.
3. Computes `total = integer_val + float(decimal_addend)` and returns `{"number": integer_val, "classification": ..., "sum": total, "sum_type": type(total).__name__}`.

### Exercise 8 — Lexical Analysis & Safe `str + str(age)` Concatenation (Chs. 3, 6 & 8)
Write `ex08_compliment_and_age(adjective: str, repetitions: int, age: int) -> dict[str, str]` that:
1. Validates `repetitions >= 1` (raising `ValueError` otherwise).
2. Applies string multiplication precedence: `'You are ' + repetitions * (adjective + ' ') + 'cool!'`.
3. Builds `'Recorded age: ' + str(age)` via explicit `str(age)` conversion (avoiding `TypeError`).
4. Returns `{"compliment": ..., "age_record": ...}`.
