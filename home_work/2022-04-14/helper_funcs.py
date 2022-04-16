import nltk
from nltk.corpus import stopwords

def raw_to_tokens(raw_file):
    to_string = raw_file.decode()
    to_tokens = nltk.word_tokenize(to_string)
    return to_tokens

def lowered(list):
    return [x.lower() for x in list if x.isalpha()]

def first_fifty_k(list):
    return list[:50000]

def filter_for_words(book, list):
    return [x for x in book if x in list]

def remove_stops(list):
    stop_words_en = stopwords.words('english')
    return [w for w in list if w not in stop_words_en]

def isolate_pos(l, str):
    return list(filter(lambda x:x[1]==str,l))
    # Note that this funciton returns a list of tuples, 
    # which is fine for our purposes of counting POS
    
def present_round_percentage(d):
    return round(d * 100, 2)
    # here, I got a little obsessive with DRY
    
''' If I had more time, I would probably write some functions to iternate through
    each text for each operation, so I wouldn't have to repeat each step 
    Didn't have enough time to work through that problem unfortunately.'''
    

# def filter_out_words(book, list):
#     return [x for x in book if x not in list]
# Didn't use, but seems like it could be helpful in some circumstances
    