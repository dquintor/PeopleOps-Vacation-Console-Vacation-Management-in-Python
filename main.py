from employees import (
    load_data_employees,
    save_data_employees,
    collect_employee_data,
    build_employee_record,
    add_employee,
    view_all_employees,
    get_employee,
)
from login import login
from utils import load_users, validate_menu_option
from vacations import (
    load_vacations,
    save_vacations,
    create_vacation_request,
    approve_or_reject_request,
    show_employee_history,
)
from reports import export_approved_report

EMPLOYEE_FILE = "employees.csv"
USERS_FILE = "users.csv"
VACATIONS_FILE = "vacations.csv"


def main_menu():
    print("\nMain Menu - Vacations Manager System\n"
          "\n1. Add Employee\n"
          "2. View all Employees\n"
          "3. Search Employee\n"
          "4. Add Vacation Request\n"
          "5. Approve/Deny vacation requests\n"
          "6. View requests history by employee\n"
          "7. Export data to CSV by month and year\n"
          "8. Exit\n")
    option = validate_menu_option(1, 8)
    return option


def main():
    users = load_users(USERS_FILE)
    employees = load_data_employees(EMPLOYEE_FILE)
    vacations = load_vacations(VACATIONS_FILE)

    sesion = login(users)

    if sesion is True:
        print("\nAccessing the Vacations Manager System...\n")
        while True:
            option = main_menu()

            if option == 1:
    
                data = collect_employee_data(employees)
                if data is not None:
                    employee_id, full_name, position, department, hire_date = data
                    employee = build_employee_record(
                        employee_id,
                        full_name,
                        position,
                        department,
                        hire_date
                    )
                    add_employee(employees, employee)
                    save_data_employees(EMPLOYEE_FILE, employees)
                    print("Employee added successfully.")

            elif option == 2:
                view_all_employees(employees)

            elif option == 3:
                emp_id = input("Enter Employee ID to search: ").strip()
                emp = get_employee(employees, emp_id)
                if emp:
                    print("\nEmployee found:")
                    print(f"ID: {emp['employee_id']}")
                    print(f"Name: {emp['full_name']}")
                    print(f"Position: {emp['position']}")
                    print(f"Department: {emp['department']}")
                    print(f"Hire date: {emp['hire_date']}")
                else:
                    print("Employee not found.")

            elif option == 4:
                
                create_vacation_request(employees, vacations)
                save_vacations(VACATIONS_FILE, vacations)

            elif option == 5:
               
                approve_or_reject_request(vacations)
                save_vacations(VACATIONS_FILE, vacations)

            elif option == 6:
                
                show_employee_history(vacations, employees)

            elif option == 7:
                
                export_approved_report(vacations, employees)

            elif option == 8:
                print("Exiting system...")
                break

    else:
        print("Invalid credentials. Access denied.")


if __name__ == "__main__":
    main()
