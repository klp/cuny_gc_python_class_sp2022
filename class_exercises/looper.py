from re import S


random_numbers = [34, 12, 3, 1, 87, 33, 34, 88]

for number in random_numbers:
    print('here goes a square number')
    print(number ** 2)

for number in random_numbers:
    print(f"The squared number of {number} is {number ** 2}")


squared_numbers = []

for number in random_numbers:
    squared = number ** 2
    squared_numbers.append(squared)

# for number in random_numbers:
#     squared_numbers.append(number ** 3)
    

print(squared_numbers)