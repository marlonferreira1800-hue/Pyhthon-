# Module 3 — Data Structures, Interpolation, and Functions

**Book chapters covered:** Chapters 13, 14, 15, 16, and 17 (*Python from Zero to Object-Oriented Programming*, updated and expanded edition, by Fernando Feltrin).

In this module, you move beyond single-value variables to organizing **entire collections of data** (lists, tuples, stacks, dictionaries, and sets), formatting text cleanly with **string interpolation**, and packaging reusable logic into well-structured **functions**.

Following the book's **"Reverse Engineering" methodology**, each section shows the complete working code first and then dissects how Python executes it line by line.

---

## Table of Contents

1. [Chapter 13 — Lists, Tuples, and Stacks](#chapter-13--lists-tuples-and-stacks)
2. [Chapter 14 — Dictionaries (`dict`)](#chapter-14--dictionaries-dict)
3. [Chapter 15 — Numeric Sets (`set`)](#chapter-15--numeric-sets-set)
4. [Chapter 16 — String Interpolation](#chapter-16--string-interpolation)
5. [Chapter 17 — Functions (`def`)](#chapter-17--functions-def)
6. [Quick Comparison Table](#quick-comparison-table)
7. [How to Run Examples and Exercises](#how-to-run-examples-and-exercises)

---

## Chapter 13 — Lists, Tuples, and Stacks

### 1.1 Lists (`[ ]`): ordered, mutable collections

```python
items = [1, 2, 4, "Paul", [2, 5, "Ana"]]
items.append("New item")
items.remove(2)
del items[0]
paul_index = items.index("Paul")
has_paul = "Paul" in items
items.reverse()
```

#### Reverse Engineering — Line by Line

- **Line 1 (`[1, 2, 4, "Paul", [2, 5, "Ana"]]`)**: square brackets `[ ]` create a `list`. Python lists support **mixed data types** (integers, strings, booleans, and even nested lists).
- **0-based indexing**: the first element is at index `0` (`items[0] == 1`). The fifth element (`items[4]`) is the nested sublist `[2, 5, "Ana"]`. To reach `"Ana"`, chain the indices: `items[4][2]`. Negative indices count from the end (`items[-1]` is the last element).
- **Line 2 (`.append("New item")`)**: appends one element to the **end** of the list in-place.
- **Line 3 (`.remove(2)`)**: finds and removes the **first occurrence of value `2`**. If the value is missing, Python raises `ValueError`.
- **Line 4 (`del items[0]`)**: deletes an element by **index position**, rather than by value.
- **Line 5 (`.index("Paul")`)**: returns the zero-based index of `"Paul"`'s first occurrence.
- **Line 6 (`"Paul" in items`)**: membership operator returning `True` or `False` so you can check before removing or indexing.
- **Line 7 (`.reverse()`)**: reverses the list **in-place** and returns `None`. Never write `new_list = items.reverse()`, or `new_list` will be `None`!

#### In-Place Mutability vs. String Immutability

In Python, a `str` is **immutable**: attempting `word = "home"; word[0] = "H"` raises `TypeError`. Methods like `word.upper()` return a brand-new string without changing the original. By contrast, a `list` is **mutable**: `items[0] = 99`, `.append()`, `.remove()`, and `.reverse()` mutate the same list object in memory.

---

### 1.2 Tuples (`( )` and `tuple()`): ordered, immutable collections

```python
colors_tuple = ("blue", "green", "yellow", "blue", "red")
single_item_tuple = (1,)
not_a_tuple = (1)
letters = tuple("Ana")

blue_count = colors_tuple.count("blue")   # 2
green_index = colors_tuple.index("green") # 1
```

#### Reverse Engineering — Line by Line

- **Line 1 (`colors_tuple = (...)`)**: parentheses create a `tuple`. Like lists, tuples preserve insertion order and support indexing (`colors_tuple[0] == "blue"`). Unlike lists, **tuples are immutable**: they have no `.append()`, `.remove()`, or `.reverse()`, and item assignment raises `TypeError`.
- **Line 2 vs. Line 3 (`(1,)` vs. `(1)`)**: the **trailing comma** is what builds a 1-element tuple! Without the comma, `(1)` is simply the integer `1` wrapped in grouping parentheses (`type((1)) is int`, whereas `type((1,)) is tuple`).
- **Line 4 (`tuple("Ana")`)**: the `tuple()` constructor iterates over any iterable passed to it. Because a string is an iterable sequence of characters, `tuple("Ana")` produces `('A', 'n', 'a')` — not `('Ana',)`!
- **Lines 6–7 (`.count()` and `.index()`)**: because tuples cannot be modified, their two main public methods are `.count(value)` and `.index(value)`.

> **Gentle Pedagogical Note on the Book:**  
> In an introductory comparison, the book remarks that lists do not repeat values. In Python, **lists do allow duplicate elements** (for example, `[10, 10, 20]`), just like tuples (`("blue", "blue")`). The collection type that automatically forbids duplicates is a **set** (`set`, covered in Chapter 15). The true core distinction between `list` and `tuple` is **mutability**: lists are mutable, while tuples are immutable.

---

### 1.3 Stacks (LIFO)

```python
paper_stack = []
paper_stack.append("Invoice #1")
paper_stack.append("Signed Contract")
paper_stack.append("Urgent Memo")

stack_size = len(paper_stack)      # 3
top_item = paper_stack.pop()       # "Urgent Memo"
```

#### Reverse Engineering — Line by Line

- **LIFO (*Last In, First Out*)**: just like a **stack of papers** on a desk, you place new sheets onto the **top** and always take the top sheet off first.
- **`.append(item)`**: pushes a new item onto the top of the stack.
- **`len(paper_stack)`**: inspects how many items are currently on the stack.
- **`.pop()`**: removes and **returns** the top (last) element. Calling `.pop()` on an empty list raises `IndexError`, so always guard with `if paper_stack:` first.

---

## Chapter 14 — Dictionaries (`dict`)

```python
person = {
    "name": "Fernando",
    "age": 43,
    "profession": "Software Developer",
    "education": ["Systems Analysis", "Python"],
}

field_count = len(person)
phone = person.get("phone", "Not provided")
keys = list(person.keys())
values = list(person.values())
entries = list(person.items())

person["age"] = 44
person["education"].append("Data Science")
person["city"] = "Curitiba"
```

#### Reverse Engineering — Line by Line

- **`{key: value}` mapping**: instead of numeric indices (`0, 1, 2`), dictionaries map unique keys to values of any complexity — including nested lists like `"education"`.
- **Line breaks after commas**: placing one `key: value` pair per line keeps multi-field dictionaries clean and readable.
- **`len(person)`**: returns the number of `key: value` pairs (`4` initially).
- **`.get("phone", "Not provided")`**: safe lookup. Reading `person["phone"]` directly raises `KeyError` when the key is missing; `.get()` returns `None` or the fallback value instead.
- **`.keys()`, `.values()`, `.items()`**: return dynamic dictionary views of all keys, values, and `(key, value)` pairs.
- **`person["age"] = 44`**: updates an existing key in-place.
- **`person["education"].append("Data Science")`**: retrieves the inner list and appends to it directly.
- **`person["city"] = "Curitiba"`**: when the key does not exist yet, assignment creates a new entry.

---

## Chapter 15 — Numeric Sets (`set`)

```python
a = {1, 2, 3}
s1 = {1, 2, 3, 4, 5}
s2 = {2, 3}

union_set = a.union({3, 4, 5})             # {1, 2, 3, 4, 5}
intersection_set = s1.intersection({3, 4, 9}) # {3, 4}
is_subset = s2 <= s1                       # True
difference_set = {1, 2, 3} - {2}           # {1, 3}

a.update({4, 5})                           # updates 'a' in-place -> {1, 2, 3, 4, 5}
```

#### Reverse Engineering — Line by Line

- **Creating sets (`{1, 2, 3}` vs. `{}`)**: curly braces with comma-separated values create a `set`. Watch out: empty `{}` creates an empty **`dict`**, so always use `set()` for an empty set.
- **Unindexed and duplicate-free**: `{1, 2, 2, 3}` automatically collapses to `{1, 2, 3}`. Sets have no positional index (`a[0]` raises `TypeError`).
- **`.union()` (or `|`)**: combines all unique elements from both sets.
- **`.intersection()` (or `&`)**: keeps only elements present in both sets.
- **`.update()`**: adds elements from another iterable/set in-place without duplicates.
- **`s2 <= s1`**: checks whether `s2` is a **subset** of `s1` (`True` if every item in `s2` is also in `s1`).
- **`{1, 2, 3} - {2}`**: **difference** operator — elements in the left set that are not in the right set (`{1, 3}`).

---

## Chapter 16 — String Interpolation

Python evolved through three generations of string formatting:

```python
name = "Maria"
age = 20

# 1. Classic %-formatting (%s for string, %d for integer)
msg_percent = "Student: %s | Age: %d years" % (name, age)

# 2. str.format() with empty {} and positional indices {0}, {1}
msg_format_auto = "Student: {} | Age: {} years".format(name, age)
msg_format_idx = "{0}'s age is {1} (3x age for {0}: {2})".format(name, age, 3 * age)

# 3. f-strings (Python 3.6+): clean, fast, and supports inline expressions!
msg_fstring = f"Student: {name} | Age: {age} | Triple age: {3 * age}"
```

#### Reverse Engineering — Line by Line

1. **`%s` / `%d`**: borrowed from C's `printf`. Requires matching format specifiers (`%s`, `%d`, `%f`) and passing a tuple for multiple values.
2. **`.format()`**: uses `{}` placeholders; positional indices `{0}`, `{1}` allow reordering or reusing arguments.
3. **`f-strings` (`f"..."`)**: modern Python standard. Evaluates variables and **arbitrary expressions** directly inside braces — such as `{3 * age}` — at runtime.

---

## Chapter 17 — Functions (`def`)

Functions come from three sources:
- **Predefined (built-in)**: available automatically (`print()`, `len()`, `sum()`, `type()`).
- **Imported**: loaded from standard or third-party modules (`math.sqrt()`).
- **Custom (`def`)**: defined by you to structure reusable behavior.

### 5.1 Parameterless Function (`None`) vs. Parameterized Function with `return`

```python
def welcome():
    print("Welcome to the Python course!")


def cube_number(number):
    return number ** 3


returned_value = welcome()     # Prints message and evaluates to None
cubed = cube_number(4)         # 64
```

#### Reverse Engineering — Line by Line

- **Why does `print(welcome())` output `None`?**  
  `welcome()` prints text as a side effect, but contains no `return` statement. In Python, any function without an explicit `return` automatically returns **`None`**. When you run `print(welcome())`, Python executes `welcome()` first (printing the greeting), receives `None`, and then the outer `print(...)` prints `None` on the next line!
- **`cube_number(number)`**: accepts an argument and uses **`return`** to pass `number ** 3` back to the caller so the result can be stored, reused, or tested.

### 5.2 `*args` and `**kwargs`

```python
def sum_all(*args):
    # *args packs variable positional arguments into a TUPLE
    return sum(args), type(args)


def user_info(**kwargs):
    # **kwargs packs variable keyword arguments into a DICT
    return kwargs
```

#### Reverse Engineering — Line by Line

- **`*args`**: a single asterisk packs any number of positional arguments into a tuple named `args`.
  > **Technical Clarification:** Although the book refers to a list in one sentence when introducing `*args`, Python **always passes `*args` as an immutable `tuple`** (`type(args) is tuple`).
- **`**kwargs`**: a double asterisk packs any number of keyword arguments (`key=value`) into a **`dict`**. Calling `user_info(name="Ana", track="Backend")` gives `kwargs == {"name": "Ana", "track": "Backend"}`.

---

## Quick Comparison Table

| Structure | Syntax | Ordered? | Mutable? | Duplicates allowed? | Primary Access |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **List** (`list`) | `[1, 2, 3]` | Yes | Yes | Yes | Numeric index `items[0]` |
| **Tuple** (`tuple`) | `(1, 2, 3)` / `(1,)` | Yes | **No** | Yes | Numeric index `items[0]` |
| **Stack** (`list` LIFO) | `.append()` / `.pop()` | Yes | Yes | Yes | Top of stack (`[-1]`) |
| **Dictionary** (`dict`) | `{"k": "v"}` | Yes (insertion) | Yes | Keys **no** / Values yes | Key `d["k"]` or `d.get("k")` |
| **Set** (`set`) | `{1, 2, 3}` / `set()` | **No** | Yes | **No** | Membership `in` and set ops |

---

## How to Run Examples and Exercises

From the repository root:

```bash
python modules/module_03_data_structures_functions/examples/ch13_lists_tuples_stacks.py
python modules/module_03_data_structures_functions/examples/ch14_dictionaries.py
python modules/module_03_data_structures_functions/examples/ch15_sets.py
python modules/module_03_data_structures_functions/examples/ch16_string_interpolation.py
python modules/module_03_data_structures_functions/examples/ch17_functions.py
python modules/module_03_data_structures_functions/solutions/solved_exercises.py
```

Work through [exercises.md](exercises.md) first, then compare your answers with [solutions/solved_exercises.py](solutions/solved_exercises.py).
