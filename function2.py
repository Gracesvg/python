def majina(fname, lname, age):
    print("Myname is ", fname, " ", lname, "and I am", age, " Years old")


majina("Grace", "Gloria", "23")
majina("lara", "jean", "29")
majina("pauline", "Gary", "12")


# create a function that calculates the average of a list
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


list = [4, 5, 6, 7, 8, 9, 13, 45, 67]
answer = calculate_average(list)
print("the average is", answer)




# create a function to disiplay a palindrome
#create a function that'll give you the longest string in a list of items
