"""Automated pytest suite for Modules 1 and 2 (Chapters 1–12)."""

import importlib
from math import pi
from pathlib import Path
import subprocess
import sys

import pytest

from modules.module_01_fundamentals.examples import (
    ch01_introduction_zen,
    ch02_environment_levels,
    ch03_logic_syntax_indentation,
    ch04_basic_structure,
    ch05_data_types,
    ch06_comments,
    ch07_variables_objects,
    ch08_basic_functions_casting,
)
from modules.module_01_fundamentals.solutions import solved_exercises as sol_m1
from modules.module_02_control_flow_strings.examples import (
    ch09_operators,
    ch10_conditionals,
    ch11_loops,
    ch12_strings_ansi,
)
from modules.module_02_control_flow_strings.solutions import solved_exercises as sol_m2

PROJECT_ROOT = Path(__file__).resolve().parent.parent

EXAMPLE_SCRIPTS = sorted(
    [
        *(PROJECT_ROOT / "modules" / "module_01_fundamentals" / "examples").glob("ch*.py"),
        *(PROJECT_ROOT / "modules" / "module_02_control_flow_strings" / "examples").glob("ch*.py"),
    ]
)

SOLUTION_SCRIPTS = [
    PROJECT_ROOT / "modules" / "module_01_fundamentals" / "solutions" / "solved_exercises.py",
    PROJECT_ROOT / "modules" / "module_02_control_flow_strings" / "solutions" / "solved_exercises.py",
]


# ---------------------------------------------------------------------------
# Subprocess Non-Blocking Execution Tests (all example & solution scripts)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("script_path", EXAMPLE_SCRIPTS + SOLUTION_SCRIPTS, ids=lambda p: p.name)
def test_scripts_run_cleanly_without_blocking(script_path: Path) -> None:
    """Every script must run cleanly with empty stdin (`echo ""`) and exit code 0."""
    proc = subprocess.run(
        [sys.executable, str(script_path)],
        input="",
        text=True,
        capture_output=True,
        cwd=str(PROJECT_ROOT),
        timeout=15,
        check=False,
    )
    assert proc.returncode == 0, f"{script_path.name} failed:\n{proc.stderr}"
    assert proc.stdout.strip(), f"{script_path.name} produced no output"


def test_interactive_examples_survive_empty_stdin() -> None:
    """Interactive mode (--interactive) must also handle empty stdin safely without tracebacks."""
    interactive_scripts = [
        PROJECT_ROOT / "modules" / "module_01_fundamentals" / "examples" / "ch03_logic_syntax_indentation.py",
        PROJECT_ROOT / "modules" / "module_01_fundamentals" / "examples" / "ch08_basic_functions_casting.py",
        PROJECT_ROOT / "modules" / "module_02_control_flow_strings" / "examples" / "ch09_operators.py",
    ]
    for script_path in interactive_scripts:
        proc = subprocess.run(
            [sys.executable, str(script_path), "--interactive"],
            input="",
            text=True,
            capture_output=True,
            cwd=str(PROJECT_ROOT),
            timeout=15,
            check=False,
        )
        assert proc.returncode == 0, f"{script_path.name} --interactive failed:\n{proc.stderr}"


# ---------------------------------------------------------------------------
# Module 1 Examples Unit Tests (Chapters 1–8)
# ---------------------------------------------------------------------------


def test_ch01_zen_and_history() -> None:
    zen = ch01_introduction_zen.get_zen_of_python()
    assert len(zen) == 19
    assert zen[0] == "Beautiful is better than ugly."
    assert "Python" in ch01_introduction_zen.compare_hello_world()


def test_ch02_bytecode_and_binary() -> None:
    bytecode_text = ch02_environment_levels.inspect_bytecode()
    assert "BINARY_ADD" in bytecode_text
    assert ch02_environment_levels.text_to_binary("A") == "01000001"


def test_ch03_logic_keywords_lexical_and_indentation() -> None:
    logic_err, math_sum, _ = ch03_logic_syntax_indentation.demonstrate_syntax_vs_logic()
    assert logic_err == "52"
    assert math_sum == 7
    assert len(ch03_logic_syntax_indentation.list_reserved_keywords()) == 35
    assert ch03_logic_syntax_indentation.lexical_analysis_compliment(False) == "You areveryveryverycool!"
    assert ch03_logic_syntax_indentation.lexical_analysis_compliment(True) == "You are very very very cool!"
    assert ch03_logic_syntax_indentation.classify_positive_or_negative("0") == "positive"
    assert ch03_logic_syntax_indentation.classify_positive_or_negative("-5") == "negative"


def test_ch04_to_ch07_core_concepts() -> None:
    assert ch04_basic_structure.basic_greeting() == "Hello World!!!"
    assert ch04_basic_structure.demonstrate_batteries_included()["sqrt_of_144"] == 12.0

    samples = ch05_data_types.create_type_samples()
    assert set(samples.keys()) >= {"int", "float", "bool", "str", "str_multiline", "list", "dict", "tuple"}
    assert "\n" in samples["str_multiline"]

    assert ch06_comments.compute_with_isolated_line(4, 5) == 20
    assert isinstance(ch06_comments.demonstrate_triple_quotes(), str)

    dyn = ch07_variables_objects.demonstrate_dynamic_typing_and_case()
    assert dyn["initial_type"] == "int"
    assert dyn["final_type"] == "str"
    assert dyn["are_equal"] is False

    multi = ch07_variables_objects.demonstrate_multiple_and_chained_assignment()
    assert multi["person"] == ("Maria", 32, "F", 1.89)
    assert multi["chained"] == (10, 10, 10)
    assert multi["shared_initial_id"] is True


