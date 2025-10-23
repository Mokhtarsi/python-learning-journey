# --- Day 2 Project:  bouncer - The Digital Bar Guard --- 
# Date: 2025-10-22

## Asking the user for basic inforamtion 
Name  = str(input("Enter your name: "))
## ---safe input for age ---

while True:
    try:
        Age = int(input("How old are you: "))
        break
    except ValueError:
        print(" No no ,Invalid input. Please enter a number for your age.")

Identity = input("Show your Identity on the screen: ")

print("\n--- Access Decision ---")

###----Case 1 :
if Age > 18 :
    print(f"Hi{Name}, you are an adult!")
    print(f"Welcome in! Your identity is {Identity}.")

### ---Case 2 :

elif Age == 18 :
    print(f"Hi {Name}, you just became an adult!")
    print("""
Before you enter ,There are some rules you should follow if you want to inter in :
          1️⃣ Don't argue about ID or house rules.
          2️⃣ Don't drink on an empty stomach.
          3️⃣ Don't ever drink and drive.
          4️⃣ Don't cause a disturbance or be overly load.
          5️⃣ Don't leave without paying your tab.
          """)
    
    ## -- Ask for agreement
    while True:
        Agreement = input("Do you agree or not , type  Yes👍 or No👎:").strip().lower()
        if  Agreement.lower() == "yes" :
            print("You are in , enjoy your time responsibly!🍾☺️ ")
            break
        elif Agreement.lower() == "no" :
            print("Sorry, you can't enter without agreeing to the rules.")
            break
        else:
            print("Invalid response - please type Yes or No.")

else:
    print(f"Hi! {Name},Sorry sweetheart - you're still a minor.")

    print(f"We can't let you in yet, come back whenn you're older ☺️")
