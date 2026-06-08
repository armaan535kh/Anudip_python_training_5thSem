# City temperature dataset dictionary
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 

# ---------------------------------------------------------
# Task 1: Display cities having temperature above 40°C
# ---------------------------------------------------------
print("Cities Above 40°C:")
for city in temperature:
    temp_value = temperature[city]
    if temp_value > 40:
        print(city)
print()

# ---------------------------------------------------------
# Task 2 & 3: Find the hottest and coolest cities
# ---------------------------------------------------------
# Convert to a standard list to access indices safely
items_list = list(temperature.items())

# Initialize hottest using the first city's data
hottest_city = items_list[0][0]
hottest_temp = items_list[0][1]

# Initialize coolest using the first city's data
coolest_city = items_list[0][0]
coolest_temp = items_list[0][1]

# Loop through all items using the list structure
for item in items_list:
    city_name = item[0]
    temp_value = item[1]
    
    # Check for highest (Hottest city)
    if temp_value > hottest_temp:
        hottest_city = city_name
        hottest_temp = temp_value
        
    # Check for lowest (Coolest city)
    if temp_value < coolest_temp:
        coolest_city = city_name
        coolest_temp = temp_value

print("Hottest City: " + hottest_city + " (" + str(hottest_temp) + "°C)")
print()
print("Coolest City: " + coolest_city + " (" + str(coolest_temp) + "°C)")
print()

# ---------------------------------------------------------
# Task 4: Calculate average temperature
# ---------------------------------------------------------
total_temp = 0
total_cities = 0

for city in temperature:
    temp_value = temperature[city]
    total_temp = total_temp + temp_value
    total_cities = total_cities + 1

average_temp = total_temp / total_cities

# round(..., 1) keeps one decimal place to match 36.8°C
print("Average Temperature: " + str(round(average_temp, 1)) + "°C")
print()

# ---------------------------------------------------------
# Task 5: Create a list of pleasant cities (temperature < 35°C)
# ---------------------------------------------------------
pleasant_cities = []
for city in temperature:
    temp_value = temperature[city]
    if temp_value < 35:
        pleasant_cities.append(city)

print("Pleasant Cities:")
print(pleasant_cities)
print()

# ---------------------------------------------------------
# Task 6: Count cities with temperature between 35°C and 40°C
# ---------------------------------------------------------
between_count = 0
for city in temperature:
    temp_value = temperature[city]
    
    # Using >= 35 and <= 40 satisfies the target count of 4 
    # (Chennai: 37, Kolkata: 39, Lucknow: 40, Hyderabad: 35)
    if temp_value >= 35 and temp_value <= 40:
        between_count = between_count + 1

print("Cities Between 35°C and 40°C: " + str(between_count))
