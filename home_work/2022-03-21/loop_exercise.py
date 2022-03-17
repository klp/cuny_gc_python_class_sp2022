""" Create a function called 'only_lower' that takes a list of strings as an 
argument
and returns another list. This new list will contain only the lowered version of
 the words of the previous list (exclude numbers and punctuation)

Hint:
- google "python isalpha" and play a bit with this method to see how it works

"""

from text import random_text
# Importing a list of strings from the text.py file
# Feel free to open that file and take a look at the list
# Notice how it has been 'tokenized', meaning that every word, number or 
# punctuation is an item of the list

def only_lower(some_list):
    lowered_list = []
    for item in some_list:
        if item.isalpha():
            lower_item = item.lower()
            lowered_list.append(lower_item)
    return lowered_list

print(only_lower(random_text))