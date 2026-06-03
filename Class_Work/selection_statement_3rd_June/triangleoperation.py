#Program to calculate area and perimeter of triangle.
#input of three sides
print("--------------------- Triangle ----------------------")
side1 = int(input("Enter first side (in cm) : "))
side2 = int(input("Enter second side (in cm) : "))
side3 = int(input("Enter third side (in cm) : "))


#------------------------------------------------------------------

print("------------------------------------------------------------")
print("First side  :  ",side1," cm")
print("Second side : ",side2," cm")
print("Third Side : ",side3," cm")
#to calcuate perimeter
perimeter = side1 + side2 + side3
#------------------------------------------------------------------

s = perimeter / 2

#Displaying of Area

print("Area : ", (s * (s-side1) * (s-side2) * (side3))**0.5, "sq.cm")

#Displaying perimeter
print("Perimeter : ",perimeter, " cm")
