# Exercises — Module 3: Data Structures, Interpolation, and Functions

These **8 progressive exercises** reinforce Chapters 13 through 17 of the book. Solve each problem yourself before checking [solutions/solved_exercises.py](solutions/solved_exercises.py).

---

## Basic Level

### Exercise 1 — List Operations and Nested Indexing (Ch. 13)
Implement `manipulate_list(items, to_add, to_remove)` that:
1. Makes a shallow copy of `items` so the caller's list is not mutated.
2. Appends `to_add` using `.append()`.
3. Checks `if to_remove in new_list:` and removes the first occurrence via `.remove()`.
4. Finds the index of `to_add` with `.index()`.
5. Builds a reversed copy using `.reverse()`.
6. Extracts `"Ana"` from the nested list `[1, 2, 4, "Paul", [2, 5, "Ana"]]` using chained indices.
7. Returns a dictionary with keys `"list"`, `"added_index"`, `"reversed"`, and `"nested_name"`.

### Exercise 2 — Tuples, Single-Element Comma, and Color Analysis (Ch. 13)
Implement `analyze_colors_tuple(colors, target_color)` that:
1. Counts how many times `target_color` appears using `.count()`.
2. Finds the first index of `target_color` using `.index()` (returning `-1` if absent).
3. Creates a 1-element tuple containing `target_color` (`(target_color,)`).
4. Demonstrates `tuple(target_color)` (which splits the string into single characters).
5. Returns `{"count", "first_index", "single_tuple", "characters"}`.

### Exercise 3 — Evolution of String Interpolation (Ch. 16)
Implement `format_profile_interpolation(name, age)` returning a dictionary with the exact same information formatted in all three Python interpolation styles:
- `"percent"`: `"Name: <name> | Age: <age> | Triple: <3*age>"` using `%s` and `%d`.
- `"format"`: the same string using `.format()` with indices `{0}`, `{1}`, `{2}`.
- `"fstring"`: the same string using an `f-string` and inline expression `{3 * age}`.

---

## Intermediate Level

### Exercise 4 — LIFO Document Stack Simulator (Ch. 13)
Implement `simulate_paper_stack(actions)` accepting a list of `(operation, document)` tuples such as `[("push", "Contract"), ("pop", "")]`, using `.append()`, `.pop()`, and `len()`:
- On `"push"`, push `document` onto the top of the stack.
- On `"pop"`, pop from the top if the stack is non-empty and append it to `popped_items`.
- Return `{"remaining_stack", "popped_items", "size", "top"}` (with `"top"` set to `None` when empty).

### Exercise 5 — Complex Profile Dictionary (Ch. 14)
Implement `update_person_profile(person, new_age, new_course, city)` that:
1. Makes a safe copy of `person` (including copying its inner `"education"` list).
2. Updates `profile["age"] = new_age`.
3. Appends `new_course` to `profile["education"]` with `.append()`.
4. Adds the new key `profile["city"] = city`.
5. Reads `"phone"` safely via `.get("phone", "Not provided")`.
6. Returns `{"profile", "phone", "total_keys", "keys", "values", "items"}`.

### Exercise 6 — Numeric Set Operations (Ch. 15)
Implement `analyze_sets(s1, s2)` receiving two `set` objects and returning:
- `"union"`: `s1.union(s2)`
- `"intersection"`: `s1.intersection(s2)`
- `"difference_s1_s2"`: `s1 - s2`
- `"s2_is_subset_of_s1"`: boolean result of `s2 <= s1`
- `"s1_updated"`: copy of `s1` after calling `.update(s2)`

---

## Challenge Level

### Exercise 7 — Functions, Return Values, `*args` (Tuple), and `**kwargs` (Dict) (Ch. 17)
Implement three functions:
1. `cube_number(number)`: returns `number ** 3`.
2. `sum_variadic_args(*args)`: returns `{"args_type": type(args).__name__, "count": len(args), "sum": sum(args)}`, proving `*args` is always `"tuple"`.
3. `build_profile(name, *skills, **details)`: returns `{"name": name, "skills": skills, "skills_type": type(skills).__name__, "details": dict(details)}`.

### Exercise 8 — Integrative Challenge: Class Cohort Report (Ch. 13–17)
Implement `generate_cohort_report(students, *required_subjects, **config)`:
- Each entry in `students` is a dict `{"name": str, "grades": list[float], "subjects": set[str]}`.
- Using `config.get("passing_grade", 7.0)` and `config.get("title", "Cohort Report")`:
  - Compute each student's average grade (`0.0` if `grades` is empty).
  - Check subset completion with `set(required_subjects) <= student["subjects"]`.
  - Push passing students onto a LIFO stack (`.append()`) and generate formatted report lines with `f-strings`.
  - Return `{"title", "approved", "lines", "last_approved", "total_approved"}`.
