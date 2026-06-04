num = int(input("Enter a number: "))

#checking the digits

num_of_digits = 0
temp = num
while temp > 0:
    num_of_digits = num_of_digits + 1
    temp = temp // 10

#Sum of digits

total_sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    total_sum = total_sum + (digit ** num_of_digits)
    temp = temp // 10


if total_sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
