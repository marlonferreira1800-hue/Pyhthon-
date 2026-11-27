"""Standard-library CLI to browse the course structure and verify files.

Runs entirely on Python >= 3.10 standard library, discovers modules under
`modules/` dynamically, and never blocks waiting for `input()`.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence

BASE_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class ModuleMetadata:
    """Curriculum metadata for a course module."""

    number: int
    slug: str
    title: str
    chapters: str
    summary: str
    test_file: str


KNOWN_MODULES: dict[str, ModuleMetadata] = {
    "module_01_fundamentals": ModuleMetadata(
        number=1,
        slug="module_01_fundamentals",
        title="Fundamentals, Logic & First Commands",
        chapters="Ch. 1–8",
        summary=(
            "Introduction to Python, environment setup, programming logic, "
            "lexical analysis, basic structure, data types, comments, variables, and I/O."
        ),
        test_file="tests/test_modules_01_02.py",
    ),
    "module_02_control_flow_strings": ModuleMetadata(
        number=2,
        slug="module_02_control_flow_strings",
        title="Operators, Control Flow & Strings",
        chapters="Ch. 9–12",
        summary=(
            "Assignment, arithmetic, logical, relational, membership, and identity "
            "operators; conditionals (if/elif/else); while/for loops; and string formatting."
        ),
        test_file="tests/test_modules_01_02.py",
    ),
    "module_03_data_structures_functions": ModuleMetadata(
        number=3,
        slug="module_03_data_structures_functions",
        title="Data Structures, Interpolation & Functions",
        chapters="Ch. 13–17",
        summary=(
            "Lists, tuples, LIFO stacks, dictionaries, sets, string interpolation "
            "(%, .format(), f-strings), and custom functions with *args/**kwargs."
        ),
        test_file="tests/test_modules_03_04.py",
    ),
    "module_04_modules_exceptions": ModuleMetadata(
        number=4,
        slug="module_04_modules_exceptions",
        title="Introspection, Builtins, Modules, Packages & Exceptions",
        chapters="Ch. 18–20 & Ch. 22",
        summary=(
            "Runtime introspection with dir()/help(), __builtins__ and math, "
            "modularization with packages, and try/except/else/finally exception handling."
        ),
        test_file="tests/test_modules_03_04.py",
    ),
    "module_05_oop": ModuleMetadata(
        number=5,
        slug="module_05_oop",
        title="Object-Oriented Programming & Final Considerations",
        chapters="Ch. 21 & Ch. 23",
        summary=(
            "Classes, __init__, self, setattr/delattr, recursion, inheritance, "
            "polymorphism, encapsulation, and final engineering synthesis."
        ),
        test_file="tests/test_module_05_and_project.py",
    ),
}

PORTAL_FILES: tuple[str, ...] = (
    "pyproject.toml",
    "README.md",
    "SYLLABUS.md",
    "ENVIRONMENT_GUIDE.md",
    "course_cli.py",
)

FINAL_PROJECT: dict[str, str] = {
    "title": "Final Project — AutoPy Fleet & Rental Management System",
    "chapters": "Integration (Ch. 1–23)",
    "dir": "final_project",
    "readme": "final_project/README.md",
    "entrypoint": "final_project/main.py",
    "package_dir": "final_project/autopy",
    "test_file": "tests/test_module_05_and_project.py",
}

REQUIRED_TESTS: tuple[str, ...] = (
    "tests/test_modules_01_02.py",
    "tests/test_modules_03_04.py",
    "tests/test_module_05_and_project.py",
)


def _list_python_files(directory: Path) -> list[Path]:
    """Return sorted .py scripts inside a directory, ignoring __pycache__."""
    if not directory.is_dir():
        return []
    return sorted(
        path
        for path in directory.rglob("*.py")
        if "__pycache__" not in path.parts
    )


def _extract_module_number(slug: str, fallback: int) -> int:
    """Extract numeric prefix from a module directory slug."""
    match = re.search(r"(\d+)", slug)
    return int(match.group(1)) if match else fallback


def _humanize_slug(slug: str) -> str:
    """Convert a folder slug like module_06_extra into a readable title."""
    cleaned = re.sub(r"^module_\d+_", "", slug)
    return cleaned.replace("_", " ").strip().title() or slug


def discover_modules(root: Path) -> list[dict[str, object]]:
    """Discover modules under `modules/` dynamically and merge known metadata."""
    modules_root = root / "modules"
    discovered_dirs: list[Path] = []
    if modules_root.is_dir():
        discovered_dirs = sorted(
            d
            for d in modules_root.iterdir()
            if d.is_dir() and not d.name.startswith((".", "__"))
        )

    slugs_seen: set[str] = set()
    records: list[dict[str, object]] = []

    for idx, mod_dir in enumerate(discovered_dirs, start=1):
        slug = mod_dir.name
        slugs_seen.add(slug)
        meta = KNOWN_MODULES.get(slug)
        if meta is None:
            number = _extract_module_number(slug, idx)
            meta = ModuleMetadata(
                number=number,
                slug=slug,
                title=_humanize_slug(slug),
                chapters="Custom module",
                summary=f"Dynamically discovered module at modules/{slug}.",
                test_file="",
            )
        records.append(_inspect_module(root, meta, exists_on_disk=True))

    for slug, meta in KNOWN_MODULES.items():
        if slug not in slugs_seen:
            records.append(_inspect_module(root, meta, exists_on_disk=False))

    records.sort(key=lambda item: (item["module"]["number"], item["module"]["slug"]))  # type: ignore[index]
    return records


def _inspect_module(
    root: Path, meta: ModuleMetadata, *, exists_on_disk: bool
) -> dict[str, object]:
    """Inspect files inside a module directory."""
    mod_rel = f"modules/{meta.slug}"
    mod_dir = root / mod_rel
    readme_rel = f"{mod_rel}/README.md"
    exercises_rel = f"{mod_rel}/exercises.md"
    examples_rel = f"{mod_rel}/examples"
    solutions_rel = f"{mod_rel}/solutions"

    readme_ok = (root / readme_rel).is_file()
    exercises_ok = (root / exercises_rel).is_file()
    examples_dir = root / examples_rel
    solutions_dir = root / solutions_rel

    example_files = _list_python_files(examples_dir)
    solution_files = [
        p for p in _list_python_files(solutions_dir) if p.name != "__init__.py"
    ]
    test_ok = bool(meta.test_file) and (root / meta.test_file).is_file()

    complete = (
        exists_on_disk
        and readme_ok
        and exercises_ok
        and len(example_files) > 0
        and len(solution_files) > 0
    )

    return {
        "module": asdict(meta),
        "exists_on_disk": exists_on_disk and mod_dir.is_dir(),
        "complete": complete,
        "readme_rel": readme_rel,
        "readme_ok": readme_ok,
        "exercises_rel": exercises_rel,
        "exercises_ok": exercises_ok,
        "examples_rel": examples_rel,
        "examples_dir_ok": examples_dir.is_dir(),
        "examples": [p.relative_to(root).as_posix() for p in example_files],
        "solutions_rel": solutions_rel,
        "solutions_dir_ok": solutions_dir.is_dir(),
        "solutions": [p.relative_to(root).as_posix() for p in solution_files],
        "test_ok": test_ok,
    }


def _final_status(root: Path) -> dict[str, object]:
    """Inspect files for the Final Project."""
    pkg_dir = root / FINAL_PROJECT["package_dir"]
    pkg_files = _list_python_files(pkg_dir)
    readme_ok = (root / FINAL_PROJECT["readme"]).is_file()
    main_ok = (root / FINAL_PROJECT["entrypoint"]).is_file()
    init_ok = (pkg_dir / "__init__.py").is_file()
    test_ok = (root / FINAL_PROJECT["test_file"]).is_file()
    return {
        "project": FINAL_PROJECT,
        "complete": readme_ok and main_ok and init_ok,
        "readme_ok": readme_ok,
        "main_ok": main_ok,
        "package_init_ok": init_ok,
        "package_files": [p.relative_to(root).as_posix() for p in pkg_files],
        "test_ok": test_ok,
    }


def format_list_output(root: Path, as_json: bool = False) -> str:
    """Format the course overview listing all modules and the Final Project."""
    modules_data = discover_modules(root)
    final_data = _final_status(root)
    if as_json:
        return json.dumps(
            {"root": str(root), "modules": modules_data, "final_project": final_data},
            ensure_ascii=False,
            indent=2,
        )

    lines = [
        "=== Course: Python from Zero to Object-Oriented Programming ===",
        f"Root directory: {root}",
        "",
        "LEARNING MODULES:",
    ]
    for item in modules_data:
        mod = item["module"]
        examples = item["examples"]
        solutions = item["solutions"]
        status = "[OK]" if item["complete"] else "[PENDING]"
        lines.append(
            f"  {status} Module {mod['number']}: {mod['title']} ({mod['chapters']})"
        )
        test_info = mod["test_file"] or "n/a"
        lines.append(
            f"       Folder: modules/{mod['slug']} | Examples .py: {len(examples)} | "
            f"Solutions .py: {len(solutions)} | Tests: {test_info}"
        )

    final_tag = "[OK]" if final_data["complete"] else "[PENDING]"
    lines.extend(
        [
            "",
            "INTEGRATED FINAL PROJECT:",
            f"  {final_tag} {FINAL_PROJECT['title']} ({FINAL_PROJECT['chapters']})",
            (
                f"       Folder: {FINAL_PROJECT['dir']} | autopy/ files: "
                f"{len(final_data['package_files'])} | Demo: "
                f"python {FINAL_PROJECT['entrypoint']} --demo"
            ),
            "",
            "Tip: run `python course_cli.py --module N`, `--final`, or `--check`.",
        ]
    )
    return "\n".join(lines)


def format_module_output(
    root: Path, module_number: int, as_json: bool = False
) -> tuple[bool, str]:
    """Format detailed inspection for a single module."""
    modules_data = discover_modules(root)
    match = next(
        (item for item in modules_data if item["module"]["number"] == module_number),  # type: ignore[index]
        None,
    )
    if match is None:
        valid_nums = ", ".join(str(item["module"]["number"]) for item in modules_data)  # type: ignore[index]
        msg = f"Module {module_number} not found. Available modules: {valid_nums}."
        if as_json:
            return False, json.dumps({"error": msg}, ensure_ascii=False, indent=2)
        return False, msg

    if as_json:
        return True, json.dumps(match, ensure_ascii=False, indent=2)

    mod = match["module"]
    mark = lambda ok: "[OK]" if ok else "[MISSING]"
    examples: list[str] = match["examples"]  # type: ignore[assignment]
    solutions: list[str] = match["solutions"]  # type: ignore[assignment]

    lines = [
        f"=== Module {mod['number']}: {mod['title']} ({mod['chapters']}) ===",
        f"Summary: {mod['summary']}",
        "",
        "Module Files:",
        f"  {mark(bool(match['readme_ok']))} Lesson (README): {match['readme_rel']}",
        f"  {mark(bool(match['exercises_ok']))} Exercises:       {match['exercises_rel']}",
        f"  {mark(len(solutions) > 0)} Solutions dir:   {match['solutions_rel']}/ ({len(solutions)} .py)",
    ]
    if mod["test_file"]:
        lines.append(
            f"  {mark(bool(match['test_ok']))} Pytest suite:    {mod['test_file']}"
        )

    lines.extend(["", f"Example Scripts in {match['examples_rel']}/:"])
    if examples:
        lines.extend(f"  - {ex_path}" for ex_path in examples)
    else:
        lines.append("  (no .py scripts found yet)")

    lines.extend(["", f"Solution Scripts in {match['solutions_rel']}/:"])
    if solutions:
        lines.extend(f"  - {sol_path}" for sol_path in solutions)
    else:
        lines.append("  (no solution .py scripts found yet)")

    lines.extend(["", "Suggested Commands:"])
    if solutions:
        lines.append(f"  python {solutions[0]}")
    elif examples:
        lines.append(f"  python {examples[0]}")
    if mod["test_file"]:
        lines.append(f"  python -m pytest {mod['test_file']} -v")

    return True, "\n".join(lines)


def format_final_output(root: Path, as_json: bool = False) -> str:
    """Format detailed inspection for the Final Project."""
    status = _final_status(root)
    if as_json:
        return json.dumps(status, ensure_ascii=False, indent=2)

    mark = lambda ok: "[OK]" if ok else "[MISSING]"
    pkg_files: list[str] = status["package_files"]  # type: ignore[assignment]
    lines = [
        f"=== {FINAL_PROJECT['title']} ===",
        f"Scope: {FINAL_PROJECT['chapters']}",
        "",
        "Core Files:",
        f"  {mark(bool(status['readme_ok']))} Documentation:  {FINAL_PROJECT['readme']}",
        f"  {mark(bool(status['main_ok']))} Entrypoint:     {FINAL_PROJECT['entrypoint']}",
        f"  {mark(bool(status['package_init_ok']))} autopy package: {FINAL_PROJECT['package_dir']}/__init__.py",
        f"  {mark(bool(status['test_ok']))} Pytest suite:   {FINAL_PROJECT['test_file']}",
        "",
        f"Python Files in {FINAL_PROJECT['package_dir']}/:",
    ]
    if pkg_files:
        lines.extend(f"  - {path}" for path in pkg_files)
    else:
        lines.append("  (no .py files found yet)")

    lines.extend(
        [
            "",
            "Run Commands:",
            f"  python {FINAL_PROJECT['entrypoint']} --demo",
            f"  python {FINAL_PROJECT['entrypoint']}",
            f"  python -m pytest {FINAL_PROJECT['test_file']} -v",
        ]
    )
    return "\n".join(lines)


def run_check(root: Path) -> tuple[bool, list[tuple[str, bool, str]]]:
    """Verify portal, dynamically discovered modules, final project, and tests."""
    results: list[tuple[str, bool, str]] = []

    for rel_path in PORTAL_FILES:
        results.append((rel_path, (root / rel_path).is_file(), "portal file"))

    for item in discover_modules(root):
        mod = item["module"]
        num = mod["number"]
        results.append(
            (str(item["readme_rel"]), bool(item["readme_ok"]), f"Module {num} README")
        )
        examples: list[str] = item["examples"]  # type: ignore[assignment]
        results.append(
            (
                f"{item['examples_rel']}/",
                len(examples) > 0,
                f"Module {num} examples ({len(examples)} .py)",
            )
        )
        results.append(
            (
                str(item["exercises_rel"]),
                bool(item["exercises_ok"]),
                f"Module {num} exercises",
            )
        )
        solutions: list[str] = item["solutions"]  # type: ignore[assignment]
        results.append(
            (
                f"{item['solutions_rel']}/",
                len(solutions) > 0,
                f"Module {num} solutions ({len(solutions)} .py)",
            )
        )

    results.append(
        (FINAL_PROJECT["readme"], (root / FINAL_PROJECT["readme"]).is_file(), "Final Project README")
    )
    results.append(
        (FINAL_PROJECT["entrypoint"], (root / FINAL_PROJECT["entrypoint"]).is_file(), "Final Project main.py")
    )
    pkg_init = f"{FINAL_PROJECT['package_dir']}/__init__.py"
    results.append(
        (pkg_init, (root / pkg_init).is_file(), "Final Project autopy package")
    )

    for test_rel in REQUIRED_TESTS:
        results.append((test_rel, (root / test_rel).is_file(), "Pytest suite"))

    all_ok = all(ok for _, ok, _ in results)
    return all_ok, results


def format_check_output(root: Path, as_json: bool = False) -> tuple[bool, str]:
    """Format the structural integrity check report."""
    all_ok, results = run_check(root)
    passed = sum(1 for _, ok, _ in results if ok)
    total = len(results)

    if as_json:
        payload = {
            "root": str(root),
            "all_ok": all_ok,
            "passed": passed,
            "total": total,
            "checks": [
                {"path": path, "ok": ok, "description": desc}
                for path, ok, desc in results
            ],
        }
        return all_ok, json.dumps(payload, ensure_ascii=False, indent=2)

    lines = [
        "=== Course Structure Integrity Check ===",
        f"Root directory: {root}",
        "",
    ]
    for path, ok, desc in results:
        tag = "[OK]     " if ok else "[MISSING]"
        lines.append(f"  {tag} {path:<60} ({desc})")

    lines.extend(
        [
            "",
            f"Summary: {passed}/{total} checks passed.",
            (
                "Overall status: COMPLETE."
                if all_ok
                else "Overall status: INCOMPLETE (missing items detected)."
            ),
        ]
    )
    return all_ok, "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="course_cli.py",
        description=(
            "Course navigator and integrity checker for 'Python from Zero to OOP'."
        ),
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List all discovered modules and the Final Project.",
    )
    group.add_argument(
        "--module",
        "-m",
        type=int,
        metavar="N",
        help="Inspect details, scripts, and commands for module N.",
    )
    group.add_argument(
        "--final",
        "-f",
        action="store_true",
        help="Inspect details and commands for the Final Project (AutoPy).",
    )
    group.add_argument(
        "--check",
        "-c",
        action="store_true",
        help="Verify that all expected course files and folders are present.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=BASE_DIR,
        help="Course root directory (defaults to this script's directory).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output machine-readable JSON.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entrypoint."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = build_parser()
    args = parser.parse_args(argv)
    root = args.root.resolve()

    if args.check:
        all_ok, output = format_check_output(root, as_json=args.json)
        print(output)
        return 0 if all_ok else 1

    if args.module is not None:
        found, output = format_module_output(root, args.module, as_json=args.json)
        print(output)
        return 0 if found else 1

    if args.final:
        print(format_final_output(root, as_json=args.json))
        return 0

    print(format_list_output(root, as_json=args.json))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
