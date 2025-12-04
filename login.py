from utils import load_users


def validate_username(username: str):
    if not username:
        print("Username cannot be empty. Please try again.")
        return None
    return username


def validate_password(password: str):
    if not password:
        print("Password cannot be empty. Please try again.")
        return None
    return password


def collect_username(users):
    username = None
    while username is None:
        try:
            username_input = input("Enter your username: ").strip()
            username = validate_username(username_input)
            if username is None:
                continue

            found = any(u['username'] == username for u in users)
            if found:
                return username
            else:
                print("Username not found. Please try again.")
                username = None

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
        except KeyboardInterrupt:
            print("Invalid input. Please try again.")
    return username


def collect_password(username, users):
    password = None
    while password is None:
        try:
            password_input = input("Enter your password: ").strip()
            password = validate_password(password_input)
            if password is None:
                continue

    
            matched_user = None
            for user in users:
                if user['username'] == username and user['password'] == password:
                    matched_user = user
                    break

            if matched_user is None:
                print("Incorrect password. Please try again.")
                password = None
            else:
                
                if matched_user['role'].lower() != "admin":
                    print("You do not have administrator privileges. Access denied.")
                    return None
                return password

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
        except KeyboardInterrupt:
            print("Invalid input. Please try again.")
    return password


def login(users):
    """
    Retorna True solo si el login es correcto y el usuario es ADMIN.
    """
    print("Welcome to the Vacations Manager System!\n"
          "Please enter your credentials to log in.\n")

    username = collect_username(users)
    if username is None:
        return False

    password = collect_password(username, users)
    if password is None:
        return False

    print("Login successful! Access granted to the Vacations Manager System.")
    return True
