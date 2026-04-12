# Simple Money System (Deposit, Withdraw, Check Balance, Exit)

balance = 1000  # initial balance

while True:
    print("\n=== MONEY SYSTEM ===")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:
        # ===== DEPOSIT =====
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))

            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                balance += amount
                print(f"Deposit successful! New balance: {balance}")

        # ===== WITHDRAW =====
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
                continue

            if amount > balance:
                print("Insufficient funds.")

                while True:
                    print("\nOptions:")
                    print("1. Re-enter amount")
                    print("2. Check balance")
                    print("3. Exit")

                    option = input("Choose an option: ")

                    if option == "1":
                        break
                    elif option == "2":
                        print(f"Current balance: {balance}")
                    elif option == "3":
                        print("Thank you. Exiting program.")
                        exit()
                    else:
                        print("Invalid option.")

            else:
                balance -= amount
                print(f"Withdrawal successful! Remaining balance: {balance}")

        # ===== CHECK BALANCE =====
        elif choice == "3":
            print(f"Current balance: {balance}")

        # ===== EXIT =====
        elif choice == "4":
            print("Thank you for using the system.")
            break

        # ===== INVALID MENU =====
        else:
            print("Invalid choice. Please select 1 to 4.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")