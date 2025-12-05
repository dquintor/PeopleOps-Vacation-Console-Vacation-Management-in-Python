# PeopleOps Vacation Console

Console-based Python application for managing employee vacation days based on company rules.

**Author:** Daniela Quinto Rios  
**Clan:** Turing  

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Core Concepts and Execution Flow](#core-concepts-and-execution-flow)  
4. [Architecture and Modules](#architecture-and-modules)  
    - [main.py](#mainpy)  
    - [employees.py](#employeespy)  
    - [login.py](#loginpy)  
    - [vacations.py](#vacationspy)  
    - [reports.py](#reportspy)  
    - [utils.py](#utilspy)  
5. [Vacation Rules](#vacation-rules)  
6. [Data Files (CSV Inputs)](#data-files-csv-inputs)  
    - [employees.csv](#employeescsv)  
    - [users.csv](#userscsv)  
    - [vacations.csv](#vacationscsv)  
7. [How to Run](#how-to-run)  
8. [Design Rationale](#design-rationale)  
9. [Limitations and Future Improvements](#limitations-and-future-improvements)  

---

## Overview

PeopleOps Vacation Console is a small console-based Python application for managing employee vacation days.

The application:

- Reads employee, user, and vacation data from CSV files.
- Applies a set of vacation rules (accrual rate, minimum time worked, exclusion of Sundays).
- Calculates available vacation days for employees.
- Supports simple operations such as vacation registration and report generation.

The system is organized in layers:

1. Data layer (CSV handling and lookups)  
2. Time layer (date and time calculations)  
3. Rules layer (vacation accrual logic)  
4. Interface layer (console interaction and menus)  

---

## Features

- Load employee records from CSV files.
- Validate employee identity by ID.
- Calculate months worked based on hire date.
- Compute eligible vacation days using company rules:
  - 1.5 days per month worked.
  - Minimum of 6 months required to start accruing vacation.
  - Sundays do not count as vacation days when calculating days taken.
- Track vacations taken and approval status.
- Generate CSV-based reports (for example, monthly or yearly vacation summaries).
- Simple login and role-based access using a `users.csv` file.

---

## Core Concepts and Execution Flow

At a high level, the application follows this pipeline:

1. **Collect employee data**  
   The program loads a CSV file with employee records (ID, name, department, hire date).

2. **Read user input from the console**  
   The user logs in and selects actions from the menu.

3. **Validate the employee**  
   Checks if the employee exists; if not, prints an error.

4. **Calculate eligible vacation days**  
   Uses:
   - Months worked
   - Accrual rule: 1.5 days per month
   - Minimum eligibility: 6 months
   - Exclusion of Sundays

5. **Show results**  
   Displays:
   - Months worked  
   - Eligible days  
   - Warnings if under 6 months  

### Full Execution Flow

```
main.py
 ├─ load employees → employees.load_csv()
 ├─ login flow → login.validate()
 ├─ display menu
 ├─ vacation calculation:
 │     ├─ find employee → employees.find_employee()
 │     ├─ compute months worked → utils.date helpers
 │     ├─ apply rules → vacations.calculate()
 │     └─ show results
 ├─ report generation → reports.export_csv()
 └─ end
```

---

## Architecture and Modules

### `main.py`

Entry point of the application.

Responsibilities:
- Launch console interface
- Handle login and roles
- Navigate the main menu
- Trigger vacation calculations, lookups, and reports

---

### `employees.py`

Manages employee records stored in `employees.csv`.

Responsibilities:
- Load employee data
- Look up employees by ID
- Expose fields such as hire date, name, and department

---

### `login.py`

Handles user authentication.

Responsibilities:
- Load credentials from `users.csv`
- Validate username and password
- Return role for access control

---

### `vacations.py`

Core vacation logic module.

Responsibilities:
- Load and store vacation records
- Apply business rules:
  - 1.5 days per month
  - Minimum 6 months
  - Exclude Sundays from days taken
- Register new vacation entries
- Compute balances: accrued, taken, remaining

---

### `reports.py`

Generates vacation reports.

Responsibilities:
- Combine employee and vacation data
- Produce monthly or yearly summaries
- Export CSV-based reports such as `reporte_vacaciones_2025_12.csv`

---

### `utils.py`

Utility helpers shared across modules.

Responsibilities:
- Date operations (e.g., months worked calculation)
- Formatting utilities
- CSV helpers
- Input validation

Example:

```python
months = (current_year - hire_year) * 12 + (current_month - hire_month)
```

---

## Vacation Rules

- **Accrual rate:** 1.5 days per month worked  
- **Minimum eligibility:** 6 months worked  
- **Exclusion of Sundays:** Sundays do not count as vacation days taken  

These rules define how vacation is accrued, used, and calculated.

---

## Data Files (CSV Inputs)

### `employees.csv`

```csv
employee_id,full_name,position,department,hire_date
123,daniela,position,department,2022-12-25
```

### `users.csv`

```csv
username,password,role
daniela,pass123,admin
john,doe456,user
mary,smith789,user
```

### `vacations.csv`

```csv
employee_id,full_name,vacations_start_date,vacations_end_date,total_days_taken,approval_status,month,year
123,daniela,2025-12-20,2026-01-02,12.0,APPROVED,12,2025
```

---

## How to Run

### Requirements

- Python **3.8 or newer**
- All CSV files placed under:

```
PeopleOps-Vacation-Console-Vacation-Management-in-Python/
```

### Run the app

```bash
python PeopleOps-Vacation-Console-Vacation-Management-in-Python/main.py
```

---

## Design Rationale

This architecture ensures:

- Clean separation of responsibilities
- Maintainable and extensible structure
- Ability to switch from CSV to a database with minimal changes
- Easy future additions:
  - GUI  
  - New rules  
  - More reporting features  

---

## Limitations and Future Improvements

- Improve CSV validation  
- Add unit tests  
- Define rounding policies  
- Enhance console UX (argparse, click)  
- Introduce database persistence  

---

