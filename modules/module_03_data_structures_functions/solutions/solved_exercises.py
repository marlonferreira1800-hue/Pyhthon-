"""Testable solutions for all 8 exercises in Module 3 (Chapters 13 to 17)."""

from typing import Any


def manipulate_list(items: list[Any], to_add: Any, to_remove: Any) -> dict[str, Any]:
    """Exercise 1: list manipulation and nested list indexing."""
    updated = list(items)
    updated.append(to_add)
    if to_remove in updated:
        updated.remove(to_remove)

    added_index = updated.index(to_add)
    reversed_copy = list(updated)
    reversed_copy.reverse()

    nested_example = [1, 2, 4, "Paul", [2, 5, "Ana"]]
    nested_name = nested_example[4][2]

    return {
        "list": updated,
        "added_index": added_index,
        "reversed": reversed_copy,
        "nested_name": nested_name,
    }


def analyze_colors_tuple(colors: tuple[str, ...], target_color: str) -> dict[str, Any]:
    """Exercise 2: tuple methods, 1-element tuple comma, and tuple(str)."""
    count = colors.count(target_color)
    first_index = colors.index(target_color) if target_color in colors else -1
    single_tuple = (target_color,)
    characters = tuple(target_color)

    return {
        "count": count,
        "first_index": first_index,
        "single_tuple": single_tuple,
        "characters": characters,
    }


def format_profile_interpolation(name: str, age: int) -> dict[str, str]:
    """Exercise 3: string interpolation using %, .format(), and f-strings."""
    percent = "Name: %s | Age: %d | Triple: %d" % (name, age, 3 * age)
    fmt = "Name: {0} | Age: {1} | Triple: {2}".format(name, age, 3 * age)
    fstring = f"Name: {name} | Age: {age} | Triple: {3 * age}"
    return {
        "percent": percent,
        "format": fmt,
        "fstring": fstring,
    }


def simulate_paper_stack(actions: list[tuple[str, str]]) -> dict[str, Any]:
    """Exercise 4: LIFO stack simulation with .append(), .pop(), and len()."""
    stack: list[str] = []
    popped_items: list[str] = []

    for operation, document in actions:
        if operation == "push":
            stack.append(document)
        elif operation == "pop" and stack:
            popped_items.append(stack.pop())

    return {
        "remaining_stack": stack,
        "popped_items": popped_items,
        "size": len(stack),
        "top": stack[-1] if stack else None,
    }


def update_person_profile(
    person: dict[str, Any], new_age: int, new_course: str, city: str
) -> dict[str, Any]:
    """Exercise 5: updating a dictionary with an inner list and safe .get()."""
    profile = dict(person)
    profile["education"] = list(person.get("education", []))

    profile["age"] = new_age
    profile["education"].append(new_course)
    profile["city"] = city
    phone = profile.get("phone", "Not provided")

    return {
        "profile": profile,
        "phone": phone,
        "total_keys": len(profile),
        "keys": list(profile.keys()),
        "values": list(profile.values()),
        "items": list(profile.items()),
    }


def analyze_sets(s1: set[Any], s2: set[Any]) -> dict[str, Any]:
    """Exercise 6: set union, intersection, difference, subset check, and update."""
    s1_updated = s1.copy()
    s1_updated.update(s2)

    return {
        "union": s1.union(s2),
        "intersection": s1.intersection(s2),
        "difference_s1_s2": s1 - s2,
        "s2_is_subset_of_s1": s2 <= s1,
        "s1_updated": s1_updated,
    }


def cube_number(number: int | float) -> int | float:
    """Exercise 7a: parameterized function returning number cubed."""
    return number ** 3


def sum_variadic_args(*args: int | float) -> dict[str, Any]:
    """Exercise 7b: sum variable arguments confirming *args is a tuple."""
    return {
        "args_type": type(args).__name__,
        "count": len(args),
        "sum": sum(args),
    }


def build_profile(name: str, *skills: str, **details: Any) -> dict[str, Any]:
    """Exercise 7c: combine fixed parameter, *args (tuple), and **kwargs (dict)."""
    return {
        "name": name,
        "skills": skills,
        "skills_type": type(skills).__name__,
        "details": dict(details),
    }


def generate_cohort_report(
    students: list[dict[str, Any]],
    *required_subjects: str,
    **config: Any,
) -> dict[str, Any]:
    """Exercise 8: combine lists, sets, LIFO stacks, dicts, f-strings, and *args/**kwargs."""
    title = str(config.get("title", "Cohort Report"))
    passing_grade = float(config.get("passing_grade", 7.0))
    required_set = set(required_subjects)

    approved_stack: list[str] = []
    lines: list[str] = []

    for student in students:
        name = str(student["name"])
        grades = student.get("grades", [])
        average = sum(grades) / len(grades) if grades else 0.0
        subjects = set(student.get("subjects", set()))
        completed_required = required_set <= subjects
        is_approved = average >= passing_grade and completed_required

        if is_approved:
            approved_stack.append(name)

        status = "APPROVED" if is_approved else "PENDING"
        lines.append(f"{name} | Avg: {average:.2f} | Status: {status}")

    last_approved = approved_stack[-1] if approved_stack else None

    return {
        "title": title,
        "approved": list(approved_stack),
        "lines": lines,
        "last_approved": last_approved,
        "total_approved": len(approved_stack),
    }


def main() -> None:
    """Demonstrate all Module 3 exercise solutions."""
    print("Ex. 1:", manipulate_list([1, 2, 3], 4, 2))
    print("Ex. 2:", analyze_colors_tuple(("blue", "green", "blue"), "blue"))
    print("Ex. 3:", format_profile_interpolation("Ana", 20))
    print(
        "Ex. 4:",
        simulate_paper_stack(
            [("push", "Doc A"), ("push", "Doc B"), ("pop", "")]
        ),
    )
    print(
        "Ex. 5:",
        update_person_profile(
            {"name": "Fernando", "age": 43, "education": ["Python"]},
            44,
            "OOP",
            "Curitiba",
        ),
    )
    print("Ex. 6:", analyze_sets({1, 2, 3, 4}, {2, 3}))
    print("Ex. 7:", cube_number(3), sum_variadic_args(10, 20, 30))
    print("Ex. 7c:", build_profile("Maria", "Python", "SQL", level="Mid"))
    print(
        "Ex. 8:",
        generate_cohort_report(
            [
                {"name": "Ana", "grades": [8.0, 9.0], "subjects": {"Python", "Data"}},
                {"name": "John", "grades": [6.0, 7.0], "subjects": {"Python"}},
            ],
            "Python",
            "Data",
            title="Cohort 2026",
            passing_grade=7.0,
        ),
    )


if __name__ == "__main__":
    main()
