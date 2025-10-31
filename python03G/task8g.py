# ATM Simulator - Difficulty: Hard

balance = 1000.00

while True:
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Choice: ")

    if choice == "1":
        print(f"Your balance: ${balance:.2f}")

    elif choice == "2":
        deposit = float(input("Deposit amount: $"))
        if deposit > 0:
            balance += deposit
            print(f"New balance: ${balance:.2f}")
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        withdraw = float(input("Withdraw amount: $"))
        if withdraw > balance:
            print("Insufficient funds.")
        elif withdraw <= 0:
            print("Invalid withdrawal amount.")
        else:
            balance -= withdraw
            print(f"New balance: ${balance:.2f}")

    elif choice == "4":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice select 1-4.")
