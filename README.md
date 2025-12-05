# PeopleOps Vacation Console

**Made by:** Daniela Quinto Rios, clan Turing

## Overview

This repository contains a small console-based Python application for managing employee vacation days. The application reads employee data from CSV files, applies company vacation rules, and helps calculate available vacation days and perform simple vacation-related operations.

## General Flow of the Application

The core idea behind the project is simple:

1.  **Collect employee data**\
    The program loads a CSV file containing employee records: ID, name,
    department, hire date, etc.

2.  **Read user input from the console**\
    The user types an employee ID to request a vacation‑days
    calculation.

3.  **Validate the employee**\
    The system checks whether that employee exists in the CSV.

    -   If not found → prints an error\
    -   If found → moves to calculation

4.  **Calculate eligible vacation days**\
    This logic uses:

    -   Months worked\
    -   Rule: *1.5 days per month*\
    -   Rule: *Minimum 6 months*\
    -   Rule: *Sundays do not count*

5.  **Show the results**\
    The console prints:

    -   Total months worked\
    -   Total eligible days\
    -   Warnings (if under 6 months)

------------------------------------------------------------------------

##  How Each Module Contributes to the Flow

### \### `main.py`

-   Entry point of the entire program.
-   Loads the CSV file of employees.
-   Displays the console interface.
-   Reads the user's chosen employee ID.
-   Calls functions from other modules to:
    -   validate employees\
    -   calculate vacation days\
    -   display the result

**Flow:**

    start → load CSV → ask user for ID → validate → calculate → print → end

------------------------------------------------------------------------

### `employee_data.py`

Handles **all data operations**, especially the CSV.

Responsibilities: - Load employees from CSV to a Python list/dict. -
Search for employees by ID. - Validate that the ID exists. - Provide the
employee's hire date when needed.

This module isolates data handling so that the rest of the program does
not worry about CSV parsing.

------------------------------------------------------------------------

### `date_utils.py`

Manages all **date calculations**.

It provides: - Functions to compute months worked between hire date and
today. - Logic that ensures calculations are correct regardless of month
length. - Tools used by the vacation rules module.

Example internal logic:

    months = (current_year - hire_year) * 12 + (current_month - hire_month)

------------------------------------------------------------------------

### `vacation_rules.py`

Contains the **core business logic** of the application.

Implements all syllabus‑required rules: - 1.5 days per month worked -
Minimum 6 months to earn vacation - Remove Sundays from final count

Flow inside this module:

    get months worked
    if months < 6 → return 0
    days = months * 1.5
    remove sundays from the projected vacation period
    return final_days

------------------------------------------------------------------------

## Full Execution Flow (Step-by-Step)

    main.py
     ├─ loads employees from CSV  → employee_data.load_csv()
     ├─ asks user for ID
     ├─ finds the employee       → employee_data.find_employee()
     ├─ gets hire date
     │
     ├─ calculate months worked  → date_utils.calculate_months_worked()
     │
     ├─ apply business rules     → vacation_rules.calculate_vacations()
     │     ├─ check minimum months
     │     ├─ multiply by 1.5 days
     │     ├─ remove sundays
     │     └─ return final count
     │
     └─ display result on console

------------------------------------------------------------------------

## How the Logic Fits Together

Everything works in a **pipeline structure**:

1.  **Data layer**\
    (`employee_data.py`)\
    → Provides employee info.

2.  **Time layer**\
    (`date_utils.py`)\
    → Calculates months worked.

3.  **Rules layer**\
    (`vacation_rules.py`)\
    → Turns months into valid vacation days.

4.  **Interface layer**\
    (`main.py`)\
    → Talks to the user and prints results.

Each module has one job, and the application works because they pass
information to the next one in the chain.

------------------------------------------------------------------------

## Why This Design Works Well

-   Clear **separation of responsibilities**
-   Clean, readable code
-   Easy to update rules without touching the rest of the system
-   Can be expanded later with:
    -   GUI
    -   more employee attributes
    -   extra vacation policies
    -   database storage

------------------------------------------------------------------------



## How to run

1. Ensure you have Python installed (see 'Python version' below).

2. From the repository root, run the main script:

```bash
python PeopleOps-Vacation-Console-Vacation-Management-in-Python/main.py
```

## Python version
Compatible with **Python 3.8 or newer**. Use a modern Python 3 interpreter.

## Required CSV files

The repository includes the following CSV files:

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
- Purpose: Manages employee records stored in employees.csv.
This module reads employee data and provides:
- employee lookup functions
- access to fields like hire date, name, ID, and department
- Other modules (such as vacations and reports) depend on this module to retrieve employee details for calculations.

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/login.py`
- Purpose: Handles the authentication layer of the app.
It loads user credentials from users.csv and validates:
-username
-password
-It provides a simple login function that the main console uses to grant or deny access.
- Contains part of the application logic or helpers.

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/main.py`
- Purpose: 
- Likely the program entry point (runs the console).
This is the entry point of the entire console application.
It launches the PeopleOps Vacation Console, manages the menu flow, and connects user actions with the internal modules.
It handles:
- Login sequence using the login module
- Menu navigation
- Calling employee lookups
- Vacation calculations
- Report generation
Basically, this file is the “controller” that drives the user experience.

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/reports.py`
- Purpose: Creates and exports vacation reports.
It fetches employee data and vacation data to produce output like:
- monthly or full-year vacation summaries
- CSV-based report generation
- It also writes formatted reports such as reporte_vacaciones_2025_12.csv.
This file acts as the “output generator” for the system.

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/utils.py`
- Purpose: 
- Utility/helper functions used across modules.
A helper module with utility functions used across the project.
Typical utilities include:
- date operations
- formatting helpers
- CSV reading/writing shortcuts
- input validation helpers
It’s not business logic by itself, but it supports every other module with shared functionality.

### `PeopleOps-Vacation-Console-Vacation-Management-in-Python/vacations.py`
- Purpose: 
- Contains core vacation calculation logic.
Implements the core vacation calculation logic used by the system.
This is where the business rules live:
- 1.5 vacation days earned per month worked
- Minimum 6 months required to start accruing days
- Sundays are not counted when calculating used vacation days
It also handles:
- loading vacations.csv
- registering new vacation entries
- calculating available vs used vacation time
This is the heart of the PeopleOps logic.

## Rules used to calculate vacations (as implemented / found in code)

- **Accrual rate:** 1.5 days per month worked. 

- **Minimum months worked to start accruing:** 6 months.

- **Sundays do not count as vacation days** when computing days taken.


## Limitations and suggested future improvements 

- **Input validation:** CSV parsing may lack robust validation; consider adding stricter checks for required fields (IDs, hire dates, vacation records).

- **Unit tests:** Add automated tests for accrual calculation, edge cases around Sundays, and minimum-month enforcement.

- **Rounding rules:** Clarify how fractional days are handled (round up/down/half-day policy) and implement consistent rounding.

- **CLI UX:** Improve the console interface to include help text, subcommands, and argument parsing (argparse or click).

- **Persistence:** Add saving of results or integration with a simple database if needed.
