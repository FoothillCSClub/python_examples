# Note that unlike other languages,
# you don't need to cast numbers to different types

an_int_value = 5
another_int = 2

float_result = an_int_value / another_int

print(f'division result was: {float_result}')

# If you need an integer result, use floor division, like so:
# This does the same thing as dividing an int by another int in
# a language such as C or Java.

int_result = an_int_value // another_int

print(f'floor division result was: {int_result}')

# Because of this, integers and floats can be usually considered
# interchangeable in python
