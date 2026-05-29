
users = {}

MAX_ATTEMPTS = 3

while True:
    print("\n===== LOGIN SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. View Users")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # REGISTER
    if choice == "1":
        username = input("Enter username: ")

        if username in users:
            print("Username already exists!")
        else:
            password = input("Enter password: ")
            users[username] = password
            print("Registration successful!")

    # LOGIN
    elif choice == "2":
        username = input("Enter username: ")

        if username not in users:
            print("User not found!")
        else:
            attempts = 0

            while attempts < MAX_ATTEMPTS:
                password = input("Enter password: ")

                if users[username] == password:
                    print("Login successful!")
                    break
                else:
                    attempts += 1
                    remaining = MAX_ATTEMPTS - attempts
                    print("Wrong password!")
                    
                    if remaining > 0:
                        print("Attempts left:", remaining)

            if attempts == MAX_ATTEMPTS:
                print("Too many failed attempts!")
                print("Login blocked.")

    # VIEW USERS
    elif choice == "3":
        if len(users) == 0:
            print("No registered users.")
        else:
            print("\nRegistered Users:")
            for user in users:
                print(user)

    # EXIT
    elif choice == "4":
        print("Exiting program...")
        break

    # INVALID CHOICE
    else:
        print("Invalid choice! Please try again.")