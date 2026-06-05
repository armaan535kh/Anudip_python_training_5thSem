"""Inventory Stock Alert System 
Problem Statement 
An inventory manager stores stock quantities as: 
stock = [25, 5, 0, 12, 3, 18, 0, 30] 
Write a program to: 
1. Display products that are out of stock.  
2. Display products that need restocking (quantity less than 10).  
3. Count available products.  
4. Create a new list containing only products with stock greater than or equal to 15.  
Expected Output 
Out of Stock Products: 2 
Restock Required: [5, 0, 3, 0] 
Available Products: 6 
Healthy Stock: [25, 18, 30]"""

# Initial stock list
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# Setup starting values for counters
out_of_stock_count = 0
available_count = 0

# Setup empty lists
restock_required = []
healthy_stock = []

# Loop through each item in the stock list
for qty in stock:
    
    # Count items that are exactly 0 (Out of stock)
    if qty == 0:
        out_of_stock_count = out_of_stock_count + 1
        
    # Count items that are greater than 0 (Available)
    if qty > 0:
        available_count = available_count + 1
        
    # Check for restock (Quantity less than 10)
    if qty < 10:
        restock_required.append(qty)
        
    # Check for healthy stock (Quantity 15 or more)
    if qty >= 15:
        healthy_stock.append(qty)

# Print results
print("Out of Stock Products:", out_of_stock_count)
print("Restock Required:", restock_required)
print("Available Products:", available_count)
print("Healthy Stock:", healthy_stock)
