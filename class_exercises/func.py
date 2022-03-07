def say_hello():
    return "hello, person!"

# print(say_hello())
# say_hello()

def hello_person(person):
    '''
    This function returns hello, plus the name of a person.
    '''
    return f"hello, {person}!"

# print(hello_person('Kai'))

def hello_again(person='buddy'):    # optional argument
    return f"hello, {person}"

# print(hello_again())
# print(hello_again('Jade'))

def add_two(num):
    return num + 2

# print(add_two(4))   # side effect

my_var = 'banana'