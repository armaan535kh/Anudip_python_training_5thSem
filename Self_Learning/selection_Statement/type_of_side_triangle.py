#program to check type of side angle
#Input from the user

#Validation
side1 = int(input("Enter the side 1 : "))
if(side1 <= 0):
    exit("Side should be positive")

#-----------------------------------------

side2 = int(input("Enter the side 2 : "))
if(side2 <= 0):
    exit("Side2 should be positive")


#-------------------------------------------
side3 = int(input("Enter the side 3 : "))
if(side3 <= 0):
    exit("Side3 should be positive")

#-------------------------------------------

if(side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2):
    

    #Equilateral Triangle
    if(side1 == side2 == side3):
        print("The triangle is equilateral Triangle")
    elif(side1 == side2 or side2 == side3 or side3 == side1): #Isoceles Triangle
        print("The triangle is Isoceles")
    else:
        print("The triangle is Scalene") #Scalene Triangle
else:
    print("It is not a triangle")