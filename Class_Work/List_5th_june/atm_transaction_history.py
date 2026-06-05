"""
.ATM Transaction History 
Problem Statement 
A customer's transactions are stored as: 
transactions = [5000, -2000, 3000, -1000, -500, 7000] 
Positive values represent deposits and negative values represent withdrawals. 
Write a program to: 
1. Calculate the current balance.  
2. Count total deposits and withdrawals.  
3. Find the largest deposit and largest withdrawal.  
4. Create separate lists for deposits and withdrawals.  
Expected Output 
Current Balance: 11500 
Deposits: [5000, 3000, 7000] 
Withdrawals: [-2000, -1000, -500] 
Largest Deposit: 7000 
Largest Withdrawal: -2000 

"""
# Initial transaction list
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Setup starting values
current_balance = 0
largest_deposit = 0
largest_withdrawal = 0

# Setup empty lists
deposits = []
withdrawals = []

# Loop through each transaction
for amt in transactions:
    # Add amount to balance
    current_balance = current_balance + amt
    
    # Process deposits 
    if amt > 0:
        deposits.append(amt)
        if amt > largest_deposit:
            largest_deposit = amt
            
    # Process withdrawals 
    if amt < 0:
        withdrawals.append(amt)
        if amt < largest_withdrawal:
            largest_withdrawal = amt

# Print results
print("Current Balance:", current_balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)
