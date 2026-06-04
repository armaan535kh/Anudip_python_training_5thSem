#Accept a number from the user and determine whether it is a prime number or not.

num = int(input("Enter a number: "))


factor_count = 0
for i in range(1, num + 1):
    
    if num % i == 0:
        print("factors are : ",i)
        factor_count = factor_count + 1

print("---------------------------------------") 


if factor_count == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")

        

#-----------------------------------------------

