#Program to Calculate area and perimeter of the rectangle
#Input from the user

length = int(input("Enter the length of a Rectangle in cm : "))
if(length <= 0):
    exit(" length and width can't be 0 ")

Width = int(input("Enter the width of a Rectangle in cm : "))
if(Width <= 0):
    exit(" width can't be  0 ")





print("-----------------------------------")

#Displaying Area
print("Area is ", length * Width, " cm.sq")

#Displaying Parameter
print("Perimeter is ", 2 *(length + Width), " cm")