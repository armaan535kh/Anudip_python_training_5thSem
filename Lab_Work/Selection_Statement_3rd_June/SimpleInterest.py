#Program to calculate Simple interest
#Input from the user rate, interest and principal


#checking the rate
rate = int(input("Enter the rate : "))
if(rate < 0):
    exit("Rate can't be negative")

#checking the time
time = int(input("Enter the time : "))
if(time < 0):
    exit("Time can't be negative")

#checking the principal
principal = int(input("Enter the princpal : "))
if(principal < 0):
    exit("Principal can't be negative")

print("-----------------------------------------")

#Displaying the interest
print(" Interest is : ", (rate/100)*time*principal)
