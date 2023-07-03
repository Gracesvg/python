# Write a python program to calculate a ticket price for a movie theatre based on the age of a customer:
# 0years is free, between 6-12yrs is 500 13-17yrs is 1000 18+ yrs is 1500
age = int(input("Enter your age"))
if age < 0:
    print("invalid")
elif age == 0:
    print("ticket is free")
elif age > 6 and age <= 12:
    print("ticket is 500")
elif age > 13 and age <= 17:
    print("ticket is 1000")
elif age > 18:
    print("ticket is 1500")
