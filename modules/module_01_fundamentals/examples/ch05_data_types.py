"""Chapter 5 — Core Data Types in Python.

Demonstrates int, float, bool, str, list, dict, tuple, and multiline strings.

Run:
    python modules/module_01_fundamentals/examples/ch05_data_types.py
"""


def create_type_samples() -> dict[str, object]:
    """Create one sample of each core type covered in Chapter 5."""
    integer_val = 42                         # int
    float_val = 1.89                         # float
    boolean_val = True                       # bool
    string_val = "Python from Zero to OOP"   # str
    multiline_str = """Line 1: multiline string
Line 2: preserves line breaks
Line 3: handy for formatted blocks."""
    list_val = [1, "Python", 3.14, True]                # list (mutable)
    dict_val = {"name": "Maria", "age": 32}             # dict (key: value)
    tuple_val = (10, 20, 30)                            # tuple (immutable)

    return {
        "int": integer_val,
        "float": float_val,
        "bool": boolean_val,
        "str": string_val,
        "str_multiline": multiline_str,
        "list": list_val,
        "dict": dict_val,
        "tuple": tuple_val,
    }


def main() -> None:
    print("=== Chapter 5: Core Data Types ===\n")
    samples = create_type_samples()

    for label, value in samples.items():
        print(f"[{label}] type={type(value).__name__} -> value={value!r}")


if __name__ == "__main__":
    main()