def test_ch08_formatting_sets_dicts_and_casting() -> None:
    styles = ch08_basic_functions_casting.format_three_styles("Maria", 32)
    assert styles["percent"] == styles["format"] == styles["fstring"]
    invoice = ch08_basic_functions_casting.generate_overdue_invoice("Maria", 250.0, "05/10")
    assert "\n" in invoice and "$250.00" in invoice

    details = ch08_basic_functions_casting.demonstrate_interaction_and_casting()
    assert details["mixed_sum_type"] == "float"
    assert details["braces_5_type"] == "set"
    assert details["empty_braces_type"] == "dict"
    assert details["braces_kv_type"] == "dict"
    assert details["safe_concat"] == "Recorded age: 15"


# ---------------------------------------------------------------------------
# Module 1 Solved Exercises Tests
# ---------------------------------------------------------------------------


def test_module_01_solved_exercises() -> None:
    assert sol_m1.ex01_hello_zen(1) == {
        "greeting": "Hello World!!!",
        "principle": "Beautiful is better than ugly.",
    }
    with pytest.raises(ValueError):
        sol_m1.ex01_hello_zen(20)
    with pytest.raises(ValueError):
        sol_m1.ex01_hello_zen(True)  # bool must be rejected

    assert sol_m1.ex02_compare_concat_and_sum("5", "2") == {
        "concatenation": "52",
        "integer_sum": 7,
    }

    assert sol_m1.ex03_classify_identifier("class") == "forbidden_keyword"
    assert sol_m1.ex03_classify_identifier("1score") == "forbidden_syntax"
    assert sol_m1.ex03_classify_identifier("NAME") == "valid_discouraged"
    assert sol_m1.ex03_classify_identifier("salário") == "valid_discouraged"
    assert sol_m1.ex03_classify_identifier("student_name") == "valid_recommended"

    inspected = sol_m1.ex04_inspect_collections(5)
    assert inspected["types"] == {
        "set": "set",
        "empty_dict": "dict",
        "populated_dict": "dict",
        "list": "list",
        "tuple": "tuple",
    }

    reg = sol_m1.ex05_multiple_registration("Maria", 32, "F", 1.89)
    assert reg["scores"] == (10, 10, 10)
    assert reg["case_differs"] is True

    inv = sol_m1.ex06_generate_invoice_and_formats("Maria", 120.5, "06/01")
    assert "\n" in inv["invoice"]
    assert inv["percent"] == inv["format"] == inv["fstring"]

    mixed = sol_m1.ex07_evaluate_positive_and_mixed_sum("10", 2.5)
    assert mixed["classification"] == "positive"
    assert mixed["sum"] == 12.5
    assert mixed["sum_type"] == "float"
    assert sol_m1.ex07_evaluate_positive_and_mixed_sum("-1", 0.5)["classification"] == "negative"

    comp = sol_m1.ex08_compliment_and_age("very", 3, 15)
    assert comp["compliment"] == "You are very very very cool!"
    assert comp["age_record"] == "Recorded age: 15"
    with pytest.raises(ValueError):
        sol_m1.ex08_compliment_and_age("very", 0, 15)


# ---------------------------------------------------------------------------
# Module 2 Examples Unit Tests (Chapters 9–12)
# ---------------------------------------------------------------------------


def test_ch09_operators_and_identity() -> None:
    steps = ch09_operators.compound_assignment_walkthrough(10.0)
    assert steps["after_+="] == 15.0
    assert steps["after_%="] == 3.0

    assert ch09_operators.evaluate_financial_goal(100.0, 5000.0, 3500.0) is True
    assert ch09_operators.evaluate_financial_goal(0.0, 5000.0, 1000.0) is False
    assert ch09_operators.evaluate_financial_goal(100.0, 5000.0, 4500.0) is False

    truth = ch09_operators.generate_truth_table()
    assert len(truth) == 4
    assert ch09_operators.demonstrate_bitwise_operators(6, 3) == {"and": 2, "or": 7, "xor": 5}

    ident = ch09_operators.compare_identity_vs_equality()
    assert ident["value_equal"] is True
    assert ident["shared_alias_is"] is True
    assert ident["distinct_objects_is"] is False


