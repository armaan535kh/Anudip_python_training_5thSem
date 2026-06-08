"""
4. Cricket Tournament Statistics 
Problem Statement 
Runs scored by players in a tournament: 
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 
Tasks 
1. Display players scoring more than 500 runs.  
2. Find the Orange Cap winner.  
3. Find the lowest scorer.  
4. Calculate total runs scored.  
5. Create a list of players scoring below 400.  
6. Count players scoring between 400 and 600 runs.  
Sample Output 
Players Scoring More Than 500 Runs: 
Virat 
Rohit 
Gill 
Pant 
 
Orange Cap Winner: Gill (698) 
 
Lowest Scorer: Hardik (278) 
 
Total Tournament Runs: 4657 
 
Players Scoring Below 400: 
['Hardik', 'Surya', 'Jadeja'] 
 
Players Between 400 and 600 Runs: 5
"""


# Cricket tournament dataset dictionary
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 

# ---------------------------------------------------------
# Task 1: Display players scoring more than 500 runs
# ---------------------------------------------------------
print("Players Scoring More Than 500 Runs:")
for player in runs:
    run_value = runs[player]
    if run_value > 500:
        print(player)
print()

# ---------------------------------------------------------
# Task 2 & 3: Find the Orange Cap winner and Lowest scorer
# ---------------------------------------------------------
# Convert to a standard list to access indices safely
items_list = list(runs.items())

# Initialize Orange Cap winner using the first player's data
orange_cap_winner = items_list[0][0]
highest_runs = items_list[0][1]

# Initialize lowest scorer using the first player's data
lowest_scorer = items_list[0][0]
lowest_runs = items_list[0][1]

# Loop through all items using the list structure
for item in items_list:
    player_name = item[0]
    run_value = item[1]
    
    # Check for highest (Orange Cap Winner)
    if run_value > highest_runs:
        orange_cap_winner = player_name
        highest_runs = run_value
        
    # Check for lowest
    if run_value < lowest_runs:
        lowest_scorer = player_name
        lowest_runs = run_value

print("Orange Cap Winner: " + orange_cap_winner + " (" + str(highest_runs) + ")")
print()
print("Lowest Scorer: " + lowest_scorer + " (" + str(lowest_runs) + ")")
print()

# ---------------------------------------------------------
# Task 4: Calculate total runs scored
# ---------------------------------------------------------
total_tournament_runs = 0
for player in runs:
    run_value = runs[player]
    total_tournament_runs = total_tournament_runs + run_value

print("Total Tournament Runs: " + str(total_tournament_runs))
print()

# ---------------------------------------------------------
# Task 5: Create a list of players scoring below 400
# ---------------------------------------------------------
below_400_list = []
for player in runs:
    run_value = runs[player]
    if run_value < 400:
        below_400_list.append(player)

print("Players Scoring Below 400:")
print(below_400_list)
print()

# ---------------------------------------------------------
# Task 6: Count players scoring between 400 and 600 runs
# ---------------------------------------------------------
between_count = 0
for player in runs:
    run_value = runs[player]
    
    # Using >= 400 and <= 600 matches the exact count of 5
    # (Rohit: 512, Rahul: 435, Pant: 534, Iyer: 455, KL: 410)
    if run_value >= 400 and run_value <= 600:
        between_count = between_count + 1

print("Players Between 400 and 600 Runs: " + str(between_count))
