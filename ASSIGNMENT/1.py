# create a python file to check if a certain year is leap
# Yar is divisible by 4 but not divisible by 100
# except if the year is also divisible by 400

year = int(input("Enter Year:"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("its a leap year")
else:
    print("Not a leap year")
