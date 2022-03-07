from os import nice


random_string = """Vermont is famous for its verdant summer landscapes and 
postcard-worthy fall colors. But it’s the Green Mountain State’s winter 
landscape that truly sparks my photographic eye. New snow transforms the dull 
shades of stick season into a fresh palette of photographic possibility. Like a 
life-size Etch A Sketch, the landscape is continually transformed by recurring 
snowfall.Fresh snow allows lone trees, hay bales and empty swimming pools to 
cast more accentuated shadows. It isolates and elevates mundane objects and 
presents them as if on display."""

nice_list = random_string.split() # spaces are the delimiter by default

# print(nice_list)        # notice that punctuation is included
# print(nice_list[:10])

# new list with only the words that start with 'f' from nice_list



# create a new list

f_words = []

# run a for loop

for word in nice_list:
# run condition: if word starts with a 'f'
    if word.startswith('f'):
        # append word that match condition to new list
        f_words.append(word)

print(f_words)


