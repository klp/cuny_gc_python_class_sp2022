import nltk

def raw_to_tokens(raw_file):
    to_string = raw_file.decode()
    to_tokens = nltk.word_tokenize(decode)
    return to_tokens


def lowered(list):
    return [x.lower() for x in list if x.isalpha()]

def first_fifty_k(list):
    return list[:50000]

# def unique(list):
#     return len(set(list))

def filter_in_words(book, list):
    return [x for x in book if x in list]

def filter_out_words(book, list):
    return [x for x in book if x not in list]
    