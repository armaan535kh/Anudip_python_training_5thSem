# ==============================================================================
# 7. Username Generator System
# ==============================================================================

# Accept full name input from the student
name = input("Enter Name: ")

# 1. Remove spaces
username = name.replace(" ", "")

# 2. Convert to lowercase
username = username.lower()

# 3. Append current year (2026)
username = username + "2026"

# 4. If username length exceeds 12, keep only first 12 characters
# We use slicing [:12] to safely truncate the string if it is too long.
if len(username) > 12:
    username = username[:12]

# Calculate the final length after applying all modification rules
length = len(username)

# Initialize tracking counters for character analysis
vowels = 0
consonants = 0

# 5. Count vowels in the generated username
# 6. Count consonants
# Traverse through the final, processed 12-character username
for ch in username:
# Ensure we only evaluate alphabetic letters (ignoring the '2026' digits)
    if ch.isalpha():
     if ch in "aeiou":
            vowels += 1
    else:
            consonants += 1

# 7. Display username statistics
print("\n--- Username Generation Statistics ---")
print("Generated Username =", username)
print("Username Length    =", length)
print("Vowels             =", vowels)
print("Consonants         =", consonants)
print("Status             = Username Generated Successfully")
