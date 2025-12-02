import csv 
    
def load_data(path):
    users = []
    invalid_rows = 0
    print(f"Loading data from: {path}\n"
          f"{users}")
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)

            if header is None:
                print("The CSV file is empty.")
                return users

            expected_header = ['username','password','role']
            normalized_header = [col.strip().lower() for col in header]
        
           
            if normalized_header != expected_header:
                print("Invalid header on file.")
                return users

            for row in reader:
                
                if not row or all(col.strip() == "" for col in row):
                    continue

                if len(row) != 3:
                    invalid_rows += 1
                    continue

                try:
                    username = row[0].strip()
                    password = row[1].strip()
                    role = row[2].strip()

                    users.append(
                        {
                            'username': username,
                            'password': password,
                            'role': role
                        }
                    )

                except ValueError:
                    invalid_rows += 1

        if not users:
            print("No valid users were found in the file.")
            return users
    except FileNotFoundError:
        print("The specified file was not found.")
    except UnicodeDecodeError:
        print("Encoding error. Make sure it is a valid CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred while loading the file: {e}")
    print(f"Inventory loaded from: {path}")
    print(f"Users loaded: {len(users)}")
    print(f"Invalid rows skipped: {invalid_rows}")
    return users