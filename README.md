# APC Practicals — TY Semester 5

A collection of my Python practical experiments for **Third Year, Semester 5 (APC)**, plus a `training` folder of extra problem-solving practice. The experiments start with core Python (data types, loops, strings), move through functions, modules, file handling and OOP, and finish with text processing, regex and the data-science stack (NumPy, Pandas, Matplotlib).

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Experiments](https://img.shields.io/badge/Experiments-10-success)

---

## Table of Contents

- [Repository Structure](#repository-structure)
- [Experiments at a Glance](#experiments-at-a-glance)
- [Experiment Details](#experiment-details)
- [Training Folder](#training-folder)
- [Getting Started](#getting-started)
- [How to Run](#how-to-run)
- [Notes](#notes)
- [Author](#author)

---

## Repository Structure

```
APC-PRAC-TY-S5/
├── EXP1/    Data types & operations
├── EXP2/    Loops & pattern printing
├── EXP3/    String handling programs
├── EXP4/    Functions: student grade manager
├── EXP5/    Functions, lambda, arrays, modules & packages
│   └── mypackage/
├── EXP6/    File & directory handling
├── EXP7/    NLP text processing (NLTK)
├── EXP8/    OOP: constructors, destructors, inheritance
├── EXP9/    Exception handling & regular expressions
├── EXP10/   NumPy, Pandas & Matplotlib
└── training/  Extra DSA / problem-solving practice
```

---

## Experiments at a Glance

| # | Topic | Main file(s) |
|---|-------|--------------|
| 1 | Python data types and operations | `EXP1/EXP1.py` |
| 2 | `for` / `while` loops and pattern printing | `EXP2/EXP2.py` |
| 3 | String manipulation programs | `EXP3/EXP3.py` |
| 4 | Student grade manager using lists and functions | `EXP4/EXP4.py` |
| 5 | Functions, lambda, arrays, modules and packages | `EXP5/*.py` |
| 6 | File handling (text, binary, images) and directories | `EXP6/EXP6.py` |
| 7 | Tokenization, stop-word removal, stemming | `EXP7/textprecessing.py` |
| 8 | Constructors, destructors, inheritance, access modifiers | `EXP8/*.py` |
| 9 | Exception handling and regular expressions | `EXP9/*.py` |
| 10 | NumPy, Pandas and Matplotlib | `EXP10/*.py` |

---

## Experiment Details

### EXP1 — Data Types and Operations
A single script that walks through Python's built-in types with formatted output: integers, floats, strings, booleans, lists, tuples, dictionaries and sets. It also covers comparison operators, type conversion and mixed-type collections.

### EXP2 — Loops and Patterns
Practice with `for` and `while` loops:
- Printing numbers, even/odd numbers and squares up to *n*
- Sum of 1 to *n*, sum of odd/even numbers, reverse counting
- Series sum using factorials and Fibonacci generation
- Alphabet and number patterns (triangles, inverted triangles)

### EXP3 — String Handling
Common string problems solved without relying on shortcuts where possible:
- Length without `len()`, reversing, palindrome check
- Counting vowels, consonants, digits, spaces and special characters
- Upper/lowercase counts, character replacement, space removal
- ASCII values, word count, longest/shortest word, title-casing
- Anagram check, duplicate removal preserving order, substring check, word frequency
- Password validation (length, uppercase, lowercase, digit, special character)

### EXP4 — Student Grade Manager
A small program built from plain functions and two parallel lists (`student`, `grades`):
- `addlist()`, `update()`, `dele()` to manage records
- `avaragegrd()` for the class average
- `extream()` for highest and lowest grades

### EXP5 — Functions, Lambda, Arrays, Modules and Packages

| File | Covers |
|------|--------|
| `func.py` | Parameters, return values, default and keyword arguments, nested calls, recursion |
| `lamfunc.py` | Lambda functions, conditional lambdas, `map()` and `filter()` |
| `array.py` | Lists as arrays, indexing, slicing, sorting, 2D arrays, the `array` module |
| `math_operations.py`, `calculator.py` | Custom modules |
| `main.py` | Import styles (`import`, `from … import`, `*`, aliases) and built-ins: `math`, `random`, `os` |
| `mypackage/` + `packages.py` | Building and importing a package |

### EXP6 — File and Directory Handling
- File modes: `x`, `w`, `a`, `r`, `r+`, `w+`, `a+`
- `read()`, `readline()`, `readlines()`, iterating over a file, `with open`
- `seek()` and `tell()`
- Binary read, write and append; copying an image (`download.jpg` → `copy.jpg`)
- `os` operations: exists, remove, rename, `mkdir`, `makedirs`

### EXP7 — Text Processing with NLTK
- Word and sentence tokenization
- Stop-word removal
- Stemming with `PorterStemmer`, including combined stemming and stop-word filtering

### EXP8 — Object-Oriented Programming
- `const-destr.py`: `__init__` with parameters and defaults, class variables, `__del__`
- `inheritance.py`: single, multiple, multilevel, hierarchical and hybrid inheritance; public, protected and private members; method overriding; `super()`; constructors in inheritance

### EXP9 — Exceptions and Regular Expressions
- `exceptionhandling.py`: `try` / `except` / `else` / `finally`, `ZeroDivisionError`, `ValueError`, `TypeError`, `raise`, and a user-defined `AgeError`
- `regularexp.py`: `compile`, `search`, `match`, `fullmatch`, `findall`, `finditer`, plus email, phone number and password validators

### EXP10 — Data Science Libraries
- `numpyop.py`: 1D, 2D and 3D arrays; shape, dimensions, slicing, axis-wise sums, element-wise operations and transpose
- `pandasop.py`: Series creation and filtering, reading `sample.csv` into a DataFrame
- `matplot.py`: a 2×2 figure with line, bar, scatter and histogram plots

---

## Training Folder

Extra practice on algorithmic problem solving:

| File | Contents |
|------|----------|
| `two pointer.py` | Two-pointer technique (pair with target sum, ticket budget), sliding window, prefix sums |
| `aaye.py` | Anagram check, linear search problems, book allocation (binary search on the answer) |
| `new.py` | Duplicate detection using `set` |
| `test.py` | Scratch work |

---

## Getting Started

### Prerequisites
- Python 3.8 or newer (developed with Python 3.14)
- `pip`

### Clone the repository
```bash
git clone https://github.com/Notrealatharv/APC-PRAC-TY-S5.git
cd APC-PRAC-TY-S5
```

### Install dependencies
Only EXP7 and EXP10 need third-party packages:
```bash
pip install nltk numpy pandas matplotlib
```

---

## How to Run

Run each script from inside its own experiment folder, because several of them use relative paths and local imports.

```bash
cd EXP1
python EXP1.py
```

```bash
# EXP5 uses local modules, so run from within the folder
cd EXP5
python main.py
python packages.py
```

```bash
# EXP10
cd EXP10
python numpyop.py
python pandasop.py
python matplot.py
```

---

## Notes

- **Commented code:** In `EXP2`, `EXP3`, `EXP6` and parts of `training`, programs are commented out so each one can be tried individually. Uncomment the block you want to run.
- **NLTK data:** `EXP7` downloads the required NLTK resources (`punkt_tab`, `punkt`, `stopwords`) on first run, so the first run needs an internet connection.
- **File handling:** Running `EXP6` blocks creates, modifies and deletes files and folders in the current directory. Use the experiment folder and keep an eye on what you uncomment.
- **Interactive input:** Several scripts in EXP3, EXP9 and `array.py` ask for input via `input()`.

---

## Author

**Atharv**
GitHub: [@Notrealatharv](https://github.com/Notrealatharv)
