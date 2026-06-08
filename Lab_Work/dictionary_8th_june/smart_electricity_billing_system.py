"""
 Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) is stored as: 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate total units consumed.  
5. Create lists:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300).  
Sample Output 
Houses Consuming More Than 400 Units: 
House103 
House106 
House110 
 
Highest Consumption: 
House110 (600 units) 
 
Lowest Consumption: 
House109 (145 units) 
 
Total Units Consumed: 3220 
 
Low Consumption: 
['House102', 'House105', 'House109'] 
 
Medium Consumption: 
['House101', 'House104', 'House107', 'House108'] 
 
High Consumption: 
['House103', 'House106', 'House110'] 
 
Eligible for Energy-Saving Campaign: 5
"""

# Monthly electricity consumption dataset dictionary
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 

# ---------------------------------------------------------
# Task 1: Display houses consuming more than 400 units
# ---------------------------------------------------------
print("Houses Consuming More Than 400 Units:")
for house in units:
    consumption = units[house]
    if consumption > 400:
        print(house)
print()

# ---------------------------------------------------------
# Task 2 & 3: Find highest and lowest consuming houses
# ---------------------------------------------------------
# Convert to a standard list to access indices safely
items_list = list(units.items())

# Initialize highest variables using the first item's data
highest_house = items_list[0][0]
highest_units = items_list[0][1]

# Initialize lowest variables using the first item's data
lowest_house = items_list[0][0]
lowest_units = items_list[0][1]

# Loop through all items using the list structure
for item in items_list:
    house_id = item[0]
    consumption = item[1]
    
    # Check for maximum consumption
    if consumption > highest_units:
        highest_house = house_id
        highest_units = consumption
        
    # Check for minimum consumption
    if consumption < lowest_units:
        lowest_house = house_id
        lowest_units = consumption

print("Highest Consumption:")
print(highest_house + " (" + str(highest_units) + " units)")
print()
print("Lowest Consumption:")
print(lowest_house + " (" + str(lowest_units) + " units)")
print()

# ---------------------------------------------------------
# Task 4: Calculate total units consumed
# ---------------------------------------------------------
total_units_consumed = 0
for house in units:
    consumption = units[house]
    total_units_consumed = total_units_consumed + consumption

print("Total Units Consumed: " + str(total_units_consumed))
print()

# ---------------------------------------------------------
# Task 5: Create low, medium, and high consumption lists
# ---------------------------------------------------------
low_consumption = []
medium_consumption = []
high_consumption = []

for house in units:
    consumption = units[house]
    
    if consumption < 200:
        low_consumption.append(house)
    elif consumption >= 200 and consumption <= 400:
        medium_consumption.append(house)
    elif consumption > 400:
        high_consumption.append(house)

print("Low Consumption:")
print(low_consumption)
print()
print("Medium Consumption:")
print(medium_consumption)
print()
print("High Consumption:")
print(high_consumption)
print()

# ---------------------------------------------------------
# Task 6: Count houses eligible for energy-saving campaign (> 300)
# ---------------------------------------------------------
campaign_count = 0
for house in units:
    consumption = units[house]
    
    # Check if consumption is strictly greater than 300
    # Matches 5 houses: House101(320), House103(510), House106(430), House108(390), House110(600)
    if consumption > 300:
        campaign_count = campaign_count + 1

print("Eligible for Energy-Saving Campaign: " + str(campaign_count))
