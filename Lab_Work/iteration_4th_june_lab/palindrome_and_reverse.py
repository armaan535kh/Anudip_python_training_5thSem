# Accept a number from the user
original_number = int(input("Enter a number: "))

# Create copies for processing and comparison
temp_number = original_number
reverse_number = 0

# Iteration statement to reverse the number mathematically
while temp_number > 0:
    remainder = temp_number % 10
    reverse_number = (reverse_number * 10) + remainder
    temp_number = temp_number // 10

# Display the reverse number
print(f"Reverse: {reverse_number}")

# Selection statement to check if it is a palindrome
if original_number == reverse_number:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
