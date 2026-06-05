# Accept employee details from the user
employee_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: ₹"))

# Calculate components based on the given percentages
hra = 0.20 * basic_salary
da = 0.10 * basic_salary
pf_deduction = 0.12 * basic_salary

# Calculate Gross and Net salaries
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf_deduction

# Determine the employee grade using selection statements
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

# Display the processed payroll information
print("\n--- Payroll Slip ---")
print("Employee Name : ", employee_name)
print("Gross Salary  : ₹", gross_salary)
print("Net Salary    : ₹", net_salary)
print("Grade         : ", grade)
