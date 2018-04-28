# Generators

# Python generators are like iterators that are much easier
# to implement


def generator_foo():
    for i in 1, 2, 3, 4, 5, 6, 7, 8:
        yield i  # yeah, it's that easy.


print('generator 1')
for n in generator_foo():
    print(n)


# Another example of the same thing
def generator_2():
    i = 0
    while i < 9:
        i += 1
        yield i


print('generator 2')
for n in generator_2():
    print(n)
