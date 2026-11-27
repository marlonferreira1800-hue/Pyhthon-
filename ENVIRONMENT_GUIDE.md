# Programming Environment Guide (Chapter 2)

This guide accompanies **Chapter 2 — Programming Environment** of *"Python do ZERO à Programação Orientada a Objetos"* (Updated and Expanded Edition, by **Fernando Feltrin**) and prepares your computer to study every module, run all example scripts, explore the final project, and execute the automated test suite.

> Quick links: [Course Portal](README.md) · [Complete Syllabus](SYLLABUS.md) · [Module 1 — Fundamentals](modules/module_01_fundamentals/README.md)

---

## 1. Backend vs. Frontend: Where Does Python Fit?

Modern web and software applications are typically split into two main layers:

| Layer | Core Responsibility | Common Technologies | Python's Role |
| :--- | :--- | :--- | :--- |
| **Frontend** | The visual interface users interact with directly (buttons, screens, forms, layouts, animations). | HTML, CSS, JavaScript, TypeScript, web/mobile UI frameworks. | Does not run natively as the primary browser UI language, though it serves templates and feeds data to frontends via APIs. |
| **Backend** | Business logic, data processing, authentication, database integration, automation pipelines, and AI/ML models. | **Python** (FastAPI, Django, Flask), Java, C#, Go, Node.js, SQL. | **Primary strength**: Python powers web backends, data engineering, automation, scientific computing, and machine learning. |

---

## 2. Language Levels: High-Level, Low-Level, and Machine Language

To understand why Python boosts productivity without sacrificing capability, compare the three classic abstraction layers between human thought and CPU hardware:

```text
[ Human / Logic ]
        │
        ▼
1. High-Level Language (Python, Java, C#)
   Readable syntax close to English and math; portable across operating systems.
   Example: print("Hello World!!!")
        │
        ▼  (Compiled to bytecode .pyc -> Python Virtual Machine / PVM)
2. Low-Level Language (Assembly and intermediate Bytecode)
   Instructions tied closely to hardware registers, memory addresses, or VM opcodes.
   Example: MOV AX, 1  /  LOAD_CONST, CALL_FUNCTION
        │
        ▼  (Final translation into electrical signals)
3. Machine Language (Binary: 0s and 1s)
   Pure sequences of bits executed directly by the CPU's transistors.
   Example: 10110000 01100001
```

### Why this matters in practice
- **Python is a high-level interpreted language** (in the standard **CPython** runtime, `.py` source files are compiled transparently into bytecode and executed by the Python Virtual Machine).
- You can express logic in a few readable lines rather than managing raw pointers or memory registers by hand, letting you focus on problem-solving, data structures, and object-oriented design.

---

## 3. Installing Python 3 (Step by Step)

This course targets **Python 3.10+** (validated on **Python 3.10.11**).

