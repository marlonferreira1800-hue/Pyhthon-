/* ==========================================================================
   Python from ZERO to Object-Oriented Programming — Interactive Controller
   Zero dependencies · Safe DOM rendering · English Edition
   ========================================================================== */

(function () {
  "use strict";

  /* ------------------------------------------------------------------------
     1. Course Contract Data (5 Modules & All 23 Chapters)
     ------------------------------------------------------------------------ */

  const MODULES = {
    "1": {
      id: "1",
      name: "Module 1 — Fundamentals, Logic & First Commands",
      chaptersRange: "Chapters 1–8",
      readme: "modules/module_01_fundamentals/README.md",
      exercises: "modules/module_01_fundamentals/exercises.md",
      summary: "Python philosophy, environment levels, algorithms, lexical order, basic types, comments, variables, and I/O casting."
    },
    "2": {
      id: "2",
      name: "Module 2 — Operators, Control Flow & Strings",
      chaptersRange: "Chapters 9–12",
      readme: "modules/module_02_control_flow_strings/README.md",
      exercises: "modules/module_02_control_flow_strings/exercises.md",
      summary: "Assignment/arithmetic/logical/identity operators, conditionals, match/case notes, while/for loops, and string formatting."
    },
    "3": {
      id: "3",
      name: "Module 3 — Data Structures, Interpolation & Functions",
      chaptersRange: "Chapters 13–17",
      readme: "modules/module_03_data_structures_functions/README.md",
      exercises: "modules/module_03_data_structures_functions/exercises.md",
      summary: "Lists, tuples, LIFO stacks, dictionaries, sets, string interpolation evolution, and functions with *args / **kwargs."
    },
    "4": {
      id: "4",
      name: "Module 4 — Introspection, Builtins, Modules & Exceptions",
      chaptersRange: "Chapters 18–20 & 22",
      readme: "modules/module_04_modules_exceptions/README.md",
      exercises: "modules/module_04_modules_exceptions/exercises.md",
      summary: "Runtime introspection with dir()/help(), __builtins__, stdlib math, modular packages, and safe try/except/else/finally."
    },
    "5": {
      id: "5",
      name: "Module 5 — Object-Oriented Programming & Closing Insights",
      chaptersRange: "Chapters 21 & 23",
      readme: "modules/module_05_oop/README.md",
      exercises: "modules/module_05_oop/exercises.md",
      summary: "Classes, __init__, self, dynamic attributes, recursion, inheritance, polymorphism, encapsulation, and career bridges."
    }
  };

  const CHAPTERS = [
    {
      num: 1,
      module: "1",
      title: "Introduction to Python",
      description: "Why learn Python, its history (1989–1994, Guido van Rossum), the 19 principles of the Zen of Python, industry adoption, and future.",
      keywords: ["Zen of Python", "Guido van Rossum", "Interpreted", "History"]
    },
    {
      num: 2,
      module: "1",
      title: "Programming Environment",
      description: "Backend vs. Frontend, high-level vs. bytecode/Assembly vs. machine code, and major IDEs: PyCharm, VS Code, Anaconda, and Jupyter.",
      keywords: ["Backend", "Bytecode", "VS Code", "PyCharm", "Jupyter"]
    },
    {
      num: 3,
      module: "1",
      title: "Programming Logic",
      description: "Algorithms (recipe analogy & 3 I/O flows), Syntax vs. Logic errors ('5'+'2' vs 5+2), 35 reserved keywords, lexical scan, and indentation.",
      keywords: ["Algorithms", "SyntaxError", "keyword.kwlist", "Indentation"],
      labId: "syntax-vs-logic"
    },
    {
      num: 4,
      module: "1",
      title: "Basic Program Structure",
      description: "Python's batteries-included philosophy, writing print('Hello World!!!'), and passing arguments inside parentheses.",
      keywords: ["Batteries Included", "print()", "Arguments"]
    },
    {
      num: 5,
      module: "1",
      title: "Data Types",
      description: "Core built-in types: int, float, bool, str, list, dict, tuple, and multiline string literals.",
      keywords: ["int", "float", "bool", "str", "list", "dict", "tuple"]
    },
    {
      num: 6,
      module: "1",
      title: "Comments",
      description: "Single-line # comments, multiline docstrings/blocks, string assignment caveats, and commenting lines to isolate bugs.",
      keywords: ["# comments", "Docstrings", "Debugging"]
    },
    {
      num: 7,
      module: "1",
      title: "Variables & Objects",
      description: "Memory drawers, dynamic typing, case sensitivity, naming conventions, multiple unpacking, and chained assignment.",
      keywords: ["Dynamic Typing", "Case Sensitive", "Unpacking"]
    },
    {
      num: 8,
      module: "1",
      title: "Basic Functions & Type Casting",
      description: "Mastering print(), input(), %s / .format() / f-strings, int + float promotion, type(), explicit casting, and {5} set vs {k: v} dict.",
      keywords: ["input()", "type()", "int()", "str()", "set vs dict"]
    },
    {
      num: 9,
      module: "2",
      title: "Operators",
      description: "Assignment & augmented ops (+=, **=), arithmetic precedence, logical truth tables, bitwise ops, membership (in), relational, and is vs ==.",
      keywords: ["Precedence", "Truth Table", "in", "is vs =="]
    },
    {
      num: 10,
      module: "2",
      title: "Conditional Statements",
      description: "Branching with if, elif, and else, combining and/or conditions, nesting, and simulating switch/case plus Python 3.10+ match/case.",
      keywords: ["if / elif / else", "Nesting", "match / case"]
    },
    {
      num: 11,
      module: "2",
      title: "Repetition Loops",
      description: "Condition-driven while loops with break, iterating sequences with for and range(), for ... else, and nested loops for multiplication tables.",
      keywords: ["while", "for", "range()", "break", "Nested Loops"],
      labId: "nested-for-table"
    },
    {
      num: 12,
      module: "2",
      title: "Strings",
      description: "Quote styles, immutability with .lower()/.upper(), substring checks, .split(), ANSI terminal colors, alignment, and numeric formatting.",
      keywords: [".lower()", ".split()", "ANSI Colors", ".center()", ":.2f"]
    },
    {
      num: 13,
      module: "3",
      title: "Lists, Tuples & Stacks",
      description: "Zero-based lists, in-place mutation (.append(), .remove(), .reverse()), nested lists, immutable tuples (1,), and LIFO stacks with .pop().",
      keywords: ["list", "tuple", "LIFO", ".append()", ".pop()"],
      labId: "lifo-and-dicts"
    },
    {
      num: 14,
      module: "3",
      title: "Dictionaries",
      description: "Mapping key-value pairs, nested lists inside dicts, safe lookup via .get(), inspecting .keys()/.values()/.items(), and updating entries.",
      keywords: ["dict", ".get()", ".items()", "Key-Value"],
      labId: "lifo-and-dicts"
    },
    {
      num: 15,
      module: "3",
      title: "Numeric Sets",
      description: "Unordered duplicate-free collections with .union() (|), .intersection() (&), .update(), subset checks (<=), and set difference (-).",
      keywords: ["set", "union", "intersection", "subset <="]
    },
    {
      num: 16,
      module: "3",
      title: "String Interpolation",
      description: "Tracing the evolution of Python formatting from legacy % placeholders to .format() and expressive inline f-strings.",
      keywords: ["%s / %d", ".format()", "f-strings"]
    },
    {
      num: 17,
      module: "3",
      title: "Functions",
      description: "Built-in vs. imported vs. custom def functions, implicit None return, parameters, *args (tuple), and **kwargs (dict).",
      keywords: ["def", "return", "*args", "**kwargs"]
    },
    {
      num: 18,
      module: "4",
      title: "dir() & help() Introspection",
      description: "Inspecting object attributes, methods, and built-in docstrings directly inside the Python runtime.",
      keywords: ["dir()", "help()", "Introspection"]
    },
    {
      num: 19,
      module: "4",
      title: "Builtins & Standard Libraries",
      description: "Exploring dir(__builtins__), reserved dunder names, and importing standard modules via import math and from math import pi.",
      keywords: ["__builtins__", "import math", "from ... import"]
    },
    {
      num: 20,
      module: "4",
      title: "Modules & Packages",
      description: "Modularizing scripts with __main__ guards, organizing subpackage folders (sales/price_calc.py), aliases (as), and sys.path resolution.",
      keywords: ["__main__", "Packages", "Aliases", "sys.path"],
      labId: "sales-package"
    },
    {
      num: 21,
      module: "5",
      title: "Object-Oriented Programming",
      description: "Classes as blueprints, __init__ & self, setattr/delattr, recursion, inheritance (Cars -> Gol/Corsa), polymorphism, and encapsulation.",
      keywords: ["class", "__init__", "super()", "Polymorphism", "@property"],
      labId: "oop-inheritance"
    },
    {
      num: 22,
      module: "4",
      title: "Tracebacks & Exceptions",
      description: "Reading NameError, ValueError, and TypeError tracebacks; handling specific exceptions cleanly with try/except/else/finally.",
      keywords: ["traceback", "try / except", "else / finally", "ValueError"],
      labId: "safe-try-except"
    },
    {
      num: 23,
      module: "5",
      title: "Final Considerations",
      description: "Consolidating the journey from zero to OOP and connecting Python fundamentals to Data Science, Machine Learning, and Backend Engineering.",
      keywords: ["Career Path", "Data Science", "ML", "Software Engineering"]
    }
  ];

  /* ------------------------------------------------------------------------
     2. Reverse Engineering Lab Examples (6 Authentic Book Scenarios)
     ------------------------------------------------------------------------ */

  const LAB_EXAMPLES = [
    {
      id: "syntax-vs-logic",
      tabLabel: "'5'+'2' vs 5+2",
      moduleId: "1",
      badge: "Module 1 · Ch. 3",
      title: "Syntax Error vs. Logic Error ('5' + '2' vs. 5 + 2)",
      subtitle: "See why Python obeys types literally instead of guessing math intent, and how lexical scanning stops invalid syntax.",
      fileName: "cap03_logic_vs_syntax.py",
      scenarios: [
        {
          id: "logic",
          label: "Logic vs. Math",
          isError: false,
          lines: [
            {
              code: "wrong_sum = '5' + '2'",
              title: "String concatenation instead of addition",
              explain: "Python sees two str objects ('5' and '2'). The + operator joins characters together into '52'. No error is raised — this is a classic Logic Error when arithmetic 7 was intended.",
              note: "Always check types with type() or cast input() strings using int() before performing math."
            },
            {
              code: "right_sum = 5 + 2",
              title: "True integer addition",
              explain: "Without quotes, 5 and 2 are int literals. Python invokes integer addition and binds the result 7 to right_sum.",
              note: "Identical operator (+), completely different behavior determined by operand types."
            },
            {
              code: "phrase = 'You are ' + 3 * 'very ' + 'cool!'",
              title: "Lexical precedence (* before +)",
              explain: "Python scans left-to-right, top-to-bottom, respecting operator precedence: 3 * 'very ' runs first ('very very very '), then + concatenates left-to-right.",
              note: "From Chapter 3's lexical analysis exercise in the book."
            },
            {
              code: "print(f'Logic error: {wrong_sum} | Math: {right_sum}')",
              title: "Interpolating both results",
              explain: "The f-string formats both the string '52' and the integer 7 cleanly into a single output line.",
              note: "Observe how '52' vs 7 exposes the exact bug immediately."
            },
            {
              code: "print(phrase)",
              title: "Printing the assembled string",
              explain: "Outputs the evaluated string built by operator precedence.",
              note: null
            }
          ],
          output: "Logic error: 52 | Math: 7\nYou are very very very cool!"
        },
        {
          id: "syntax",
          label: "Syntax Error Case",
          isError: true,
          lines: [
            {
              code: "# Case-sensitive & invalid syntax example from Ch. 3:",
              title: "Comment ignored by parser",
              explain: "Lines starting with # are skipped during compilation and never become bytecode.",
              note: null
            },
            {
              code: "Print(5) + 2 =",
              title: "Trailing '=' triggers SyntaxError before execution",
              explain: "Before running line 1, Python's parser checks grammar rules. A trailing '=' with no right-hand value fails immediately with SyntaxError. Even after fixing '=', 'Print' is capitalized and would trigger NameError because Python is case-sensitive (print is lowercase).",
              note: "Syntax errors prevent the entire file from running; logic errors run silently with wrong results."
            }
          ],
          output: "  File \"cap03_logic_vs_syntax.py\", line 2\n    Print(5) + 2 =\n                  ^\nSyntaxError: invalid syntax"
        }
      ]
    },
    {
      id: "nested-for-table",
      tabLabel: "Multiplication Table (for)",
      moduleId: "2",
      badge: "Module 2 · Ch. 11",
      title: "Nested for Loops — Multiplication Table (0 to 10)",
      subtitle: "Trace how an outer loop drives an inner loop to generate structured multiplication rows using range().",
      fileName: "cap11_multiplication_table.py",
      scenarios: [
        {
          id: "default",
          label: "Run Table",
          isError: false,
          lines: [
            {
              code: "for factor in range(2, 4):",
              title: "Outer loop controls the current table header",
              explain: "range(2, 4) yields 2, then 3 (stop value 4 is exclusive). On the first pass, factor is bound to 2.",
              note: "In the full book example, range(0, 11) builds every table from 0x0 up to 10x10."
            },
            {
              code: "    print(f'--- Table of {factor} ---')",
              title: "Indented block runs once per outer step",
              explain: "Four spaces of indentation mark this line inside the outer loop body.",
              note: null
            },
            {
              code: "    for mult in range(1, 4):",
              title: "Inner loop completes all iterations per outer step",
              explain: "For each single value of factor, mult iterates through 1, 2, and 3 completely before factor advances.",
              note: "Total executions = outer_count x inner_count (2 x 3 = 6 lines)."
            },
            {
              code: "        product = factor * mult",
              title: "8 spaces = inside inner loop",
              explain: "Evaluates the product for the current (factor, mult) pair and assigns it to product.",
              note: null
            },
            {
              code: "        print(f'{factor} x {mult} = {product}')",
              title: "Formatted row output",
              explain: "Displays the calculation for the current step before returning control to the inner for header.",
              note: null
            }
          ],
          output: "--- Table of 2 ---\n2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n--- Table of 3 ---\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9"
        }
      ]
    },
    {
      id: "lifo-and-dicts",
      tabLabel: "LIFO Stack & Dicts",
      moduleId: "3",
      badge: "Module 3 · Ch. 13–14",
      title: "LIFO Stack & Nested Dictionaries",
      subtitle: "Combine mutable lists acting as Last-In-First-Out paper stacks with structured dictionary records.",
      fileName: "cap13_14_stack_and_dict.py",
      scenarios: [
        {
          id: "default",
          label: "Trace Memory",
          isError: false,
          lines: [
            {
              code: "paper_stack = []",
              title: "Initialize an empty list as a LIFO stack",
              explain: "Lists are ordered and mutable in-place, making the end of the list ideal as the 'top' of a stack.",
              note: "LIFO = Last In, First Out — just like placing and removing sheets on a desk stack."
            },
            {
              code: "paper_stack.append('Doc 1')",
              title: "Push first item onto the top",
              explain: ".append() adds 'Doc 1' at index 0. Stack size is now 1.",
              note: null
            },
            {
              code: "paper_stack.append('Doc 2')",
              title: "Push second item onto the top",
              explain: "'Doc 2' becomes the newest element at the top (index -1). Stack: ['Doc 1', 'Doc 2'].",
              note: null
            },
            {
              code: "last_doc = paper_stack.pop()",
              title: "Pop removes and returns the top item",
              explain: ".pop() with no arguments removes 'Doc 2' from the end in O(1) time and returns it to last_doc.",
              note: "Calling .pop() on an empty list raises IndexError — check if paper_stack: first!"
            },
            {
              code: "learner = {'name': 'Fernando', 'skills': ['Python']}",
              title: "Dictionary with nested mutable list",
              explain: "Dictionaries map unique keys ('name', 'skills') to values, including complex structures like lists.",
              note: null
            },
            {
              code: "learner['skills'].append('OOP')",
              title: "Mutating a list stored inside a dictionary",
              explain: "learner['skills'] resolves to the inner list object in memory, and .append('OOP') mutates it in place.",
              note: "Use learner.get('phone', 'Not registered') for safe lookup without KeyError."
            },
            {
              code: "print(f'Popped: {last_doc} | Skills: {learner[\"skills\"]}')",
              title: "Inspect final stack and dictionary state",
              explain: "Verifies that 'Doc 2' left the stack and 'OOP' was added to the nested skills list.",
              note: null
            }
          ],
          output: "Popped: Doc 2 | Skills: ['Python', 'OOP']"
        }
      ]
    },
    {
      id: "sales-package",
      tabLabel: "sales Package",
      moduleId: "4",
      badge: "Module 4 · Ch. 20",
      title: "Modular Packages (sales/price_calc.py) & __main__",
      subtitle: "Organize reusable modules into package directories, use selective aliases, and guard direct script execution.",
      fileName: "index.py  (imports sales/price_calc.py)",
      scenarios: [
        {
          id: "default",
          label: "Import & Run",
          isError: false,
          lines: [
            {
              code: "import sys",
              title: "Load sys module to inspect import search paths",
              explain: "Python searches the current directory, PYTHONPATH, and standard/site packages listed in sys.path.",
              note: null
            },
            {
              code: "from sales.price_calc import increase_price as apply_markup",
              title: "Selective package import with alias",
              explain: "Locates the sales/ package folder (__init__.py), opens price_calc.py, imports increase_price, and binds it locally as apply_markup.",
              note: "Aliases prevent name collisions and make domain call sites self-documenting."
            },
            {
              code: "def run_quote(base: float, pct: float) -> float:",
              title: "Reusable business function",
              explain: "Encapsulates package logic inside a clean, testable function with type hints.",
              note: null
            },
            {
              code: "    return apply_markup(base, pct)",
              title: "Delegate calculation to package helper",
              explain: "Calls increase_price(100.0, 15.0) inside sales/price_calc.py and returns 115.0.",
              note: null
            },
            {
              code: "if __name__ == '__main__':",
              title: "The __main__ execution guard",
              explain: "True ONLY when running index.py directly. When imported by another module or pytest, __name__ equals the module path, skipping CLI prints.",
              note: "Essential rule across all modules in this repository so imports never trigger blocking side effects."
            },
            {
              code: "    print(f'New price: ${run_quote(100.0, 15.0):.2f} | Paths: {len(sys.path)}')",
              title: "Protected CLI entrypoint output",
              explain: "Formats the adjusted currency price to two decimal places and reports sys.path length.",
              note: null
            }
          ],
          output: "New price: $115.00 | Paths: 6"
        }
      ]
    },
    {
      id: "oop-inheritance",
      tabLabel: "Cars -> Gol / Corsa",
      moduleId: "5",
      badge: "Module 5 · Ch. 21",
      title: "Inheritance & Polymorphism (Cars → Gol / Corsa)",
      subtitle: "Extend the Cars superclass with super().__init__(), override methods, and review the book's classic __int__ errata fix.",
      fileName: "04_inheritance_and_polymorphism.py",
      scenarios: [
        {
          id: "default",
          label: "Run Fleet",
          isError: false,
          lines: [
            {
              code: "class Cars:",
              title: "Base class (superclass) blueprint in PascalCase",
              explain: "Defines shared state and behavior for all cars. Every Python class implicitly inherits from object.",
              note: "PEP 8 reserves PascalCase for classes and snake_case for functions/methods."
            },
            {
              code: "    def __init__(self, name: str, color: str, base_daily_rate: float = 100.0):",
              title: "Initializer sets instance attributes via self",
              explain: "Runs automatically after __new__ allocates the object. Notice it is __init__ (double underscore + init), never __int__.",
              note: "Errata tip: older printings of the book had a typo '__int__' in Corsa — '__int__' is for int(obj), while '__init__' initializes instances!"
            },
            {
              code: "        self.name, self.color, self.base_daily_rate = name, color, base_daily_rate",
              title: "Bind attributes to instance __dict__",
              explain: "Stores name, color, and base_daily_rate uniquely inside each created car instance.",
              note: null
            },
            {
              code: "    def calculate_daily_rate(self, days: int) -> float:",
              title: "Base polymorphic interface",
              explain: "Provides the default calculation formula reused or specialized by subclasses.",
              note: null
            },
            {
              code: "        return round(self.base_daily_rate * days, 2)",
              title: "Compute base rental cost",
              explain: "Multiplies the instance rate by days and rounds to two decimal places.",
              note: null
            },
            {
              code: "class Corsa(Cars):",
              title: "Subclass inheriting from Cars",
              explain: "Corsa inherits __init__ and methods from Cars and appears before Cars in Corsa.__mro__.",
              note: null
            },
            {
              code: "    def __init__(self, name: str, color: str, doors: int = 4):",
              title: "Subclass initializer adding doors",
              explain: "Accepts base attributes plus subclass-specific configuration.",
              note: null
            },
            {
              code: "        super().__init__(name, color, base_daily_rate=120.0)",
              title: "Delegate shared setup to Cars via super()",
              explain: "Avoids duplicating self.name and self.color assignments by invoking the parent initializer cleanly.",
              note: null
            },
            {
              code: "        self.doors = doors",
              title: "Attach subclass-only state",
              explain: "Adds doors to this Corsa instance.",
              note: null
            },
            {
              code: "    def calculate_daily_rate(self, days: int) -> float:",
              title: "Polymorphic override",
              explain: "Redefines calculate_daily_rate while preserving the exact same method signature as Cars.",
              note: null
            },
            {
              code: "        total = super().calculate_daily_rate(days)",
              title: "Reuse parent math before extending",
              explain: "Calls Cars.calculate_daily_rate(self, days) instead of duplicating base_daily_rate * days.",
              note: null
            },
            {
              code: "        return round(total * 0.95 if days >= 5 else total, 2)",
              title: "Apply 5% multi-day discount",
              explain: "For 5+ days, applies a 5% discount automatically while callers treat all cars uniformly.",
              note: null
            },
            {
              code: "fleet = [Cars('Standard Model', 'Black'), Corsa('Corsa Classic', 'Silver')]",
              title: "Polymorphic collection",
              explain: "Holds both base and subclass objects under one common interface.",
              note: null
            },
            {
              code: "for car in fleet: print(f'{car.name}: ${car.calculate_daily_rate(5):.2f}')",
              title: "Dynamic dispatch at runtime",
              explain: "Python resolves car.calculate_daily_rate(5) per object class: Standard Model pays $500.00, Corsa Classic receives 5% off ($570.00).",
              note: null
            }
          ],
          output: "Standard Model: $500.00\nCorsa Classic: $570.00"
        }
      ]
    },
    {
      id: "safe-try-except",
      tabLabel: "try / except / else / finally",
      moduleId: "4",
      badge: "Module 4 · Ch. 22",
      title: "Safe Exception Pattern: try / except / else / finally",
      subtitle: "Avoid the p. 213 book trap where finally references variables that failed to initialize inside try.",
      fileName: "cap22_safe_exceptions.py",
      scenarios: [
        {
          id: "valid",
          label: "Valid Input ('10', '5')",
          isError: false,
          lines: [
            {
              code: "def safe_add(raw_a: str, raw_b: str) -> dict:",
              title: "Pure function wrapping risky parsing",
              explain: "Encapsulates conversion and exception handling so callers receive structured results without crashes.",
              note: null
            },
            {
              code: "    result, error = None, None",
              title: "Pre-initialize state outside try",
              explain: "Ensures variables referenced later always exist even if an exception occurs early.",
              note: null
            },
            {
              code: "    try:",
              title: "Guard only the risky lines",
              explain: "Keep try blocks minimal so you never accidentally swallow unrelated exceptions.",
              note: null
            },
            {
              code: "        num1 = int(raw_a); num2 = int(raw_b)",
              title: "Attempt integer conversion",
              explain: "For ('10', '5'), both int() calls succeed and execution skips the except block.",
              note: null
            },
            {
              code: "    except ValueError as exc:",
              title: "Catch specific conversion errors",
              explain: "Naming ValueError explicitly avoids hiding unexpected bugs like KeyboardInterrupt or ZeroDivisionError.",
              note: null
            },
            {
              code: "        error = f'Invalid integer: {exc}'",
              title: "Record clean user-facing error",
              explain: "Skipped when try succeeds.",
              note: null
            },
            {
              code: "    else:",
              title: "else runs ONLY when try succeeded",
              explain: "Now num1 and num2 are guaranteed to exist, so computing num1 + num2 here can never cause a NameError!",
              note: "In p. 213 of the book, num1 + num2 sat inside finally — moving it to else makes the pattern 100% crash-proof."
            },
            {
              code: "        result = num1 + num2",
              title: "Safe sum computed in else",
              explain: "Binds 15 to result.",
              note: null
            },
            {
              code: "    finally:",
              title: "finally ALWAYS runs — success or failure",
              explain: "Ideal for closing files/connections or setting cleanup flags without touching num1 or num2.",
              note: null
            },
            {
              code: "        cleaned_up = True",
              title: "Guaranteed cleanup flag",
              explain: "Runs regardless of whether except or else executed.",
              note: null
            },
            {
              code: "    return {'ok': error is None, 'result': result, 'error': error, 'cleaned_up': cleaned_up}",
              title: "Return predictable status dictionary",
              explain: "Callers inspect 'ok' without risking uncaught tracebacks.",
              note: null
            }
          ],
          output: "{'ok': True, 'result': 15, 'error': None, 'cleaned_up': True}"
        },
        {
          id: "invalid",
          label: "Invalid Input ('abc', '5')",
          isError: true,
          lines: [
            {
              code: "def safe_add(raw_a: str, raw_b: str) -> dict:",
              title: "Called with ('abc', '5')",
              explain: "Traces the failure path step by step.",
              note: null
            },
            {
              code: "    result, error = None, None",
              title: "Defaults protect downstream return",
              explain: "result starts as None.",
              note: null
            },
            {
              code: "    try:",
              title: "Enter protected conversion block",
              explain: "Starts monitoring for exceptions.",
              note: null
            },
            {
              code: "        num1 = int(raw_a); num2 = int(raw_b)",
              title: "int('abc') raises ValueError immediately",
              explain: "Execution halts at int('abc') — num1 and num2 are NEVER created, and control jumps straight to except ValueError.",
              note: null
            },
            {
              code: "    except ValueError as exc:",
              title: "Matched ValueError handler catches failure",
              explain: "Binds the exception details to exc so the program recovers gracefully.",
              note: null
            },
            {
              code: "        error = f'Invalid integer: {exc}'",
              title: "Captures diagnostic message",
              explain: "Sets error to \"Invalid integer: invalid literal for int() with base 10: 'abc'\".",
              note: null
            },
            {
              code: "    else:",
              title: "else is SKIPPED on exception",
              explain: "Because try failed, Python skips else completely — preventing any NameError on missing num1/num2.",
              note: "This solves the p. 213 NameError trap cleanly."
            },
            {
              code: "        result = num1 + num2",
              title: "Skipped safely",
              explain: "Not executed when an exception occurred.",
              note: null
            },
            {
              code: "    finally:",
              title: "finally STILL runs after except",
              explain: "Executes cleanup unconditionally even after catching ValueError.",
              note: null
            },
            {
              code: "        cleaned_up = True",
              title: "Cleanup confirmed",
              explain: "cleaned_up becomes True without referencing num1 or num2.",
              note: null
            },
            {
              code: "    return {'ok': error is None, 'result': result, 'error': error, 'cleaned_up': cleaned_up}",
              title: "Graceful structured error returned",
              explain: "Program stays alive and returns full context.",
              note: null
            }
          ],
          output: "{'ok': False, 'result': None, 'error': \"Invalid integer: invalid literal for int() with base 10: 'abc'\", 'cleaned_up': True}"
        }
      ]
    }
  ];

  /* ------------------------------------------------------------------------
     3. Theme Persistence & Header Controls
     ------------------------------------------------------------------------ */

  const THEME_STORAGE_KEY = "pyzero-theme";

  function readStoredTheme() {
    try {
      const saved = window.localStorage.getItem(THEME_STORAGE_KEY);
      if (saved === "dark" || saved === "light") {
        return saved;
      }
    } catch (_err) {
      // Storage may be blocked in strict sandboxed contexts; default safely.
    }
    return "dark";
  }

  function saveTheme(theme) {
    try {
      window.localStorage.setItem(THEME_STORAGE_KEY, theme);
    } catch (_err) {
      // Ignore storage errors gracefully.
    }
  }

  function createSvgIcon(type) {
    const svgNS = "http://www.w3.org/2000/svg";
    const svg = document.createElementNS(svgNS, "svg");
    svg.setAttribute("width", "16");
    svg.setAttribute("height", "16");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", "2");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");

    if (type === "sun") {
      const circle = document.createElementNS(svgNS, "circle");
      circle.setAttribute("cx", "12");
      circle.setAttribute("cy", "12");
      circle.setAttribute("r", "4");
      svg.appendChild(circle);

      const rays = [
        "M12 2v2", "M12 20v2", "M4.93 4.93l1.41 1.41", "M17.66 17.66l1.41 1.41",
        "M2 12h2", "M20 12h2", "M6.34 17.66l-1.41 1.41", "M19.07 4.93l-1.41 1.41"
      ];
      rays.forEach(function (d) {
        const path = document.createElementNS(svgNS, "path");
        path.setAttribute("d", d);
        svg.appendChild(path);
      });
    } else {
      const path = document.createElementNS(svgNS, "path");
      path.setAttribute("d", "M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z");
      svg.appendChild(path);
    }
    return svg;
  }

  function applyTheme(theme) {
    const root = document.documentElement;
    root.setAttribute("data-theme", theme);

    const toggleBtn = document.getElementById("themeToggle");
    const themeIcon = document.getElementById("themeIcon");
    const themeLabel = document.getElementById("themeLabel");
    if (!toggleBtn || !themeIcon || !themeLabel) {
      return;
    }

    const isLight = theme === "light";
    toggleBtn.setAttribute("aria-pressed", String(isLight));
    toggleBtn.setAttribute("aria-label", isLight ? "Switch to dark theme" : "Switch to light theme");
    themeLabel.textContent = isLight ? "Dark" : "Light";
    themeIcon.replaceChildren(createSvgIcon(isLight ? "moon" : "sun"));
  }

  function setupNavigationAndTheme() {
    applyTheme(readStoredTheme());

    const themeToggle = document.getElementById("themeToggle");
    if (themeToggle) {
      themeToggle.addEventListener("click", function () {
        const current = document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark";
        const next = current === "light" ? "dark" : "light";
        applyTheme(next);
        saveTheme(next);
      });
    }

    const menuToggle = document.getElementById("menuToggle");
    const mainNav = document.getElementById("mainNav");
    if (menuToggle && mainNav) {
      menuToggle.addEventListener("click", function () {
        const open = mainNav.classList.toggle("is-open");
        menuToggle.setAttribute("aria-expanded", String(open));
      });

      mainNav.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", function () {
          mainNav.classList.remove("is-open");
          menuToggle.setAttribute("aria-expanded", "false");
        });
      });
    }
  }

  /* ------------------------------------------------------------------------
     4. Safe DOM Helper & Python Tokenizer
     ------------------------------------------------------------------------ */

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) {
      node.className = className;
    }
    if (typeof text === "string") {
      node.textContent = text;
    }
    return node;
  }

  const PY_KEYWORDS = new Set([
    "False", "None", "True", "and", "as", "assert", "async", "await",
    "break", "class", "continue", "def", "del", "elif", "else", "except",
    "finally", "for", "from", "global", "if", "import", "in", "is",
    "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try",
    "while", "with", "yield"
  ]);

  const PY_BUILTINS = new Set([
    "print", "input", "int", "float", "str", "list", "dict", "tuple", "set",
    "len", "range", "round", "super", "type", "dir", "help", "isinstance",
    "setattr", "getattr", "hasattr", "delattr", "ValueError", "NameError",
    "TypeError", "SyntaxError", "IndexError"
  ]);

  function renderHighlightedLine(container, code) {
    // Lightweight single-pass lexer building span text nodes safely (no innerHTML).
    const tokenRegex = /(#.*$)|('(?:\\.|[^'\\])*'|"(?:\\.|[^"\\])*")|(\b\d+(?:\.\d+)?\b)|(\b[A-Za-z_][A-Za-z0-9_]*\b)/gm;
    let lastIndex = 0;
    let match;

    while ((match = tokenRegex.exec(code)) !== null) {
      if (match.index > lastIndex) {
        container.appendChild(document.createTextNode(code.slice(lastIndex, match.index)));
      }
      const full = match[0];
      let cls = "";
      if (match[1]) {
        cls = "tok-cmt";
      } else if (match[2]) {
        cls = "tok-str";
      } else if (match[3]) {
        cls = "tok-num";
      } else if (match[4]) {
        if (PY_KEYWORDS.has(full)) {
          cls = "tok-kw";
        } else if (full === "self") {
          cls = "tok-self";
        } else if (PY_BUILTINS.has(full)) {
          cls = "tok-fn";
        } else if (/^[A-Z][A-Za-z0-9_]*$/.test(full)) {
          cls = "tok-cls";
        }
      }

      if (cls) {
        container.appendChild(el("span", cls, full));
      } else {
        container.appendChild(document.createTextNode(full));
      }
      lastIndex = tokenRegex.lastIndex;
    }

    if (lastIndex < code.length) {
      container.appendChild(document.createTextNode(code.slice(lastIndex)));
    }
  }

  /* ------------------------------------------------------------------------
     5. Interactive 5-Module & 23-Chapter Track
     ------------------------------------------------------------------------ */

  const trackState = {
    activeModule: "all",
    query: ""
  };

  function padChapter(num) {
    return num < 10 ? "0" + num : String(num);
  }

  function renderModuleBanner() {
    const banner = document.getElementById("moduleBanner");
    if (!banner) {
      return;
    }

    if (trackState.activeModule === "all") {
      banner.hidden = true;
      banner.replaceChildren();
      return;
    }

    const mod = MODULES[trackState.activeModule];
    if (!mod) {
      banner.hidden = true;
      return;
    }

    const info = el("div");
    info.appendChild(el("h3", "", mod.name + " (" + mod.chaptersRange + ")"));
    info.appendChild(el("p", "", mod.summary));

    const bannerLinks = el("div", "arch-actions");
    const lessonBtn = el("a", "btn btn-sm btn-primary", "Open Module Lesson →");
    lessonBtn.href = mod.readme;
    const exercisesBtn = el("a", "btn btn-sm btn-outline", "Open Exercises");
    exercisesBtn.href = mod.exercises;
    bannerLinks.appendChild(lessonBtn);
    bannerLinks.appendChild(exercisesBtn);

    banner.replaceChildren(info, bannerLinks);
    banner.hidden = false;
  }

  function renderChapters() {
    const grid = document.getElementById("chaptersGrid");
    const countEl = document.getElementById("trackCount");
    const emptyEl = document.getElementById("emptyTrackState");
    if (!grid || !countEl || !emptyEl) {
      return;
    }

    const q = trackState.query.trim().toLowerCase();
    const filtered = CHAPTERS.filter(function (ch) {
      const modMatch = trackState.activeModule === "all" || ch.module === trackState.activeModule;
      if (!modMatch) {
        return false;
      }
      if (!q) {
        return true;
      }
      const haystack = [
        "ch", String(ch.num), padChapter(ch.num),
        ch.title, ch.description, ch.keywords.join(" "),
        MODULES[ch.module].name
      ].join(" ").toLowerCase();
      return haystack.includes(q);
    });

    countEl.textContent = "Showing " + filtered.length + " of " + CHAPTERS.length + " chapters";
    renderModuleBanner();

    if (filtered.length === 0) {
      grid.replaceChildren();
      emptyEl.hidden = false;
      return;
    }

    emptyEl.hidden = true;
    const fragment = document.createDocumentFragment();

    filtered.forEach(function (ch) {
      const mod = MODULES[ch.module];
      const card = el("article", "chapter-card");

      const body = el("div");
      const top = el("div", "chapter-top");
      top.appendChild(el("span", "ch-badge", "Ch. " + padChapter(ch.num)));
      top.appendChild(el("span", "mod-tag", "Module " + ch.module));
      body.appendChild(top);

      body.appendChild(el("h3", "", ch.title));
      body.appendChild(el("p", "chapter-desc", ch.description));

      const kwWrap = el("div", "keyword-list");
      ch.keywords.forEach(function (kw) {
        kwWrap.appendChild(el("span", "kw-chip", kw));
      });
      body.appendChild(kwWrap);
      card.appendChild(body);

      const actions = el("div", "chapter-actions");
      const linksGroup = el("div", "chapter-link-group");
      const lessonLink = el("a", "chapter-link", "Lesson");
      lessonLink.href = mod.readme;
      const exercisesLink = el("a", "chapter-link", "Exercises");
      exercisesLink.href = mod.exercises;
      linksGroup.appendChild(lessonLink);
      linksGroup.appendChild(document.createTextNode(" · "));
      linksGroup.appendChild(exercisesLink);
      actions.appendChild(linksGroup);

      if (ch.labId) {
        const jumpBtn = el("button", "lab-jump-btn", "Open in Lab");
        jumpBtn.type = "button";
        jumpBtn.addEventListener("click", function () {
          selectLabExample(ch.labId);
          const labEl = document.getElementById("lab");
          if (labEl) {
            labEl.scrollIntoView({ behavior: "smooth" });
          }
        });
        actions.appendChild(jumpBtn);
      }

      card.appendChild(actions);
      fragment.appendChild(card);
    });

    grid.replaceChildren(fragment);
  }

  function setupTrackControls() {
    const tabs = document.querySelectorAll("#moduleTabs .tab-btn");
    const searchInput = document.getElementById("chapterSearch");
    const clearBtn = document.getElementById("clearSearch");
    const resetBtn = document.getElementById("resetTrackFilters");

    tabs.forEach(function (btn) {
      btn.addEventListener("click", function () {
        tabs.forEach(function (other) {
          other.classList.remove("is-active");
          other.setAttribute("aria-selected", "false");
        });
        btn.classList.add("is-active");
        btn.setAttribute("aria-selected", "true");
        trackState.activeModule = btn.dataset.module || "all";
        renderChapters();
      });
    });

    if (searchInput && clearBtn) {
      searchInput.addEventListener("input", function () {
        trackState.query = searchInput.value;
        clearBtn.hidden = trackState.query.length === 0;
        renderChapters();
      });

      clearBtn.addEventListener("click", function () {
        searchInput.value = "";
        trackState.query = "";
        clearBtn.hidden = true;
        renderChapters();
        searchInput.focus();
      });
    }

    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        trackState.activeModule = "all";
        trackState.query = "";
        if (searchInput) {
          searchInput.value = "";
        }
        if (clearBtn) {
          clearBtn.hidden = true;
        }
        tabs.forEach(function (tab) {
          const isAll = tab.dataset.module === "all";
          tab.classList.toggle("is-active", isAll);
          tab.setAttribute("aria-selected", String(isAll));
        });
        renderChapters();
      });
    }

    renderChapters();
  }

  /* ------------------------------------------------------------------------
     6. Interactive Reverse Engineering Laboratory
     ------------------------------------------------------------------------ */

  const labState = {
    exampleIndex: 0,
    scenarioIndex: 0,
    lineIndex: 0,
    showAllLines: false
  };

  function getActiveScenario() {
    const ex = LAB_EXAMPLES[labState.exampleIndex];
    return ex.scenarios[labState.scenarioIndex] || ex.scenarios[0];
  }

  function selectLabExample(exampleId) {
    const idx = LAB_EXAMPLES.findIndex(function (ex) {
      return ex.id === exampleId;
    });
    if (idx !== -1) {
      labState.exampleIndex = idx;
      labState.scenarioIndex = 0;
      labState.lineIndex = 0;
      renderLab();
    }
  }

  function renderLabSelector() {
    const selector = document.getElementById("labSelector");
    if (!selector) {
      return;
    }

    const fragment = document.createDocumentFragment();
    LAB_EXAMPLES.forEach(function (ex, idx) {
      const btn = el("button", "lab-pill", ex.tabLabel);
      btn.type = "button";
      btn.setAttribute("role", "tab");
      const active = idx === labState.exampleIndex;
      btn.classList.toggle("is-active", active);
      btn.setAttribute("aria-selected", String(active));
      btn.addEventListener("click", function () {
        labState.exampleIndex = idx;
        labState.scenarioIndex = 0;
        labState.lineIndex = 0;
        renderLab();
      });
      fragment.appendChild(btn);
    });
    selector.replaceChildren(fragment);
  }

  function renderLabScenarios(example) {
    const wrap = document.getElementById("labScenarios");
    if (!wrap) {
      return;
    }

    if (example.scenarios.length <= 1) {
      wrap.hidden = true;
      wrap.replaceChildren();
      return;
    }

    wrap.hidden = false;
    const fragment = document.createDocumentFragment();
    example.scenarios.forEach(function (sc, idx) {
      const btn = el("button", "scenario-btn", sc.label);
      btn.type = "button";
      btn.classList.toggle("is-active", idx === labState.scenarioIndex);
      btn.addEventListener("click", function () {
        labState.scenarioIndex = idx;
        labState.lineIndex = 0;
        renderLab();
      });
      fragment.appendChild(btn);
    });
    wrap.replaceChildren(fragment);
  }

  function renderLabExplanation(scenario) {
    const container = document.getElementById("labExplanation");
    const lineTag = document.getElementById("labLineTag");
    if (!container || !lineTag) {
      return;
    }

    const line = scenario.lines[labState.lineIndex] || scenario.lines[0];
    lineTag.textContent = labState.showAllLines
      ? "All " + scenario.lines.length + " Lines"
      : "Line " + (labState.lineIndex + 1);

    if (labState.showAllLines) {
      const ul = el("ul", "breakdown-list");
      scenario.lines.forEach(function (item, idx) {
        const li = el("li", idx === labState.lineIndex ? "is-current" : "");
        li.appendChild(el("span", "breakdown-line-tag", "L" + (idx + 1)));
        li.appendChild(el("strong", "", item.title + ": "));
        li.appendChild(document.createTextNode(item.explain));
        ul.appendChild(li);
      });
      container.replaceChildren(ul);
      return;
    }

    const box = el("div", "analysis-spotlight");
    box.appendChild(el("strong", "", line.title));
    box.appendChild(el("p", "", line.explain));
    if (line.note) {
      box.appendChild(el("div", "analysis-note", "Note: " + line.note));
    }
    container.replaceChildren(box);
  }

  function renderLab() {
    const ex = LAB_EXAMPLES[labState.exampleIndex];
    const scenario = getActiveScenario();
    if (labState.lineIndex >= scenario.lines.length) {
      labState.lineIndex = 0;
    }

    renderLabSelector();
    renderLabScenarios(ex);

    const badge = document.getElementById("labModuleBadge");
    const title = document.getElementById("labExampleTitle");
    const subtitle = document.getElementById("labExampleSubtitle");
    const fileName = document.getElementById("labFileName");
    const codeLines = document.getElementById("labCodeLines");
    const stepCounter = document.getElementById("labStepCounter");
    const prevBtn = document.getElementById("labPrevLine");
    const nextBtn = document.getElementById("labNextLine");
    const outStatus = document.getElementById("labOutputStatus");
    const outPre = document.getElementById("labOutputPre");
    const modLink = document.getElementById("labModuleLink");

    if (badge) badge.textContent = ex.badge;
    if (title) title.textContent = ex.title;
    if (subtitle) subtitle.textContent = ex.subtitle;
    if (fileName) fileName.textContent = ex.fileName;

    if (codeLines) {
      const frag = document.createDocumentFragment();
      scenario.lines.forEach(function (item, idx) {
        const btn = el("button", "code-line-btn");
        btn.type = "button";
        btn.setAttribute("role", "option");
        const selected = idx === labState.lineIndex;
        btn.classList.toggle("is-selected", selected);
        btn.setAttribute("aria-selected", String(selected));
        btn.appendChild(el("span", "line-num", String(idx + 1)));

        const textSpan = el("span", "line-text");
        renderHighlightedLine(textSpan, item.code);
        btn.appendChild(textSpan);

        btn.addEventListener("click", function () {
          labState.lineIndex = idx;
          renderLab();
        });
        frag.appendChild(btn);
      });
      codeLines.replaceChildren(frag);
    }

    if (stepCounter) {
      stepCounter.textContent = "Line " + (labState.lineIndex + 1) + " of " + scenario.lines.length;
    }
    if (prevBtn) {
      prevBtn.disabled = labState.lineIndex === 0;
    }
    if (nextBtn) {
      nextBtn.disabled = labState.lineIndex >= scenario.lines.length - 1;
    }

    renderLabExplanation(scenario);

    if (outStatus) {
      outStatus.textContent = scenario.isError ? "Traceback / Error" : "Exit 0";
      outStatus.classList.toggle("is-error", Boolean(scenario.isError));
    }
    if (outPre) {
      outPre.textContent = scenario.output;
    }
    if (modLink && MODULES[ex.moduleId]) {
      modLink.href = MODULES[ex.moduleId].readme;
      modLink.textContent = "Open " + MODULES[ex.moduleId].name + " →";
    }
  }

  function setupLabControls() {
    const prevBtn = document.getElementById("labPrevLine");
    const nextBtn = document.getElementById("labNextLine");
    const modeBtn = document.getElementById("labModeToggle");
    const copyBtn = document.getElementById("labCopyBtn");

    if (prevBtn) {
      prevBtn.addEventListener("click", function () {
        if (labState.lineIndex > 0) {
          labState.lineIndex -= 1;
          renderLab();
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener("click", function () {
        const scenario = getActiveScenario();
        if (labState.lineIndex < scenario.lines.length - 1) {
          labState.lineIndex += 1;
          renderLab();
        }
      });
    }

    if (modeBtn) {
      modeBtn.addEventListener("click", function () {
        labState.showAllLines = !labState.showAllLines;
        modeBtn.setAttribute("aria-pressed", String(labState.showAllLines));
        modeBtn.textContent = labState.showAllLines ? "Single Line Focus" : "Show All Lines";
        renderLabExplanation(getActiveScenario());
      });
    }

    if (copyBtn) {
      copyBtn.addEventListener("click", function () {
        const scenario = getActiveScenario();
        const codeText = scenario.lines.map(function (item) {
          return item.code;
        }).join("\n");
        copyToClipboard(codeText, copyBtn, "Copy Code");
      });
    }

    renderLab();
  }

  /* ------------------------------------------------------------------------
     7. Clipboard Utility (with file:// fallback)
     ------------------------------------------------------------------------ */

  function copyToClipboard(text, button, defaultLabel) {
    function markCopied() {
      button.textContent = "Copied!";
      button.classList.add("is-copied");
      window.setTimeout(function () {
        button.textContent = defaultLabel;
        button.classList.remove("is-copied");
      }, 1800);
    }

    if (navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
      navigator.clipboard.writeText(text).then(markCopied).catch(function () {
        fallbackCopy(text);
        markCopied();
      });
      return;
    }

    fallbackCopy(text);
    markCopied();
  }

  function fallbackCopy(text) {
    const area = document.createElement("textarea");
    area.value = text;
    area.setAttribute("readonly", "");
    area.style.position = "fixed";
    area.style.opacity = "0";
    document.body.appendChild(area);
    area.select();
    try {
      document.execCommand("copy");
    } catch (_err) {
      // Clipboard blocked in current context; fail silently without breaking UI.
    }
    document.body.removeChild(area);
  }

  function setupCommandCopyButtons() {
    document.querySelectorAll(".copy-cmd-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        const targetId = btn.dataset.copyTarget;
        const targetEl = targetId ? document.getElementById(targetId) : null;
        if (!targetEl) {
          return;
        }
        copyToClipboard(targetEl.textContent || "", btn, "Copy");
      });
    });
  }

  /* ------------------------------------------------------------------------
     8. Initialize Application
     ------------------------------------------------------------------------ */

  document.addEventListener("DOMContentLoaded", function () {
    setupNavigationAndTheme();
    setupTrackControls();
    setupLabControls();
    setupCommandCopyButtons();
  });
})();
