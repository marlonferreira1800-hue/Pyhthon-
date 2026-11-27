"""Solved exercises for Module 1 (Chapters 1 to 8).

All functions are pure and testable (no blocking `input()` calls).

Run directly:
    python modules/module_01_fundamentals/solutions/solved_exercises.py
"""

import keyword

ZEN_OF_PYTHON: tuple[str, ...] = (
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
)


def ex01_hello_zen(index: int) -> dict[str, str]:
    """Return 'Hello World!!!' and the 1-based Zen of Python principle (1..19)."""
    if not isinstance(index, int) or isinstance(index, bool) or not 1 <= index <= 19:
        raise ValueError("Zen of Python index must be an integer between 1 and 19.")
    return {
        "greeting": "Hello World!!!",
        "principle": ZEN_OF_PYTHON[index - 1],
    }


def ex02_compare_concat_and_sum(text_a: str, text_b: str) -> dict[str, object]:
    """Contrast string concatenation logic error with true integer addition."""
    concatenation = str(text_a) + str(text_b)
    integer_sum = int(text_a) + int(text_b)
    return {
        "concatenation": concatenation,
        "integer_sum": integer_sum,
    }


def ex03_classify_identifier(name: str) -> str:
    """Classify a variable name candidate against keywords, syntax, and PEP 8."""
    if name in keyword.kwlist:
        return "forbidden_keyword"
    if not name.isidentifier():
        return "forbidden_syntax"
    if not name.isascii() or any(ch.isupper() for ch in name):
        return "valid_discouraged"
    return "valid_recommended"


def ex04_inspect_collections(number: int) -> dict[str, object]:
    """Inspect `{number}` (set), `{}` (dict), `{k: v}`, `[n]`, and `(n,)`."""
    single_set = {number}
    empty_dict: dict[str, int] = {}
    populated_dict = {"value": number}
    single_list = [number]
    single_tuple = (number,)

    values = {
        "set": single_set,
        "empty_dict": empty_dict,
        "populated_dict": populated_dict,
        "list": single_list,
        "tuple": single_tuple,
    }
    types = {key: type(obj).__name__ for key, obj in values.items()}
    return {"values": values, "types": types}


def ex05_multiple_registration(
    name: str,
    age: int,
    gender: str,
    height: float,
) -> dict[str, object]:
    """Practice multiple assignment, chained assignment, and case sensitivity."""
    user_name, user_age, user_gender, user_height = name, age, gender, height
    s1 = s2 = s3 = 10
    NAME = user_name.upper()

    return {
        "summary": (
            f"{user_name} | {user_age} yrs | "
            f"gender={user_gender} | height={user_height:.2f}m"
        ),
        "scores": (s1, s2, s3),
        "case_differs": NAME != user_name,
    }


def ex06_generate_invoice_and_formats(
    customer: str,
    amount: float,
    due_date: str,
) -> dict[str, str]:
    """Build an invoice using `\\n` and compare %, .format(), and f-strings."""
    invoice = (
        f"Customer: {customer}\n"
        f"Amount: ${amount:.2f}\n"
        f"Due Date: {due_date}"
    )
    percent = "Customer: %s | Amount: $%.2f | Due Date: %s" % (customer, amount, due_date)
    fmt = "Customer: {} | Amount: ${:.2f} | Due Date: {}".format(customer, amount, due_date)
    fstring = f"Customer: {customer} | Amount: ${amount:.2f} | Due Date: {due_date}"
    return {
        "invoice": invoice,
        "percent": percent,
        "format": fmt,
        "fstring": fstring,
    }


def ex07_evaluate_positive_and_mixed_sum(
    input_str: str,
    decimal_addend: float,
) -> dict[str, object]:
    """Cast str->int, classify positive/negative, and verify int + float -> float."""
    integer_val = int(input_str)
    classification = "positive" if integer_val >= 0 else "negative"
    total = integer_val + float(decimal_addend)
    return {
        "number": integer_val,
        "classification": classification,
        "sum": total,
        "sum_type": type(total).__name__,
    }


def ex08_compliment_and_age(adjective: str, repetitions: int, age: int) -> dict[str, str]:
    """Demonstrate string multiplication precedence and explicit str(age) casting."""
    if repetitions < 1:
        raise ValueError("`repetitions` must be at least 1.")
    compliment = "You are " + repetitions * (adjective + " ") + "cool!"
    age_record = "Recorded age: " + str(age)
    return {
        "compliment": compliment,
        "age_record": age_record,
    }


def main() -> None:
    print("=== Module 1 Solved Exercises ===")
    print("Ex 01:", ex01_hello_zen(2))
    print("Ex 02:", ex02_compare_concat_and_sum("5", "2"))
    print("Ex 03:", ex03_classify_identifier("student_name"))
    print("Ex 04:", ex04_inspect_collections(5)["types"])
    print("Ex 05:", ex05_multiple_registration("Maria", 32, "F", 1.89))
    print("Ex 06:\n" + ex06_generate_invoice_and_formats("Maria", 250.0, "05/10")["invoice"])
    print("Ex 07:", ex07_evaluate_positive_and_mixed_sum("10", 2.5))
    print("Ex 08:", ex08_compliment_and_age("very", 3, 15))


if __name__ == "__main__":
    main()
