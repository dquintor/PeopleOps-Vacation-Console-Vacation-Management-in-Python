# vacations.py
import csv
from datetime import datetime, timedelta

VACATION_CSV_HEADER = [
    'employee_id',
    'full_name',
    'vacations_start_date',
    'vacations_end_date',
    'total_days_taken',
    'approval_status',
    'month',
    'year',
]

DATE_FORMAT = "%Y-%m-%d"
DAYS_PER_MONTH = 1.5
MIN_MONTHS_FOR_VACATION = 6


def parse_date(date_str: str):
    return datetime.strptime(date_str, DATE_FORMAT).date()


def full_months_between(start_date, end_date):
    """
    Calcula meses completos entre start_date y end_date.
    """
    if end_date < start_date:
        return 0
    years = end_date.year - start_date.year
    months = end_date.month - start_date.month
    total_months = years * 12 + months
    if end_date.day < start_date.day:
        total_months -= 1
    return max(total_months, 0)


def count_days_excluding_sundays(start_date, end_date):
    """
    Cuenta días entre start_date y end_date (inclusive), excluyendo domingos.
    """
    if end_date < start_date:
        return 0

    current = start_date
    days = 0
    while current <= end_date:
        if current.weekday() != 6:  # 6 = Sunday
            days += 1
        current += timedelta(days=1)
    return days


def load_vacations(path: str):
    vacations = []
    invalid_rows = 0
    print(f"Loading vacations from: {path}")

    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)

            if header is None:
                print("The vacations CSV file is empty.")
                return vacations

            expected_header = VACATION_CSV_HEADER
            normalized_header = [col.strip().lower() for col in header]
            expected_normalized = [col.strip().lower() for col in expected_header]

            if normalized_header != expected_normalized:
                print("Invalid header on vacations file.")
                print(f"Expected: {expected_header}")
                print(f"Found:    {header}")
                return vacations

            for row in reader:
                if not row or all(col.strip() == "" for col in row):
                    continue

                if len(row) != len(VACATION_CSV_HEADER):
                    invalid_rows += 1
                    continue

                record = {
                    'employee_id': row[0].strip(),
                    'full_name': row[1].strip(),
                    'vacations_start_date': row[2].strip(),
                    'vacations_end_date': row[3].strip(),
                    'total_days_taken': float(row[4].strip()),
                    'approval_status': row[5].strip(),
                    'month': int(row[6].strip()),
                    'year': int(row[7].strip()),
                }
                vacations.append(record)

    except FileNotFoundError:
        print("The specified vacations file was not found. A new one will be created on save.")
    except UnicodeDecodeError:
        print("Encoding error. Make sure it is a valid CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred while loading vacations: {e}")

    print(f"Vacations records loaded: {len(vacations)}")
    print(f"Invalid rows skipped: {invalid_rows}")
    return vacations


def save_vacations(path: str, vacations):
    try:
        with open(path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=VACATION_CSV_HEADER)
            writer.writeheader()
            for v in vacations:
                writer.writerow(v)
        print(f"Vacations saved to: {path}")
    except Exception as e:
        print(f"Error while saving vacations: {e}")


def calculate_accrued_days(employee, today=None, vacations=None):
    """
    Días acumulados de vacaciones para un empleado:
    meses completos * 1.5 - días ya aprobados.
    """
    if today is None:
        today = datetime.today().date()
    if vacations is None:
        vacations = []

    hire_date = parse_date(employee['hire_date'])
    months = full_months_between(hire_date, today)
    accrued = months * DAYS_PER_MONTH

    # días ya usados en solicitudes APROBADAS
    used = 0
    for v in vacations:
        if v['employee_id'] == employee['employee_id'] and v['approval_status'].upper() == "APPROVED":
            used += float(v['total_days_taken'])

    available = accrued - used
    return max(available, 0), months, used, accrued


