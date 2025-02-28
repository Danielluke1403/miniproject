def show_balance(balance):
    print(f"\nYour current balance is: ₹{balance:.2f}\n")  # Added currency symbol and formatting

def deposit():
    amount = float(input("\nEnter the amount to deposit: ₹"))
    if amount <= 0:
        print("Invalid amount. Deposit must be greater than 0.")
        return 0
    else:
        print(f"₹{amount:.2f} deposited successfully!\n")
        return amount

def withdraw(balance):
    amount = float(input("\nEnter the amount to withdraw: ₹"))
    if amount > balance:
        print("Insufficient balance. Withdrawal not possible.")
        return 0
    elif amount <= 0:
        print("Invalid amount. Withdrawal must be greater than 0.")
        return 0
    else:
        print(f"₹{amount:.2f} withdrawn successfully!\n")
        return amount

def main():
    balance = 0  # Initialize balance
    is_running = True

    while is_running:
        print("\n===== Banking Program =====")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            print("\nThank you for using the banking program. Have a great day! 😊")
            is_running = False
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
