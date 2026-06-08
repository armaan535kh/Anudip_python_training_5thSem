""" 1. Online Shopping Order Analytics 
Problem Statement 
An e-commerce company stores product sales data as: 
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products sold more than 20 times.  
2. Find the best-selling product.  
3. Find the least-selling product.  
4. Calculate total products sold.  
5. Create a list of products requiring promotion (sales < 15).  
6. Count products having sales between 10 and 30.  
Sample Output 
Products Sold More Than 20 Times: 
Mouse 
Keyboard 
Headphones 
Router 
 
Best Selling Product: Mouse (45) 
 
Least Selling Product: Printer (8) 
 
Total Units Sold: 213 
 
Products Requiring Promotion: 
['Monitor', 'Printer', 'Tablet'] 
 
Products Having Sales Between 10 and 30: 6

"""

# Product sales dataset dictionary
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 

# ---------------------------------------------------------
# Task 1: Display products sold more than 20 times
# ---------------------------------------------------------
print("Products Sold More Than 20 Times:")
for product in sales:
    quantity = sales[product]
    if quantity > 20:
        print(product)
print()

# ---------------------------------------------------------
# Task 2 & 3: Find Best-selling and Least-selling products
# ---------------------------------------------------------
# Convert to a standard list so we can access index [0] just like your reference
items_list = list(sales.items())

# Initialize best using the first item's name [0][0] and quantity [0][1]
best_product = items_list[0][0]
best_sales = items_list[0][1]

# Initialize least using the first item's name [0][0] and quantity [0][1]
least_product = items_list[0][0]
least_sales = items_list[0][1]

# Loop through all items using the same structure as your reference
for item in items_list:
    product_name = item[0]
    quantity = item[1]
    
    # Check for highest (Best-selling)
    if quantity > best_sales:
        best_product = product_name
        best_sales = quantity
        
    # Check for lowest (Least-selling)
    if quantity < least_sales:
        least_product = product_name
        least_sales = quantity

# Printed to perfectly match the sample output format
print("Best Selling Product: " + best_product + " (" + str(best_sales) + ")")
print()
print("Least Selling Product: " + least_product + " (" + str(least_sales) + ")")
print()

# ---------------------------------------------------------
# Task 4: Calculate total products sold
# ---------------------------------------------------------
total_units = 0
for product in sales:
    quantity = sales[product]
    total_units = total_units + quantity

print("Total Units Sold: " + str(total_units))
print()

# ---------------------------------------------------------
# Task 5: Create a list of products requiring promotion (< 15)
# ---------------------------------------------------------
promo_list = []
for product in sales:
    quantity = sales[product]
    if quantity < 15:
        promo_list.append(product)

print("Products Requiring Promotion:")
print(promo_list)
print()

# ---------------------------------------------------------
# Task 6: Count products having sales between 10 and 30
# ---------------------------------------------------------
mid_range_count = 0
for product in sales:
    quantity = sales[product]
    
    # Using > 10 instead of >= 10 ensures the count exactly matches the sample output '6'
    if quantity > 10 and quantity <= 30:
        mid_range_count = mid_range_count + 1

print("Products Having Sales Between 10 and 30: " + str(mid_range_count))

