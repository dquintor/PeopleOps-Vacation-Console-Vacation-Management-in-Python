# employees.py
import csv
from datetime import datetime

EMPLOYEE_CSV_HEADER = ['employee_id', 'full_name', 'position', 'department', 'hire_date']
DATE_FORMAT = "%Y-%m-%d" 


def add_employee(employees, employee):
    """
    Agrega un empleado a la lista en memoria.
    NO guarda en CSV, solo en la lista.
    """
    employees.append(employee)
    return employees


def view_all_employees(employees):
    """
    Muestra todos los empleados en formato de tabla simple.
    """
    if not employees:
        print("\nNo hay empleados registrados.\n")
        return

    print("\nListado de empleados:")
    print("-" * 80)
    print(f"{'ID':<10} {'Nombre completo':<25} {'Cargo':<20} {'Área':<15} {'Fecha inicio':<12}")
    print("-" * 80)
    for e in employees:
        print(f"{e['employee_id']:<10} {e['full_name']:<25} {e['position']:<20} {e['department']:<15} {e['hire_date']:<12}")
    print("-" * 80)


def get_employee(employees, employee_id):
    """
    Busca un empleado por ID en la lista.
    Retorna el dict del empleado o None si no existe.
    """
    for e in employees:
        if e['employee_id'] == employee_id:
            return e
    return None


def build_employee_record(employee_id, full_name, position, department, hire_date):
    """
    Construye el registro de empleado en forma de diccionario.
    Valida formato de fecha YYYY-MM-DD (solo para advertir).
    """
    try:
        datetime.strptime(hire_date, DATE_FORMAT)
    except ValueError:
        print("Formato de fecha inválido, se esperaba YYYY-MM-DD. Se guardará tal cual.")

    return {
        'employee_id': employee_id,
        'full_name': full_name,
        'position': position,
        'department': department,
        'hire_date': hire_date,
    }


def collect_employee_data(employees):
    """
    Pide por consola la información del empleado y devuelve
    los campos (employee_id, full_name, position, department, hire_date)
    o None si el ID ya existe.
    """
    employee_id = input("Enter Employee ID: ").strip()
    for e in employees:
        if employee_id == e['employee_id']:
            print(f"Employee with ID {e['employee_id']} already exists.")
            return None

    full_name = input("Enter the employee Full Name: ").strip()
    position = input("Enter the employee Position: ").strip()
    department = input("Enter the employee Department: ").strip()
    hire_date = input("Enter the Hire Date (YYYY-MM-DD): ").strip()
    return employee_id, full_name, position, department, hire_date


def load_data_employees(path):
    """
    Carga los empleados desde un CSV con cabecera:
    employee_id, full_name, position, department, hire_date
    y devuelve una lista de dicts.
    """
    employees = []
    invalid_rows = 0
    print(f"Loading employees from: {path}")

    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)

            if header is None:
                print("The CSV file is empty.")
                return employees

            expected_header = EMPLOYEE_CSV_HEADER
            normalized_header = [col.strip().lower() for col in header]
            expected_normalized = [col.strip().lower() for col in expected_header]

            if normalized_header != expected_normalized:
                print("Invalid header on employees file.")
                print(f"Expected: {expected_header}")
                print(f"Found:    {header}")
                return employees

            for row in reader:
                if not row or all(col.strip() == "" for col in row):
                    continue

                if len(row) != 5:
                    invalid_rows += 1
                    continue

                employee_id = row[0].strip()
                full_name = row[1].strip()
                position = row[2].strip()
                department = row[3].strip()
                hire_date = row[4].strip()

                employees.append(
                    {
                        'employee_id': employee_id,
                        'full_name': full_name,
                        'position': position,
                        'department': department,
                        'hire_date': hire_date,
                    }
                )

        if not employees:
            print("No valid employees were found in the file.")
            return employees

    except FileNotFoundError:
        print("The specified employees file was not found. A new one will be created on save.")
    except UnicodeDecodeError:
        print("Encoding error. Make sure it is a valid CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred while loading employees: {e}")

    print(f"Employees loaded: {len(employees)}")
    print(f"Invalid rows skipped: {invalid_rows}")
    return employees


def save_data_employees(path, employees):
    """
    Guarda la lista de empleados en el CSV, sobrescribiendo el archivo.
    """
    try:
        with open(path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=EMPLOYEE_CSV_HEADER)
            writer.writeheader()
            for e in employees:
                writer.writerow(e)
        print(f"Employees saved to: {path}")
    except Exception as e:
        print(f"Error while saving employees: {e}")