### Windows
1. Visit the official downloads page at [python.org/downloads](https://www.python.org/downloads/) and download the Python 3.10+ installer for Windows.
2. Run the installer and, **on the very first screen**, make sure to check:
   - `[x] Add python.exe to PATH` *(allows running `python` from any terminal window)*.
3. Click **Install Now** and finish setup.
4. Open **PowerShell** or **Command Prompt (CMD)** and verify your installation:
   ```powershell
   python --version
   pip --version
   ```

### Linux (Ubuntu / Debian / Fedora)
Most Linux distributions include Python 3 or provide it via the system package manager:
```bash
# Check installed version
python3 --version

# Ubuntu / Debian
sudo apt update && sudo apt install -y python3 python3-pip python3-venv

# Fedora
sudo dnf install -y python3 python3-pip
```

### macOS
1. Download the official `.pkg` installer from [python.org/downloads](https://www.python.org/downloads/) or install with Homebrew:
   ```bash
   brew install python@3.10
   ```
2. Verify in Terminal:
   ```bash
   python3 --version
   ```

### Optional Virtual Environment (`venv`)
All course modules and the final project rely strictly on the **Python standard library** (plus `pytest` for running automated tests). Using a virtual environment keeps your tools isolated:

```powershell
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pytest
```

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
```

---

## 4. Main IDEs and Development Environments (Chapter 2)

An **IDE (Integrated Development Environment)** combines a code editor with syntax highlighting, autocompletion, a debugger, and an integrated terminal. Chapter 2 highlights the core tools used across the Python ecosystem:

### 1. IDLE (Built into Python)
- **What it is:** The lightweight editor and interactive shell bundled with official Python installers.
- **When to use it:** Quick one-line experiments in the REPL (`>>>`), early Chapter 3–8 exercises, and checking built-in functions such as `print()`, `type()`, and `dir()`.

### 2. Visual Studio Code (VS Code)
- **What it is:** A fast, free, extensible code editor by Microsoft.
- **Setup for this course:**
  1. Install VS Code and add Microsoft's official **Python** extension.
  2. Open the repository root folder (`curso-python-do-zero-a-poo/` or your cloned repository directory).
  3. Choose your Python interpreter (`Ctrl+Shift+P` -> *Python: Select Interpreter*).
  4. Use the integrated terminal (`Ctrl+'`) to run scripts, `course_cli.py`, and `pytest`.
- **When to use it:** Great all-around editor for navigating modules, running examples, and working on the multi-file Final Project.

### 3. PyCharm (JetBrains)
- **What it is:** A dedicated, full-featured Python IDE (the **Community Edition** is free and open-source).
- **Strengths:** Deep static code inspection, safe symbol refactoring across packages (Chapter 20), visual virtual-environment management, and a step-by-step debugger well suited for OOP (Module 5).
- **When to use it:** Ideal when working with larger multi-module projects and object hierarchies.

### 4. Anaconda & Jupyter Notebook / JupyterLab
- **What they are:**
  - **Anaconda:** A distribution focused on Data Science, Data Engineering, and Machine Learning, bundling the `conda` package/environment manager and popular scientific libraries.
  - **Jupyter Notebook / JupyterLab:** A browser-based interactive workspace organized into **cells**, mixing executable Python code, immediate outputs, tables, plots, and Markdown notes.
- **When to use them:** Great for exploratory prototyping, inspecting datasets, and step-by-step experimentation with lists, dictionaries, sets, and formatting.

> **Quick recommendation:** If you are starting from scratch, **VS Code** or **PyCharm Community** paired with the **terminal** gives you a smooth, industry-standard workflow from Chapter 1 through OOP.

---

## 5. Practical Terminal Usage for This Course

Running scripts from the terminal prevents UI lock-ins, makes automated testing effortless, and builds real-world command-line fluency.

### Essential course navigation commands

```powershell
# 1. Move into the course directory
cd curso-python-do-zero-a-poo

# 2. List all modules and inspect course status
python course_cli.py --list

# 3. Inspect a specific module's files, examples, and commands (1 to 5)
python course_cli.py --module 1

# 4. Verify that every required course file is present
python course_cli.py --check
```

### Running the Final Project and automated tests

```powershell
# Run the Final Project in non-blocking automated demo mode
python final_project/main.py --demo

# Run the Final Project in interactive menu mode
python final_project/main.py

# Run the full automated pytest suite
python -m pytest -v
```

### Windows UTF-8 Console Tip
If an older Windows console (`cmd.exe` or Windows PowerShell) renders accented characters or ANSI colors strangely, enable UTF-8 mode for your session:

```powershell
# PowerShell: force Python UTF-8 mode for the current session
$env:PYTHONUTF8 = "1"
```

```cmd
:: CMD: switch active code page to UTF-8
chcp 65001
```

---

## Next Steps

Once your environment is ready, explore the [Complete Syllabus](SYLLABUS.md) to trace all 23 chapters of the book, or jump directly into [Module 1 — Fundamentals, Logic & First Commands](modules/module_01_fundamentals/README.md).
