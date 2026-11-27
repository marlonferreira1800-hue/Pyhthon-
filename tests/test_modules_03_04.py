"""Pytest suite covering Module 3 and Module 4 examples, sales package, and solutions."""

import math
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules.module_03_data_structures_functions.examples import (  # noqa: E402
    ch13_lists_tuples_stacks,
    ch14_dictionaries,
    ch15_sets,
    ch16_string_interpolation,
    ch17_functions,
)
from modules.module_03_data_structures_functions.solutions import (  # noqa: E402
    solved_exercises as m3_sol,
)
from modules.module_04_modules_exceptions.examples import (  # noqa: E402
    addition,
    ch18_introspection_dir_help,
    ch19_builtins_and_math,
    ch22_tracebacks_exceptions,
    greetings,
    index,
)
from modules.module_04_modules_exceptions.examples.sales import price_calc  # noqa: E402
from modules.module_04_modules_exceptions.solutions import (  # noqa: E402
    solved_exercises as m4_sol,
)

M3_DIR = PROJECT_ROOT / "modules" / "module_03_data_structures_functions"
M4_DIR = PROJECT_ROOT / "modules" / "module_04_modules_exceptions"


def test_required_files_exist() -> None:
    """Verify all expected Module 3 and Module 4 artifacts exist."""
    expected_paths = [
        M3_DIR / "README.md",
        M3_DIR / "exercises.md",
        M3_DIR / "solutions" / "solved_exercises.py",
        M4_DIR / "README.md",
        M4_DIR / "exercises.md",
        M4_DIR / "solutions" / "solved_exercises.py",
        M4_DIR / "examples" / "greetings.py",
        M4_DIR / "examples" / "addition.py",
        M4_DIR / "examples" / "index.py",
        M4_DIR / "examples" / "sales" / "__init__.py",
        M4_DIR / "examples" / "sales" / "price_calc.py",
    ]
    for path in expected_paths:
        assert path.is_file(), f"Missing required file: {path}"


@pytest.mark.parametrize(
    "script_path",
    [
        M3_DIR / "examples" / "ch13_lists_tuples_stacks.py",
        M3_DIR / "examples" / "ch14_dictionaries.py",
        M3_DIR / "examples" / "ch15_sets.py",
        M3_DIR / "examples" / "ch16_string_interpolation.py",
        M3_DIR / "examples" / "ch17_functions.py",
        M3_DIR / "solutions" / "solved_exercises.py",
        M4_DIR / "examples" / "ch18_introspection_dir_help.py",
        M4_DIR / "examples" / "ch19_builtins_and_math.py",
        M4_DIR / "examples" / "greetings.py",
        M4_DIR / "examples" / "addition.py",
        M4_DIR / "examples" / "sales" / "price_calc.py",
        M4_DIR / "examples" / "index.py",
        M4_DIR / "examples" / "ch22_tracebacks_exceptions.py",
        M4_DIR / "solutions" / "solved_exercises.py",
    ],
    ids=lambda p: p.relative_to(PROJECT_ROOT).as_posix(),
)
def test_example_and_solution_scripts_run_cleanly(script_path: Path) -> None:
    """Every example and solution script must run non-blockingly without PYTHONPATH and exit 0."""
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert result.returncode == 0, (
        f"{script_path.name} failed with stderr:\n{result.stderr}"
    )


def test_module_03_examples(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture) -> None:
    """Validate Chapter 13–17 example modules."""
    lists_res = ch13_lists_tuples_stacks.demonstrate_lists()
    assert lists_res["nested_name"] == "Ana"
    assert lists_res["reverse_return"] is None
    assert lists_res["reversed_list"] == [30, 20, 10]

    tuples_res = ch13_lists_tuples_stacks.demonstrate_tuples()
    assert tuples_res["not_a_tuple_type"] == "int"
    assert tuples_res["single_item_tuple_type"] == "tuple"
    assert tuples_res["ana_characters"] == ("A", "n", "a")
    assert tuples_res["blue_count"] == 2
    assert tuples_res["green_index"] == 1

    stack_res = ch13_lists_tuples_stacks.demonstrate_lifo_stack()
    assert stack_res["initial_size"] == 3
    assert stack_res["first_popped"] == "Urgent Report"
    assert stack_res["second_popped"] == "Signed Contract"
    assert stack_res["remaining_size"] == 1

    dict_res = ch14_dictionaries.create_and_update_person()
    assert dict_res["person"]["age"] == 44
    assert "Data Science" in dict_res["person"]["education"]
    assert dict_res["person"]["city"] == "Curitiba"
    assert dict_res["phone"] == "Not provided"

    set_res = ch15_sets.demonstrate_sets()
    assert set_res["deduplicated"] == {1, 2, 3}
    assert set_res["is_subset"] is True
    assert set_res["not_subset"] is False
    assert set_res["difference"] == {1, 3}
    assert set_res["a_updated"] == {1, 2, 3, 4, 5}

    interp_res = ch16_string_interpolation.generate_interpolation_examples("Ana", 10)
    assert "30" in interp_res["percent"]
    assert "30" in interp_res["format_auto"]
    assert "30" in interp_res["format_indexed"]
    assert "30" in interp_res["fstring"]

    assert ch17_functions.welcome() is None
    assert "Welcome" in capsys.readouterr().out
    assert ch17_functions.cube_number(3) == 27
    variadic = ch17_functions.sum_variadic(2, 4, 6)
    assert variadic["type"] is tuple
    assert variadic["total"] == 12
    kw = ch17_functions.user_info(name="Ana", role="Dev")
    assert kw["type"] is dict
    assert kw["kwargs"] == {"name": "Ana", "role": "Dev"}

    monkeypatch.setattr("builtins.input", lambda _: "5")
    assert ch17_functions.interactive_cube_prompt() == 125


