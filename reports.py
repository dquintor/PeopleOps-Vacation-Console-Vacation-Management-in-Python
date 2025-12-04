import csv

REPORT_HEADER = [
    'employee_id',
    'full_name',
    'position',
    'department',
    'vacations_start_date',
    'vacations_end_date',
    'total_days_taken',
    'month',
    'year',
]


def export_approved_report(vacations, employees):
    """
    Exporta a CSV todas las solicitudes APROBADAS de un mes/año dado.
    """
    try:
        month = int(input("Enter month (1-12): ").strip())
        year = int(input("Enter year (e.g. 2025): ").strip())
    except ValueError:
        print("Invalid month or year.")
        return

    if month < 1 or month > 12:
        print("Month must be between 1 and 12.")
        return

    employee_map = {e['employee_id']: e for e in employees}

    filtered = [
        v for v in vacations
        if v['approval_status'].upper() == "APPROVED"
        and v['month'] == month
        and v['year'] == year
    ]

    if not filtered:
        print("No approved vacations found for that period.")
        return

    filename = f"reporte_vacaciones_{year}_{month:02}.csv"

    try:
        with open(filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=REPORT_HEADER)
            writer.writeheader()

            for v in filtered:
                emp = employee_map.get(v['employee_id'])
                position = emp['position'] if emp else ""
                department = emp['department'] if emp else ""

                row = {
                    'employee_id': v['employee_id'],
                    'full_name': v['full_name'],
                    'position': position,
                    'department': department,
                    'vacations_start_date': v['vacations_start_date'],
                    'vacations_end_date': v['vacations_end_date'],
                    'total_days_taken': v['total_days_taken'],
                    'month': v['month'],
                    'year': v['year'],
                }
                writer.writerow(row)

        print(f"Report generated successfully: {filename}")
    except Exception as e:
        print(f"Error while generating report: {e}")
