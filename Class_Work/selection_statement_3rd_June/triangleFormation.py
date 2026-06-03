#Program to check three angles form a triangle or not 
angle1 = float(input("Enter first angle : "))
#validate angle1 
if (angle1 <= 0):
    exit("Angle must be positive")

#--------------------------------------------------

#validate angle2
if(angle2 <= 0):
    exit("Angle must be positive")

#--------------------------------------------------

#validate angle3
if(angle3 <= 0):
    exit("Angle must be positive")

#--------------------------------------------------

#Verifying triangle formation
if(angle1 + angle2 + angle3 == 180):
    print("Above angles form a triangle")
else:
    print("Above angles do not form any triangles")