def test_module_03_solved_exercises() -> None:
    """Validate all 8 solutions in Module 3."""
    original_list = [1, 2, 3]
    ex1 = m3_sol.manipulate_list(original_list, 9, 2)
    assert original_list == [1, 2, 3]
    assert ex1["list"] == [1, 3, 9]
    assert ex1["added_index"] == 2
    assert ex1["reversed"] == [9, 3, 1]
    assert ex1["nested_name"] == "Ana"

    ex2 = m3_sol.analyze_colors_tuple(("red", "blue", "red"), "red")
    assert ex2["count"] == 2
    assert ex2["first_index"] == 0
    assert ex2["single_tuple"] == ("red",)
    assert ex2["characters"] == ("r", "e", "d")
    assert m3_sol.analyze_colors_tuple(("red",), "green")["first_index"] == -1

    ex3 = m3_sol.format_profile_interpolation("John", 12)
    assert ex3["percent"] == ex3["format"] == ex3["fstring"]
    assert "36" in ex3["fstring"]

    ex4 = m3_sol.simulate_paper_stack(
        [("pop", ""), ("push", "A"), ("push", "B"), ("pop", ""), ("push", "C")]
    )
    assert ex4["remaining_stack"] == ["A", "C"]
    assert ex4["popped_items"] == ["B"]
    assert ex4["size"] == 2
    assert ex4["top"] == "C"

    source_person = {"name": "Fernando", "age": 43, "education": ["Python"]}
    ex5 = m3_sol.update_person_profile(source_person, 44, "ML", "Curitiba")
    assert source_person["age"] == 43
    assert source_person["education"] == ["Python"]
    assert ex5["profile"]["age"] == 44
    assert ex5["profile"]["education"] == ["Python", "ML"]
    assert ex5["profile"]["city"] == "Curitiba"
    assert ex5["phone"] == "Not provided"
    assert ex5["total_keys"] == 4

    ex6 = m3_sol.analyze_sets({1, 2, 3, 4}, {2, 3})
    assert ex6["union"] == {1, 2, 3, 4}
    assert ex6["intersection"] == {2, 3}
    assert ex6["difference_s1_s2"] == {1, 4}
    assert ex6["s2_is_subset_of_s1"] is True
    assert ex6["s1_updated"] == {1, 2, 3, 4}

    assert m3_sol.cube_number(4) == 64
    ex7b = m3_sol.sum_variadic_args(5, 10, 15)
    assert ex7b == {"args_type": "tuple", "count": 3, "sum": 30}
    ex7c = m3_sol.build_profile("Maria", "Python", "SQL", city="SP")
    assert ex7c["skills_type"] == "tuple"
    assert ex7c["details"] == {"city": "SP"}

    ex8 = m3_sol.generate_cohort_report(
        [
            {"name": "Ana", "grades": [8.0, 9.0], "subjects": {"Python", "Data"}},
            {"name": "Bob", "grades": [8.5, 9.5], "subjects": {"Python"}},
            {"name": "Eva", "grades": [], "subjects": {"Python", "Data"}},
        ],
        "Python",
        "Data",
        title="Cohort A",
        passing_grade=7.0,
    )
    assert ex8["title"] == "Cohort A"
    assert ex8["approved"] == ["Ana"]
    assert ex8["last_approved"] == "Ana"
    assert ex8["total_approved"] == 1
    assert len(ex8["lines"]) == 3


