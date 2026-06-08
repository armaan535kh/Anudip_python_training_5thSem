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
best_product = ""
best_sales = -1        # Start below 0 so any real sale updates it

least_product = ""
least_sales = 999999    # Start very high so any real sale updates it

# Loop through all items to find highest and lowest counts manually
for product in sales:
    quantity = sales[product]
    
    # Check for highest
    if quantity > best_sales:
        best_sales = quantity
        best_product = product
        
    # Check for lowest
    if quantity < least_sales:
        least_sales = quantity
        least_product = product


print("Best Selling Product: " + str(best_product) + " (" + str(best_sales) + ")")
print()
print("Least Selling Product: " + str(least_product) + " (" + str(least_sales) + ")")
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
    
    
    if quantity > 10 and quantity <= 30:
        mid_range_count = mid_range_count + 1


print("Products Having Sales Between 10 and 30: " + str(mid_range_count))
