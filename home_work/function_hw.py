'''
Write a function called my_func that takes two arguments---a list and a 
substring---and returns a new list, containing only words that start with the 
chosen substring. Make sure that your function is not case sensitive: meaning 
that if you want to filter by words that start with 'a', both 'apple' and 
'Apple' would be included.

If your function is working properly, this code:

my_list = ['apple', 'banana', 'cranberry', 'Apple', 'watermelon', 'avocado']
only_a = my_func(my_list, 'a')
only_c = my_func(my_list, 'c')
print(only_a)
print(only_c)

should output:
['apple', 'Apple', 'avocado']
['cranberry']
  '''

def my_func(some_list, sub_string):
   
    starting_with = []
    for word in some_list:
        if word.lower().startswith(sub_string):
            starting_with.append(word)
    return starting_with
