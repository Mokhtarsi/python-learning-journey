
#
## =====> Mini project to paractice <====
## ===> Mini Project : (User Access Manager ) That can manager the Users

Users = {}

Admin_username = "Admin"
Admin_password = "Admin123"
current_user = None
is_admin = False


def admin_login():
    """Handle admin authentication"""
    global current_user, is_admin

    print("\n --- Admin Login ---")
    username = input("Enter the name of the Admin : ")
    password = input("Enter the password :")
    
    ## Trying  thinking if this match or not .
    while True:
        if username == Admin_username and password == Admin_password :
            current_user = username 
            is_admin = True
            print("Admin Login successful!")
            return True
        else:
            print("Invalid Admin Credentials!")
            return False
def change_admin_Credentials():
    """Allow admin to change login credenrials"""
    global Admin_username, Admin_password

    print("\n--- Change Admin Currentials ---")
    current_pass = input("Enter current admin password: ") 

    if current_pass == Admin_password:
        new_username = input("Enter new admin username: ")
        new_password = input("Enter new admin password: ")

        Admin_username = new_username 
        Admin_password = new_password

        print("Admin credentials updated Seccessfully!")

    else:
        print("Incorrect current password!")

while True:
    print(f"""
    \n=== User Access Manager === 
    Current User: {current_user if current_user else 'Guest'}
    Permission Level: {'Admin' if is_admin else 'Guest'}
    Options: 
            [Login] - Admin login
            [View] - View all users
            [Add] - Add a new user (Admin Only)
            [Remove] - Remove a user (Admin Only)
            [ChangeCred] - Change admin credentials (Admin Only)
            [Logout] - Logout Admin
            [Exit or Quit] - Exit or Quit the program
    """)

    Choice = input("Choose one: ").lower()
    if Choice == "login" :
        if is_admin:
            print("You are already logged in as admin!")

        else:
            admin_login()

    elif Choice == "view":
        if not Users:
            print("No Users found. ")

        else:
            print("\n--- Users List ----")
            for Name, Role in Users.items():
                print(f"{Name} is a {Role}.")

    elif Choice == "add":
        if is_admin :
            Name = input("Enter user name: ")
            Role = input("Enter user Role: ")
            Users[Name] = Role
            print(f"{Name} added as {Role}.")
        else:
            print("Permission denied! Admin Login Required.")
    elif Choice == "remove":
        if is_admin:
            Name = input("Enter the user naem that you want to remove : ")
            if Name in Users:
                del Users[Name]
                print(f"{Name} removed. ")
            else:
                print("The User That you entered is not Found.")
        else:
            print("Permission denied! Admin login required.")

    elif Choice == "changecred":
        if is_admin:
            change_admin_Credentials()
        else:
            print("Permission denied! Admin login required.")
    

    elif Choice == "logout" :
        if is_admin:
            current_user = None
            is_admin = False
            print("Admin logged out successfully!")

        else:
            print("No admin user is currently logged in.")

    elif Choice == "exit" or Choice == "quit":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")          
                
                
                
                
