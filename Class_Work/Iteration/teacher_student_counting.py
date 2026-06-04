students = 1
students_present = 0
students_absent = 0

while(students <= 30):
    
    present = int(input("Is student  present (yes == 1/no == 0) : "))
    if(present != 1 and present != 0):
        exit("Input should be in 0 or 1")

    if(present == 1):
        students_present += 1
    else:
        students_absent += 1

    students +=  1

#---------------------------------
print("Student present in the class : ",students_present)
print("Student absent in the class : ", students_absent)

    
