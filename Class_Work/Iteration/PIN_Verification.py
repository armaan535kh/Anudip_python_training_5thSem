# program that repeatedly asks the user to enter a PIN until the correct PIN is entered. 
PIN = True
while(PIN == True):

    paw = input("Enter the PIN ")
    if paw == "1234":
        PIN = False
        print("PIN is correct")

#--------------------------------------------------
print("Entered in the system")
