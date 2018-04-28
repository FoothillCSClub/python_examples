

def add_two_numbers(a, b):
    result = a + b
    return result


print(f'sum of 5 and 11: {add_two_numbers(5, 11)}')

print(f'sum of 3 and 2 : {add_two_numbers(3, 2)}')


# Functions are similar to other languages,
# but with some unique features


# default arguments can be optionally left out by the caller
def add(a=2, b=3):
    return a + b


print(f'add with one argument: {add(4)}')


# arguments can be passed explicitly, useful when multiple
# defaults exist.
print(f'call function with named argument: {add(b=1)}')


# Variable numbers of arguments can be passed
# A single star causes arguments to be packed into a tuple
def print_stuff(*args):
    print(args)  # this is where you would normally iterate over args


# Double stars cause named arguments to be packed into a dictionary
def print_other_stuff(**kwargs):
    print(kwargs)


print_stuff(2, 4, 6, 8)
print_other_stuff(a=2, b=5, c=7)


# it is semi-common to see all of these combined, such as

def a_complex_function(a, b, *args, **kwargs):
    pass


# Functions are objects themselves and can be treated as variables

def foo():
    print('hi')


# Function takes another function as an argument
def call_func(func):
    func()
