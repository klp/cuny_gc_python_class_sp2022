fruits = ['apple', 'banana', 'chair', 'watermelon', 'pineapple', 'Greece']

more_fruits = ['strawberry', 'mango', 'kiwi']

best_fruit = 'guava'

fruit_list = []

# Best fruit first element of this list
# Delete non-fruit items
# Add more_fruits to fruits
# print the list 
# print the length of the list

fruit_list.append(best_fruit)
fruits.pop()
fruits.remove('chair')
fruits.extend(more_fruits)
fruit_list.extend(fruits)
print(fruit_list)
print(len(fruit_list))






