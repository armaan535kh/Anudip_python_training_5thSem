"""
Employee performance scores are stored as: 
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Create separate lists:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60)  
Sample Output 
Employees Scoring Above 80: 
EMP101 
EMP104 
EMP105 
EMP107 
 
Top Performer: EMP105 (97) 
 
Employees Needing Improvement: 3 
 
Average Score: 71.3 
 
Excellent: 
['EMP101', 'EMP105'] 
 
Good: 
['EMP102', 'EMP104', 'EMP107'] 
 
Average: 
['EMP108', 'EMP110'] 
 
Poor: 
['EMP103', 'EMP106', 'EMP109']
"""

# Employee performance dataset dictionary
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 

# ---------------------------------------------------------
# Task 1: Display employees scoring above 80
# ---------------------------------------------------------
print("Employees Scoring Above 80:")
for emp in performance:
    score = performance[emp]
    if score > 80:
        print(emp)
print()

# ---------------------------------------------------------
# Task 3: Find the top performer
# ---------------------------------------------------------
# Convert to a standard list to access indices safely
items_list = list(performance.items())

# Initialize top performer using the first employee's data
top_emp = items_list[0][0]
top_score = items_list[0][1]

# Loop through all items using the list structure
for item in items_list:
    emp_id = item[0]
    score_value = item[1]
    
    # Check for highest score
    if score_value > top_score:
        top_emp = emp_id
        top_score = score_value

print("Top Performer: " + top_emp + " (" + str(top_score) + ")")
print()

# ---------------------------------------------------------
# Task 2: Count employees needing improvement (score < 60)
# ---------------------------------------------------------
needs_improvement_count = 0
for emp in performance:
    score = performance[emp]
    if score < 60:
        needs_improvement_count = needs_improvement_count + 1

print("Employees Needing Improvement: " + str(needs_improvement_count))
print()

# ---------------------------------------------------------
# Task 4: Calculate average performance score
# ---------------------------------------------------------
total_score = 0
total_employees = 0

for emp in performance:
    score = performance[emp]
    total_score = total_score + score
    total_employees = total_employees + 1

average_score = total_score / total_employees

# round(..., 1) keeps one decimal place to match 71.3
print("Average Score: " + str(round(average_score, 1)))
print()

# ---------------------------------------------------------
# Task 5: Create separate performance lists
# ---------------------------------------------------------
excellent = []
good = []
average = []
poor = []

for emp in performance:
    score = performance[emp]
    
    if score >= 90:
        excellent.append(emp)
    elif score >= 75 and score <= 89:
        good.append(emp)
    elif score >= 60 and score <= 74:
        average.append(emp)
    elif score < 60:
        poor.append(emp)

print("Excellent:")
print(excellent)
print()
print("Good:")
print(good)
print()
print("Average:")
print(average)
print()
print("Poor:")
print(poor)
