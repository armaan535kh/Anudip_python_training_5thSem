    #program that repeatedly asks the user to guess the number and displays a success message when the correct number 
game = True
while(game):
        
    guess = int(input("Enter the number 0 to 9 : "))
    if guess < 0 or guess > 9:
        exit("Number should be 0 to 9")

    if guess == 7:
        game = False
        print("Correct guesss")

    #-------------------------------------