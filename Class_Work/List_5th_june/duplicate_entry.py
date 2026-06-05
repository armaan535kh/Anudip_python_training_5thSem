numbers = []

for x in range(5):
    num = int(input("Enter the number : "))

    numbers.append(num)

print("------------------------------------------")
element = int(input("Enter any number to remove its duplicate : "))

frequency = numbers.count(element)
if frequency == 0:
    print("element not found")
elif frequency == 1:
    print("no duplicate found")
else:
    #reversing the list
    numbers.reverse()
    for i in range(1, frequency):
        
        numbers.remove(element)

    numbers.reverse()
    print("Final list ",  numberse)

   

