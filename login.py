def collect_username(users):
    username = None 
    while username is None:
        try:
            username_input = input("Enter your username: ").strip()
            username = validate_username(username_input)
            if username is None: 
                continue
            else: 
                for user in users:
                    if user['username'] != username:
                        username = None
                    else:
                        return username
            print("Username not found. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
        except KeyboardInterrupt:
            print("Invalid input. Please try again.")
    return username


def collect_password(username, users):
    password = None
    while password is None:
        try:
            password_input = input("Enter your password:").strip()
            password = validate_password(password_input)
            if password is None:
                continue
            else:
                for user in users:
                    if user['username'] == username and user['password'] == password:
                        return password
                    else: 
                        password = None
                if password is None: 
                    print("Incorrect password. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
        except KeyboardInterrupt:
            print("Invalid input. Please try again.")
    return password 

def validate_username(username):
    if not username: 
        print("Username cannot be empty. Please try again:")
        username = None 
    return username
    
            
def validate_password(password):
    if not password: 
        print("Password cannot be empty. Please try again:")
        password = None
    return password

def login(users):
    print("Welcome to the Vacations Manager System!\n"
          "Please enter your credentials to log in.\n")
    username = collect_username(users)
    password = collect_password(username, users)
    print("Login successful! Access granted to the Vacations Manager System.")
    return True
