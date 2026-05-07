import random 
import string

current_password = ""
password_history = []
def password_generator(length , use_symbols ):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    password = []

    for i in range(length):
        password.append(random.choice(characters))

    password = ''.join(password)
    return password
def check_strength(password):
    strength = 0
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if len(password) < 6:
        return "weak"
    elif len(password) < 10:
        return "medium"
    else:
        return "strong"

while True:
    print("---welcome to password history game---")
    choice = input("1. Generate a new password \n2. View current password \n3. Check password strength \n4. View password history \n5. Exit \nPlease select an operation: ")
    if choice == "1":
        user_length = int(input("Enter the desired length of your password: "))
        use_symbols = input("Do you want to include symbols in your password? (yes/no): ").lower()
        if use_symbols == "yes":
            use_symbols = True
        else:
            use_symbols = False
        current_password = password_generator(user_length, use_symbols)
        password_history.append(current_password)
        print("Your new password is: " , current_password)

    elif choice == "2":
        if current_password:
            print("your current password is:" , current_password)
        else:
            print("you have not generated a password yet. Please select option 1 to generate a new password.")
        
    elif choice == "3":
        if current_password:
            strength = check_strength(current_password)
            print(f"your password strength is: {strength}")
        else:
            print("you have not generated a password yet. Please select option 1 to generate a new password.")
    
    elif choice == "4":
        if password_history:
            for index,pwd in enumerate(password_history):
                print(f"{index + 1}. {pwd}")
        else:
            print("you have not generated any password yet. Please select option 1 to generate a new password.")
    elif choice == "5":
        print("Thank you for using the password history game. Goodbye!")
        break
