balance = 1000
while True:
    print("Welcome to the ATM")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit")
    # Get user choice
    choice = int(input("Enter your choice: "))
    # Check balance
    if choice == 1:
        print("Your current balance is:", balance)
    # Withdraw money
    elif choice == 2:
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance =balance-amount
            print("Amount withdrawn:", amount)
            print("Your current balance is:", balance)
    # Deposit money
    elif choice == 3:
        amount = int(input("Enter the amount you want to deposit: "))
        balance += amount
        print("Amount deposited:", amount)
        print("Your current balance is:", balance)
    # Exit
    elif choice == 4:
        print("Thank you for using our ATM. Have a nice day!")
        break
    # Invalid choice
    else:
        print("Invalid choice. Please enter a valid option.")
        

