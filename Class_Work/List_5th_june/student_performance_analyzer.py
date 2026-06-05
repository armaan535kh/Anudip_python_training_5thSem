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
