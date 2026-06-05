"""
 Bus Seat Reservation Analysis 
Problem Statement 
A bus has seats represented as: 
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0] 
Where: 
• 1 → Seat Booked  
• 0 → Seat Available  
Write a program to: 
1. Count booked and available seats.  
2. Find the first available seat and stop searching immediately.  
3. Create a list of all available seat numbers.  
4. Determine whether the bus is more than 70% occupied.  
Expected Output 
Booked Seats: 6 
Available Seats: 4 
First Available Seat: 2 
Available Seat Numbers: [2, 5, 6, 10] 
Bus Occupancy: 60% 
Status: Not More Than 70% Occupied

"""


# Initial seats list (1 means Booked, 0 means Available)
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Setup starting counters
booked_count = 0
available_count = 0

# Setup empty list for available seat numbers 
available_seat_numbers = []

# Variable to keep track of the first available seat
first_available_seat = 0
found_first_available = False

# Loop through the list using index positions
for i in range(0, len(seats)):
    
    #seat number is always the index position + 1
    seat_number = i + 1
    
    #  Count Booked Seats
    if seats[i] == 1:
        booked_count = booked_count + 1
        
    # Count Available Seats and record their numbers
    if seats[i] == 0:
        available_count = available_count + 1
        available_seat_numbers.append(seat_number)
        
        #  Find the very first available seat and stop searching immediately
        if found_first_available == False:
            first_available_seat = seat_number
            found_first_available = True  # Marks that we found it, so we don't change it again

# Calculate the occupancy percentage
total_seats = len(seats)
occupancy_percentage = (booked_count / total_seats) * 100

# Convert percentage to an integer to match the expected output format
occupancy_percentage = int(occupancy_percentage)

# Print the basic statistics
print("Booked Seats:", booked_count)
print("Available Seats:", available_count)
print("First Available Seat:", first_available_seat)
print("Available Seat Numbers:", available_seat_numbers)
print("Bus Occupancy:", occupancy_percentage + "%")

#  Determine if the bus is more than 70% occupied
if occupancy_percentage > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")
