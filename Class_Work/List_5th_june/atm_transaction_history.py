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
