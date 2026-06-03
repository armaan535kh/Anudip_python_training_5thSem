#Program to check type of triangle
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
    #acute angled triangle
    if(angle1 < 90 and angle2 < 90 and angle3 < 90):
        print("Above angles form acute angled triangle")
    elif(angle1 == 90 or angle2 == 90 or angle3 == 90):
        print("Above angles form right angled triangle")
    else:
        print("Above angles form obtuse Angle Triangle")
else:
    print("Above angles do not form any triangles")

