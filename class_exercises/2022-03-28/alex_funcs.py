import nltk
from nltk.book import *

def lower_words(text_num):
    new_list = []
    for x in text_num:
        if x.isalpha():
            new_list.append(x.lower())
    return new_list

def lex_den(a_list):
    return len(set(a_list[:10000]))/10000

t3 = lower_words(text3)
t3_ld = lex_den(t3)

print(t3[:30])
print(t3_ld)


