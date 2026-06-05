"""
. Student Performance Analyzer 
Problem Statement 
A teacher has marks of students stored in a list. 
marks = [78, 45, 92, 35, 88, 40, 99, 56] 
Write a program to: 
1. Display all passed students (marks ≥ 40).  
2. Count the number of failed students.  
3. Find the highest and lowest marks without using max() or min().  
4. Create a new list containing marks above 75.  
Expected Output 
Passed Students: [78, 45, 92, 88, 40, 99, 56] 
Failed Count: 1 
Highest Marks: 99 
Lowest Marks: 35 
Merit List: [78, 92, 88, 99]

"""



# Initial student marks list
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# Initialize variables 
passed_students = []
failed_count = 0
merit_list = []

# Initialize highest and lowest with the first element of the list
highest_marks = marks[0]
lowest_marks = marks[0]

# Iterate through the marks list
for mark in marks:
    #  Check for passed students
    if mark >= 40:
        passed_students.append(mark)
    else:
        #  Count failed students
        failed_count += 1

    # Find highest and lowest marks manually
    if mark > highest_marks:
        highest_marks = mark
        
    if mark < lowest_marks:
        lowest_marks = mark

    # Create merit list for marks above 75
    if mark > 75:
        merit_list.append(mark)

# Print the final results
print("Passed Students:", passed_students)
print("Failed Count:", failed_count)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Merit List:", merit_list)
