#Calculate electricity bill based on the following slab rates

# Input units consumed
units = int(input("Enter the units : "))
if(units < 0):
    exit(" units can't be negative ")

total_bill = 0.0
category = ""

# calculating the bill
if units <= 100:
    total_bill = units * 5
    category = "Low Consumption"
elif units <= 200:
    total_bill = (100 * 5) + ((units - 100) * 7)
    category = "Medium Consumption"
else:
    total_bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    category = "High Consumption"



#  Display output
print("Units Consumed: ", units)
print("Total Bill: ₹ ", total_bill)
print("Category: ", category)
    