import csv


def load_users(path: str):
    """
    Carga usuarios desde un CSV con cabecera:
    username,password,role
    """
    users = []
    invalid_rows = 0
    print(f"Loading users from: {path}")
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)

            if header is None:
                print("The CSV file is empty.")
                return users

            expected_header = ['username', 'password', 'role']
            normalized_header = [col.strip().lower() for col in header]
            expected_normalized = [col.strip().lower() for col in expected_header]

            if normalized_header != expected_normalized:
                print("Invalid header on users file.")
                print(f"Expected: {expected_header}")
                print(f"Found:    {header}")
                return users

            for row in reader:
                if not row or all(col.strip() == "" for col in row):
                    continue

                if len(row) != 3:
                    invalid_rows += 1
                    continue

                username = row[0].strip()
                password = row[1].strip()
                role = row[2].strip()

                users.append(
                    {
                        'username': username,
                        'password': password,
                        'role': role,
                    }
                )

        if not users:
            print("No valid users were found in the file.")
            return users

    except FileNotFoundError:
        print("The specified users file was not found.")
    except UnicodeDecodeError:
        print("Encoding error. Make sure it is a valid CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred while loading users: {e}")

    print(f"Users loaded: {len(users)}")
    print(f"Invalid rows skipped: {invalid_rows}")
    return users


def validate_menu_option(min_option: int, max_option: int) -> int:
    """
    Pide una opción de menú entre min_option y max_option (ambos incluidos).
    """
    while True:
        try:
            option = int(input(f"Please select an option ({min_option}-{max_option}): ").strip())
            if option < min_option or option > max_option:
                print(f"Invalid option. Please enter a number between {min_option} and {max_option}.")
            else:
                return option
        except ValueError:
            print("Invalid input. Please enter a valid number.")
