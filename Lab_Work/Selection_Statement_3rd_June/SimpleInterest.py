#Program to calculate Simple interest
#Input from the user rate, interest and principal

rate = int(input("Enter the rate : "))
time = int(input("Enter the time : "))
principal = int(input("Enter the princpal : "))

#check the input

if(rate < 0 and principal < 0):
    exit("Rate and Principal can't be negative")

print("-----------------------------------------")

#Displaying the interest
print(" Interest is : ", (rate/100)*time*principal)