def test_module_04_examples(monkeypatch: pytest.MonkeyPatch) -> None:
    """Validate Chapter 18, 19, 20, and 22 example modules and sales package."""
    intro = ch18_introspection_dir_help.inspect_object([1, 2, 3])
    assert intro["type"] == "list"
    assert "append" in intro["public"]
    assert "__len__" in intro["dunders"]
    assert "append" in ch18_introspection_dir_help.capture_help_safely([].append)

    b_info = ch19_builtins_and_math.analyze_builtins()
    assert "ValueError" in b_info["exceptions"]
    assert "print" in b_info["functions_and_types"]
    assert "__name__" in b_info["dunders"]
    assert math.isclose(ch19_builtins_and_math.calculate_circle_area(2), 4 * math.pi)
    assert ch19_builtins_and_math.compare_math_imports(3)["equal"] is True
    with pytest.raises(ValueError):
        ch19_builtins_and_math.calculate_circle_area(-1)

    assert "Fernando" in greetings.greet("Fernando")
    assert addition.add(4, 6) == 10
    assert addition.subtract(10, 3) == 7
    assert price_calc.increase_price(100.0, 15.0) == 115.0
    assert price_calc.discount_price(100.0, 20.0) == 80.0
    with pytest.raises(ValueError):
        price_calc.increase_price(-10, 5)

    demo = index.run_modularization_demo()
    assert demo["sum_result"] == 42
    assert demo["marked_up_price"] == 225.0
    assert demo["discounted_price"] == 180.0
    assert demo["addition_module_name"] != "__main__"
    assert demo["sys_path_count"] > 0

    common_errs = ch22_tracebacks_exceptions.demonstrate_common_exceptions()
    assert set(common_errs.keys()) == {"NameError", "ValueError", "TypeError"}

    ok_res = ch22_tracebacks_exceptions.safe_add_pattern("10", "20")
    assert ok_res["ok"] is True and ok_res["result"] == 30 and ok_res["finally_ran"] is True
    val_err = ch22_tracebacks_exceptions.safe_add_pattern("abc", "20")
    assert val_err["ok"] is False and val_err["error_type"] == "ValueError" and val_err["finally_ran"] is True
    type_err = ch22_tracebacks_exceptions.safe_add_pattern(None, "20")
    assert type_err["ok"] is False and type_err["error_type"] == "TypeError" and type_err["finally_ran"] is True

    inputs = iter(["7", "8"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert ch22_tracebacks_exceptions.interactive_addition()["result"] == 15


def test_module_04_solved_exercises() -> None:
    """Validate all 8 solutions in Module 4."""
    ex1 = m4_sol.inspect_attributes("hello")
    assert ex1["type"] == "str"
    assert "upper" in ex1["public"]
    assert "__len__" in ex1["special"]

    ex2 = m4_sol.explore_builtins_and_area(2.0)
    assert ex2["builtins_verified"] is True
    assert math.isclose(ex2["area"], math.pi * 4.0)
    with pytest.raises(ValueError):
        m4_sol.explore_builtins_and_area(-5)

    assert m4_sol.safe_divide("10", "2")["result"] == 5.0
    assert m4_sol.safe_divide("abc", "2")["error_type"] == "ValueError"
    assert m4_sol.safe_divide(None, "2")["error_type"] == "TypeError"
    assert m4_sol.safe_divide("10", 0)["error_type"] == "ZeroDivisionError"

    ex4 = m4_sol.diagnose_modules_and_paths()
    assert ex4["greetings_module"] != "__main__"
    assert ex4["addition_module"] != "__main__"
    assert ex4["sys_path_count"] > 0
    assert ex4["sample_sum"] == 15

    ex5 = m4_sol.compute_price_table([100.0, 200.0], 10.0)
    assert ex5[0]["updated_price"] == 110.0
    assert ex5[1]["updated_price"] == 220.0

    ex6_ok = m4_sol.safe_sum_inputs("8", "12")
    assert ex6_ok["ok"] is True and ex6_ok["sum"] == 20 and ex6_ok["finalized"] is True
    ex6_bad = m4_sol.safe_sum_inputs("bad", "12")
    assert ex6_bad["ok"] is False and ex6_bad["error_type"] == "ValueError" and ex6_bad["finalized"] is True
    ex6_none = m4_sol.safe_sum_inputs(None, "12")
    assert ex6_none["ok"] is False and ex6_none["error_type"] == "TypeError" and ex6_none["finalized"] is True

    ex7 = m4_sol.convert_and_divide_pairs([("10", "2"), ("10", "0"), ("abc", "2"), (None, "2")])
    assert ex7["successes"] == [5.0]
    assert ex7["finalized_attempts"] == 4
    assert [f["error_type"] for f in ex7["failures"]] == [
        "ZeroDivisionError",
        "ValueError",
        "TypeError",
    ]

    ex8 = m4_sol.process_sales_batch(
        [
            {"product": "Book", "price": "100.0", "markup": 10},
            {"product": "Pen", "price": "20.0"},
            {"product": "BadPrice", "price": "xyz"},
            {"price": "15.0"},
        ],
        default_rate=25.0,
    )
    assert len(ex8["processed"]) == 2
    assert ex8["processed"][0]["updated_price"] == 110.0
    assert ex8["processed"][1]["updated_price"] == 25.0
    assert ex8["total_updated"] == 135.0
    assert ex8["audit_completed"] is True
    assert [e["error_type"] for e in ex8["errors"]] == ["ValueError", "KeyError"]
