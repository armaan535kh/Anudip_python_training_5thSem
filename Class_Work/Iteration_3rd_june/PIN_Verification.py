# program that repeatedly asks the user to enter a PIN until the correct PIN is entered. 
PIN = True
count = 0
while(PIN == True  ):

    if(count >= 4):
        exit("You've reached the limit")
    #validation
    paw = int(input("Enter the PIN "))

    if paw == 1234:
        PIN = False
        print("PIN is correct")
    else:
        print("Try Again")
        count += 1

#--------------------------------------------------
print("Entered in the system")
