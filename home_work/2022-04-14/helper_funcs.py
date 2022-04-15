import nltk
# from nltk.book import *

def lowered(list):
    return [x.lower() for x in list if x.isalpha()]

def split_ten(list):
    return list[:10000]

def slice_fifty(list):
    return list[:50000]

def unique(list):
    return len(set(list))

# def filter_in_words(book, list):
    