### project Password strength checker
## --- Date 2025-10-23
### -- A simple python program that checks if a user's password meets basic security requirement 
### such as length, uppercase,
### lowercase, digits, and space restrictions.


print("=== PASSWORD REQUIREMENTS ===")

while True:
    password = input("Enter Your Password: ")

    if len(password) < 8 :
        print("Your password is Too short. Must be at least 8 characters.")
    elif len(password) > 20:
         print("Your password is too long. Must be 20 characters or less.")
    elif not any(char.isupper() for char in password):
        print("Weak password: Should contain at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        print("Weak password: Should contain at least one lowercase letter.")       
    elif " " in password:
        print("Password cannot contain spaces.")
    elif password.isdigit():
        print("weak password: only numbers.")
    elif password.isalpha():
        print("Weak password: only letters.")
          
    else:
        print("Strong Password accepted.")

        break
