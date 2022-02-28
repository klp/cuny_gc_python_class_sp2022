# Lists

# Collections used to store multiple items in a single variable. They are
# ordered, changable, and allows duplicates

from re import M


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

# insert
my_list.insert(0, 'apple')  # takes two arguments, first index, then value
print(my_list)