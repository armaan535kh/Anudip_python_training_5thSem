# Program to Accept marks of 5 subjects.



total_marks = 0.0
failed_subjects_count = 0

# take input and calculate sums
for i in range(1, 6):
    print("Enter marks for Subject", i, ":")
    score = float(input("Enter the Marks : "))
    
    # Accumulate the total marks
    total_marks = total_marks + score
    
    #Check if the individual subject is failed
    if score < 40:
        failed_subjects_count = failed_subjects_count + 1


percentage = (total_marks / 500)*100


if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Display Outputs
print("\n--- Student Result Summary ---")
print("Total Marks:", total_marks, "/ 500")
print("Percentage:", percentage, "%")
print("Final Grade:", grade)
print("Number of Subjects Failed:", failed_subjects_count)
