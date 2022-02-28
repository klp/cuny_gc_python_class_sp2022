# Lists

# Collections used to store multiple items in a single variable. They are
# ordered, changable, and allows duplicates

from itertools import count


my_list = [0, 1, "2", 3, "4", 5, 6]
print(len(my_list))

# List indexing
print(my_list[0])   # first element
print(my_list[4])   # fifth element
print(my_list[-1])  # last item
print(my_list[-3])  # fifth element in another way

print(my_list[0:3]) # when slicing include first element, excluding last element
print(my_list[:3])
print(my_list[4:7])
print(my_list[4:])
print(my_list[2:5])

# Reassigning values
my_list[2] = 2  # replace the strings
my_list[4] = 4
print(my_list)

# Adding values to an existing list
my_list.append(7)           # add a value to the end of the list
my_list.append('banana')
print(my_list)

# Insert
my_list.insert(0, 'apple')  # takes two arguments, first index, then value
print(my_list)

my_list.insert(4, 'this is the fifth item')
print(my_list)

# Add list to another list, embedded
# Useful in text analysis
list_2 = [8, 9, 10]
my_list.append(list_2)
print(my_list)
print(my_list[-1])
# Appending is most common list operation

# Add individual items to a list
my_list.extend([11, 12, 13])
print(my_list)

countries = ['brazil', 'bolivia', 'argentina']
other_countries = ['argentina', 'paraguia']
countries.append(other_countries)
print(countries)

print(type(countries[3]))
print(type(countries[2]))

print(countries[3][1]) # getting item of nested list using indexes

# Removing items
countries.pop()     # pop off the last item of a list
print(countries)

countries.remove('bolivia') # remove by content, removes first occurance
print(countries)

# rare
quick_list = [1, 2, 3, 1, 2, 3, 1]
del(quick_list[3])  # if you don't give the index, it'll delete whole list
print(quick_list)

# clear out a list of all values
quick_list.clear()  # empties list
print(quick_list)

