# Add the necessary code and uncomment (by removing the '#' symbol) the print statements to see if it is working

##################################################
# Exercise 1
# Remove the non-fruit element
# Sort the list alphabetically (google to find out the correct method)

from audioop import reverse


fruits = ['pear', 'apple', 'banana', 'strawberry', 'blackberry', 'waffle', 'grape']
fruits.remove('waffle')
fruits = sorted(fruits)
print(fruits)

##################################################
# Exercise 2
# Remove the last element of the list
# Sort the list in the DESCENDING order (the method you used in exercise 1 will sort the list in the ascending order by default. Google to find out how to give it an option to reverse that order)

random_numbers = [12, 45, 23, 32, 1, 198, 4, 'avocado']
random_numbers.pop()
random_numbers.sort(reverse=True)
print(random_numbers)

##################################################
# Exercise 3
# Remove the first occurrence of the repeated month (there's a nice method for doing that)
# Reverse the order of the list below (google to find out the correct method)
# Notice that here we don't want it to sort alphabetically or numerically, we want to reverse the current order

months = ['June', 'April', 'May', 'April', 'March', 'Feb', 'Jan']
months.remove('April')
months.sort(reverse=True)
print(months)

##################################################
# Exercise 4
# Add another_month and remaining_months to months

another_month = 'July'
remaining_months = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months= []
months.append(another_month)
months.extend(remaining_months)
print(months)

##################################################
# Exercise 5
# You may ignore the first three lines below, we have not covered them yet
# They are just a way to create a list with random numbers

# Store the first 10 items in the list in a variable called "first_10"
# Store the last 5 items in the list in a variable called "last_5"
# Uncomment all the lines of the if statement below to get  print "This is probably correct"
# pay attention to the indentations
# First and third lines of the if statement should have no spaces
# Second and fourth lines should have 4 spaces


import random
random.seed(42)
random_list = [random.randint(0,100) for i in range(30)]
print(random_list)
first_10 = random_list[0:10]
last_5 = random_list[-5:]
print(first_10)
print(last_5)

if len(first_10 + last_5) == 15:
    print("This is probably correct")
else:
    print("Something went wrong")




##################################################
# Exercise 6
#
# Write a if/else condition that will print whether 'banana' is in the `fruit` list created in exercise 1
# The output should be "banana is indeed in the list" in case it is, and "banana is NOT in the list" in case it is not
# Repeat the same if/else expression, but this time with the months` list, created in exercise 3

# To help you out, let me introduce you to the 'in' keyword. Uncomment lines below to see how it works
#print(1 in [1, 2, 3])
#print(5 in [1, 2, 3])