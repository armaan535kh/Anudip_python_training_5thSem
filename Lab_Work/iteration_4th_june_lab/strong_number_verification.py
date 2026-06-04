#Program to check whether a given number is a Strong Number. 

# Input number
number = int(input("Enter the number : "))

temp = number
digit_sum = 0

# Loop through each digit of the number
while temp > 0:
    digit = temp % 10
    
    # Calculate the factorial 
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
        
    digit_sum += fact
    temp //= 10


if digit_sum == number:
    print("IT is a Strong Number")
else:
    print("IT is not a Strong Number")
