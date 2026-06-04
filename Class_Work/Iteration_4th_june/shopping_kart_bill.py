# program that continuously accepts item prices and calculates the total bill amount. The program should stop accepting
total_amount = 0
a = True

while(a):
    
    price = int(input("Enter the price  : "))
    if(price <= 0):
        exit("Number should be positive")

    if (price == 0):
        a = False

    print("Enter item price : ", price)
    total_amount += price

#---------------------------------------

print("Total bill amount : ", total_amount)