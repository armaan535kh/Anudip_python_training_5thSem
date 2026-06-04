#Generate a secret number between 1 and 50. 
num = int(input("Enter the secret number "))
if(num <0 or num > 50):
    exit("number should be between 1 to 50")


while(True):
    
    guess_number = int(input("Enter the number between 1 and 50 : "))

    if(guess_number > num):
        print("It's too big")
    elif(guess_number < num):
        print("It's too small")
    else:
        print("You guessed it right")
        print()
        break

