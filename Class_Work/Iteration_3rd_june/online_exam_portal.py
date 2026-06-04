#program that accepts marks from the user and continues asking for marks until the entered score is 40

exam = True
while(exam):

    marks = int(input("Enter the marks out of 100 : "))

    if marks >= 40:
        print("pass")
        exam = False
    else:
        print("Try again")