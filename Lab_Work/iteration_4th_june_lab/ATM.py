# Initialize the account balance
balance = 10000
choice = 0

# Iteration statement to repeat the menu until Exit is selected
while choice != 4:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    # Take user input for the menu choice
    choice = int(input("Enter your choice (1-4): "))
    
    # Selection statements to handle user choices
    if choice == 1:
        print(f"Your current balance is: ₹{balance}")
        
    elif choice == 2:
        deposit_amount = float(input("Enter the amount to deposit: ₹"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"₹{deposit_amount} deposited successfully.")
        else:
            print("Invalid amount. Deposit must be greater than zero.")
            
    elif choice == 3:
        withdraw_amount = float(input("Enter the amount to withdraw: ₹"))
        if withdraw_amount > balance:
            print("Transaction Denied: Insufficient balance.")
        elif withdraw_amount <= 0:
            print("Invalid amount. Withdrawal must be greater than zero.")
        else:
            balance -= withdraw_amount
            print(f"₹{withdraw_amount} withdrawn successfully.")
            
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        
    else:
        print("Invalid choice! Please select an option between 1 and 4.")