def create_vacation_request(employees, vacations):
    """
    Registra una nueva solicitud de vacaciones:
    - Seleccionar empleado
    - Validar >= 6 meses trabajados
    - Calcular días sin domingos
    - Validar balance
    - Guardar en estado PENDING
    """
    if not employees:
        print("No employees registered. Please add employees first.")
        return

    employee_id = input("Enter Employee ID for vacation request: ").strip()
    employee = None
    for e in employees:
        if e['employee_id'] == employee_id:
            employee = e
            break

    if employee is None:
        print("Employee not found.")
        return

    today = datetime.today().date()
    available, months_worked, used, accrued = calculate_accrued_days(employee, today, vacations)

    print(f"\nEmployee: {employee['full_name']}")
    print(f"Months worked: {months_worked}")
    print(f"Accrued days: {accrued:.2f}")
    print(f"Used days: {used:.2f}")
    print(f"Available days: {available:.2f}\n")

    
    if months_worked < MIN_MONTHS_FOR_VACATION:
        print("This employee has less than 6 full months of work. Vacation request is not allowed.")
        return

    start_str = input("Enter vacation START date (YYYY-MM-DD): ").strip()
    end_str = input("Enter vacation END date (YYYY-MM-DD): ").strip()

    try:
        start_date = parse_date(start_str)
        end_date = parse_date(end_str)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    if end_date < start_date:
        print("End date cannot be before start date.")
        return

    days_requested = count_days_excluding_sundays(start_date, end_date)
    print(f"Days requested (excluding Sundays): {days_requested}")

    if days_requested <= 0:
        print("Requested days must be greater than 0.")
        return

    if days_requested > available:
        print("Requested days exceed the available vacation balance.")
        return

    record = {
        'employee_id': employee['employee_id'],
        'full_name': employee['full_name'],
        'vacations_start_date': start_date.strftime(DATE_FORMAT),
        'vacations_end_date': end_date.strftime(DATE_FORMAT),
        'total_days_taken': float(days_requested),
        'approval_status': "PENDING",
        'month': start_date.month,
        'year': start_date.year,
    }

    vacations.append(record)
    print("Vacation request created successfully with status PENDING.")


def list_pending_requests(vacations):
    pending = [v for v in vacations if v['approval_status'].upper() == "PENDING"]
    if not pending:
        print("\nNo pending vacation requests.\n")
        return []

    print("\nPending vacation requests:")
    print("-" * 90)
    for idx, v in enumerate(pending, start=1):
        print(f"{idx}. {v['employee_id']} - {v['full_name']} | "
              f"{v['vacations_start_date']} to {v['vacations_end_date']} | "
              f"Days: {v['total_days_taken']}")
    print("-" * 90)
    return pending


def approve_or_reject_request(vacations):
    pending = list_pending_requests(vacations)
    if not pending:
        return

    try:
        choice = int(input("Select request number to manage (0 to cancel): ").strip())
    except ValueError:
        print("Invalid input.")
        return

    if choice == 0:
        return

    if choice < 1 or choice > len(pending):
        print("Invalid selection.")
        return

    selected = pending[choice - 1]

    print("1. APPROVE")
    print("2. REJECT")
    decision = input("Choose an option: ").strip()

    if decision == "1":
        new_status = "APPROVED"
    elif decision == "2":
        new_status = "REJECTED"
    else:
        print("Invalid option.")
        return

    # actualizar en la lista original de vacations
    for v in vacations:
        if (v['employee_id'] == selected['employee_id'] and
                v['vacations_start_date'] == selected['vacations_start_date'] and
                v['vacations_end_date'] == selected['vacations_end_date'] and
                v['approval_status'].upper() == "PENDING"):
            v['approval_status'] = new_status
            break

    print(f"Request updated to {new_status}.")


def show_employee_history(vacations, employees):
    employee_id = input("Enter Employee ID to view vacation history: ").strip()
    employee = None
    for e in employees:
        if e['employee_id'] == employee_id:
            employee = e
            break

    if employee is None:
        print("Employee not found.")
        return

    history = [v for v in vacations if v['employee_id'] == employee_id]
    if not history:
        print("No vacation requests found for this employee.")
        return

    print(f"\nVacation history for {employee['full_name']} (ID: {employee_id})")
    print("-" * 100)
    for v in history:
        print(f"{v['vacations_start_date']} to {v['vacations_end_date']} | "
              f"Days: {v['total_days_taken']} | "
              f"Status: {v['approval_status']} | "
              f"Month/Year: {v['month']}/{v['year']}")
    print("-" * 100)
