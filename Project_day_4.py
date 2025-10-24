print("==== Password Strenghth Meter ==== ")

import string ## ==> bringing a toolbox containe all the punctuation symbols like "!@#$%^&*()"
### ==> create a function the takes a password and checkes it 

def check_password(password: str):
    
    
### the basic rules   containe ( lenght and no spaces)
    if len(password) < 6: 
        return False, " Too short! Minimum 6 Characters."
    if len(password) > 20: 
        return False,  "Too long! Maximum 20 characters."
    if " " in password :
        return False,  " No spaces allowed!" 
    

## ==> 

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)


### ==> Security Requirements

    if not (has_upper or has_lower): 
        return False,  "Must contain at least one letter (upper or lower)."

    if not (has_digit or has_symbol):
        return False, "Must contain at least one number or symbol."
    
    return True, "Strong password!"
    
    

## ==>
    
    
while True:
    passwd = input("Enter password (Type 'quit' to exit):")
    if passwd.lower() == "quit":
        print(" Goodbye!")
        break
    
    ok, msg = check_password(passwd)

    print(msg)
    if ok:
        print("Accepted.")
        break
