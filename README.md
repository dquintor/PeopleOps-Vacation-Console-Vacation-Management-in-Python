# PeopleOps Vacation Console

**Made by:** Daniela Quinto Rios, clan Turing

## Overview

This repository contains a small console-based Python application for managing employee vacation days. The application reads employee data from CSV files, applies company vacation rules, and helps calculate available vacation days and perform simple vacation-related operations.

## How it works 
- The program loads one or more CSV files containing employee records and/or vacation requests.
- It computes accrued vacation days according to the rules described below.
- It excludes Sundays from counted vacation days and enforces a minimum months-worked rule for accrual.
- It provides a command-line interface (console) to query and perform operations.

## How to run

1. Ensure you have Python installed (see 'Python version' below).

2. From the repository root (or the extracted directory), run the main script:

```bash
python PeopleOps-Vacation-Console-Vacation-Management-in-Python/main.py
```

## Python version
There is no explicit Python version pinned in the files. The code appears compatible with **Python 3.8 or newer**. Use a modern Python 3 interpreter.

## Required CSV files

The repository includes the following CSV files (names and a brief preview):

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/employees.csv`

Sample:

```
employee_id,  full_name,  position,  department,  hire_date
123, daniela, position, department, 2022-12-25
```


### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/users.csv`

Sample:

```
username, password, role
daniela, pass123, admin
john, doe456, user
mary, smith789, user
```

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/vacations.csv`

Sample:

```
employee_id, full_name, vacations_start_date, vacations_end_date, total_days_taken, approval_status, month, year
123, daniela, 2025-12-20, 2026-01-02, 12.0, APPROVED, 12, 2025
```

## Project structure and purpose of each `.py` file

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/employees.py`
- Short: employees.py
- Purpose: 
- Contains part of the application logic or helpers.

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/login.py`
- Short: (no short description found)
- Purpose: 
- Contains part of the application logic or helpers.

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/main.py`
- Short: (no short description found)
- Purpose: 
- Likely the program entry point (runs the console).

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/reports.py`
- Short: (no short description found)
- Purpose: 
- Contains part of the application logic or helpers.

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/utils.py`
- Short: (no short description found)
- Purpose: 
- Utility/helper functions used across modules.

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/vacations.py`
- Short: vacations.py
- Purpose: 
- Contains core vacation calculation logic.

## Rules used to calculate vacations (as implemented / found in code)

- **Accrual rate:** 1.5 days per month worked. (This rule was requested and searched for in the code; see files: PeopleOps-Vacation-Console-Vacation-Management-in-Python/.git/config, PeopleOps-Vacation-Console-Vacation-Management-in-Python/.git/index, PeopleOps-Vacation-Console-Vacation-Management-in-Python/login.py, PeopleOps-Vacation-Console-Vacation-Management-in-Python/main.py, PeopleOps-Vacation-Console-Vacation-Management-in-Python/reports.py, PeopleOps-Vacation-Console-Vacation-Management-in-Python/vacations.py)

- **Minimum months worked to start accruing:** 6 months.

- **Sundays do not count as vacation days** when computing days taken.


Notes on rule evidence: the codebase contains references to 'vacation' and related keywords in the files listed above; the exact arithmetic implementation (e.g., rounding, prorating partial months) is described in the relevant `.py` files and summarized below.


## Limitations and suggested future improvements 

- **Input validation:** CSV parsing may lack robust validation; consider adding stricter checks for required fields (IDs, hire dates, vacation records).

- **Timezone / date handling:** If the code uses naive date arithmetic, consider using `datetime` with timezone-aware objects or `pendulum` for clarity.

- **Unit tests:** Add automated tests for accrual calculation, edge cases around Sundays, and minimum-month enforcement.

- **Rounding rules:** Clarify how fractional days are handled (round up/down/half-day policy) and implement consistent rounding.

- **CLI UX:** Improve the console interface to include help text, subcommands, and argument parsing (argparse or click).

- **Persistence:** Add saving of results or integration with a simple database if needed.
