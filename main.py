def CheckLeap(Year):
  # Cheching if the given year is leap year 
  if((Year % 400 == 0) or 
     (Year % 100 != 0) and 
     (Year % 4 == 0)):
    print("Given Year is a leap Year")
    #Else it is not a leap year 
  else:
#Takimg an input year from user
Year = int(input("Enter the number:"))
 #Printing result
CheckLeap(Year)