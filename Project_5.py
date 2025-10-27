

#### ====> Caesar Cipher Code <=====

def encrypt(text, shift):
    result = ""
    for each_chara in text:
        if each_chara.isalpha():
            rule = ord('A') if each_chara.isupper() else ord('a')
            result += chr((ord(each_chara) -rule + shift ) %26 + rule)


        else:
            result += each_chara
    return result



def decrypt(text, shift):
    return encrypt(text, -shift)


def brute_force_decrypt(text):
    print("/n --- Brute force Results ---")
    for shift in range (1, 26):
        decrypted_text = decrypt(text, shift)
        print(f"shift {shift:2}: {decrypted_text}")

print("---- Welcome ! this program can encrypt & and decrypt text and Brute force decrypt ---")
while True:
    print("""
          \nOptions:
          [e] Encrypt text
          [d] Decrypt text [known shift)
          [b] brute force decrypt (unknown shift)
          [q] Quit
          """)
    
    choice = input("\nChosee an option: ").lower()

    if choice == "q":
        print("Goodbye!")
        break

    if choice not in ['e', 'd', 'b']:
        print("Invalid character !. Please try again.")
        continue 
    text = input("Enter your text: ")

    if choice == "e":
        shift = int(input("Enter shift value (1 - 25): "))
        print("\nEncrypted text:", encrypt(text, shift))

    elif choice == "d":
        shift = int(input("Enter shift value (1 - 25): "))
        print("\nDecrypted text:", decrypt(text, shift))

    elif choice == "b":
        brute_force_decrypt(text)

    