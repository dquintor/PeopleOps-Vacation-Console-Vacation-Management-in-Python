from login import login
from utils import load_data 

def main():
      users = load_data("users.csv")
      login(users)
      
def main_menu():
      print("Main Menu - Vacations Manager System\n"
            "1. Add Employee\n"
            "2. View all Employees\n"
            "3. Search Employee\n"
            "4. Add Vacation Request\n"
            "5. Approve/Deny vacation requests\n"
            "6. View requests history by employee\n"
            "7. Export data to CSV by motnh and year\n"
            "8. Exit\n")
      
      


if __name__ == "__main__":
    main()


