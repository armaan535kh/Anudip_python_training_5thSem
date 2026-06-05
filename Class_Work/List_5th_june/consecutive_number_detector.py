""" . Consecutive Number Detector 
Problem Statement 
Given a list: 
numbers = [4, 5, 6, 10, 11, 15, 16, 17] 
Write a program to find all pairs of consecutive numbers. 
Expected Output 
4 and 5 are consecutive 
5 and 6 are consecutive 
10 and 11 are consecutive 
15 and 16 are consecutive 
16 and 17 are consecutive 
Additional Challenge 
Store all consecutive pairs in a new list. 
[(4,5), (5,6), (10,11), (15,16), (16,17)] """

# Initial numbers list
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

#empty list to store the pairs for the additional challenge
consecutive_pairs = []

# Loop through the list using index positions
# We stop at len(numbers) - 1 so we don't go past the last item
for i in range(0, len(numbers) - 1):
    
    # Get the current number and the very next number
    current_num = numbers[i]
    next_num = numbers[i + 1]
    
    # Check if the next number is exactly 1 more than the current number
    if next_num == current_num + 1:
        # Print the text output exactly as expected
        print(current_num, "and", next_num, "are consecutive")
        
        #  Create a pair and add it to our list
        pair = [current_num, next_num]
        consecutive_pairs.append(pair)

# Print the final list of pairs

print("Consecutive Pairs List:")
print(consecutive_pairs)
