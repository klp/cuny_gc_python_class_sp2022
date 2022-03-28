import nltk
from nltk.book import *

def lowered(l):
    return [x.lower() for x in l if x.isalpha()]

def split_ten(l):
    return l[:10000]

def unique(l):
    return len(set(l))

def lex_den(l):
    return ### etc