def test_ch10_conditionals_and_switch_patterns() -> None:
    assert "Bought 'Coffee'" in ch10_conditionals.go_to_the_market("Coffee", 30.0, 18.5, False, False)
    assert "Wait for the rain" in ch10_conditionals.go_to_the_market("Coffee", 30.0, 18.5, True, False)

    assert ch10_conditionals.classify_grade(9.5) == "Excellent"
    assert ch10_conditionals.classify_grade(7.0) == "Good"
    assert ch10_conditionals.classify_grade(5.0) == "Recovery"
    assert ch10_conditionals.classify_grade(4.9) == "Failed"
    with pytest.raises(ValueError):
        ch10_conditionals.classify_grade(11.0)

    for code in (1, 2, 3, 99):
        a = ch10_conditionals.select_color_if_elif(code)
        b = ch10_conditionals.select_color_dict(code)
        c = ch10_conditionals.select_color_match_case(code)
        assert a == b == c


def test_ch11_loops_and_multiplication_table() -> None:
    assert ch11_loops.count_until_break(10, 4) == [0, 1, 2, 3]
    assert ch11_loops.search_with_for_else(["rice", "beans"], "beans") == "Found 'beans' in list."
    assert ch11_loops.search_with_for_else(["rice", "beans"], "tea") == "'tea' was not found."

    table = ch11_loops.build_multiplication_table(10)
    assert len(table) == 121  # 11 x 11 (0..10 inclusive)
    assert table[0] == "0 x 0 = 0"
    assert table[-1] == "10 x 10 = 100"


def test_ch12_strings_ansi_and_formatting() -> None:
    quotes = ch12_strings_ansi.demonstrate_quotes_and_immutability("Python OOP")
    assert quotes["original_unchanged"] is True
    assert quotes["upper_preview"] == "PYTHON OOP"

    ansi_str = ch12_strings_ansi.colorize_ansi("WARN", "red")
    assert ansi_str.startswith("\033[91m") and ansi_str.endswith("\033[0m")

    pi_fmt = ch12_strings_ansi.format_pi_variants()
    assert pi_fmt["legacy_2"] == pi_fmt["modern_2"] == "3.14"
    assert pi_fmt["legacy_5"] == pi_fmt["modern_5"] == "3.14159"


# ---------------------------------------------------------------------------
# Module 2 Solved Exercises Tests
# ---------------------------------------------------------------------------


def test_module_02_solved_exercises() -> None:
    fin = sol_m2.ex01_financial_goal_and_compound(100.0, 50.0, 4000.0, 2800.0)
    assert fin == {"updated_balance": 150.0, "savings_margin": 1200.0, "goal_met": True}

    tb = sol_m2.ex02_truth_and_bitwise_summary(True, False, 6, 3)
    assert tb["logical"] == {"and": False, "or": True, "xor": True, "not_a": False}
    assert tb["bitwise"] == {"and": 2, "or": 7, "xor": 5}

    ident = sol_m2.ex03_compare_identity_and_equality(1000, 1000)
    assert ident["equal_value"] is True
    assert ident["alias_same_identity"] is True
    assert ident["independent_same_identity"] is False

    cls_res = sol_m2.ex04_classify_grade_and_market(9.2, 50.0, 25.0)
    assert cls_res == {"grade_status": "Excellent", "market_status": "Bought"}

    sw = sol_m2.ex05_dispatch_color_switch(sol_m2.Color.BLUE)
    assert sw == {"if_elif": "Blue", "dict": "Blue", "match_case": "Blue"}

    loop_res = sol_m2.ex06_while_break_and_for_search(["a", "b"], "c", 10, 3)
    assert loop_res == {"collected": [0, 1, 2], "search_status": "not_found"}

    table = sol_m2.ex07_multiplication_table(0, 10)
    assert len(table) == 121
    assert "7 x 8 = 56" in table
    with pytest.raises(ValueError):
        sol_m2.ex07_multiplication_table(5, 3)

    pipe = sol_m2.ex08_string_pipeline_ansi("Python,Strings,ANSI", "strings", pi)
    assert pipe["tokens"] == ["Python", "Strings", "ANSI"]
    assert pipe["term_found"] is True
    assert pipe["legacy_2"] == pipe["modern_2"] == "3.14"
    assert pipe["legacy_5"] == "3.14159"
    assert len(pipe["centered_header"]) == 30
    assert pipe["ansi_tag"] == "\033[91mstrings\033[0m"


def test_required_module_files_exist() -> None:
    """Ensure all required English deliverables for Modules 1 and 2 exist."""
    expected = [
        PROJECT_ROOT / "modules" / "module_01_fundamentals" / "README.md",
        PROJECT_ROOT / "modules" / "module_01_fundamentals" / "exercises.md",
        PROJECT_ROOT / "modules" / "module_01_fundamentals" / "solutions" / "solved_exercises.py",
        PROJECT_ROOT / "modules" / "module_02_control_flow_strings" / "README.md",
        PROJECT_ROOT / "modules" / "module_02_control_flow_strings" / "exercises.md",
        PROJECT_ROOT / "modules" / "module_02_control_flow_strings" / "solutions" / "solved_exercises.py",
    ]
    for path in expected:
        assert path.is_file(), f"Missing file: {path}"

    # Verify importlib cleanly imports every example module without side effects
    for script in EXAMPLE_SCRIPTS:
        rel = script.relative_to(PROJECT_ROOT).with_suffix("")
        mod_name = ".".join(rel.parts)
        mod = importlib.import_module(mod_name)
        assert hasattr(mod, "main")
