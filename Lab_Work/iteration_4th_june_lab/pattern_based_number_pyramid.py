rows = int(input("Enter the rows"))
if(rows <0):
    exit("Enter only positive number")

print("Normal Pattern:")

for i in range(1, rows + 1):
    #  printing sequential numbers
    for j in range(1, rows + 1):
        #  print numbers only up to the row inde
        if j <= i:
            print(j, end=" ")
    print()

print("\nReverse Pattern:")

for i in range(rows, 0, -1):
    # loop for printing sequential numbers
    for j in range(1, rows + 1):
        #  print numbers only up to the shrinkin limit
        if j <= i:
            print(j, end=" ")
    print()
