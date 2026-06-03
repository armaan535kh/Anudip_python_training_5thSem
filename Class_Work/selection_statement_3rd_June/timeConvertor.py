#Program to convert time into corresponding hour, minute and second
#input of time in second
second = int(input("Enter time in seconds : "))

#check second is negative
if(second < 0):
    exit("Time cannot be negative")

#-------------------------------------------------------------------
print("-----------------------------")
hour = 0
minute = 0

#converting number of seconds into hours
if(second >= 3600):
    hour = second // 3600
    second = second % 3600
#--------------------------------------------------------------------
#Converting into minute
if(second >= 60):
    minute = second // 60
    second = second % 60

#---------------------------------------------------------------------
#Display the time
print("Seconds in ", hour ," hour" , minute , " minute", second, " second")