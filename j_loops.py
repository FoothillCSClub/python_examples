stuff = ['a', 'b', 'c', 'd']

# Every loop in python is either a for loop
# (referred to as a for-in loop in some other languages)
# or a while loop

# While loops operate virtually identically to other languages

i = 0
while i < 5:
    print(f'i is now: {i}')
    i += 1


# for loops however operate a little differently

# iterate over a collection
for item in stuff:
    print(f'item: {item}')

# iterate over a range:
# there is no direct equivalent to the c: ' for(int i = 0; i < 5; ++i) {} '
# instead, range is used
# note that ranges are exclusive; they run up to, but not including,
# the final value.

for i in range(5):
    print(f'range a: {i}')

for i in range(2, 5):
    print(f'range b: {i}')

for i in range(2, 8, 2):
    print(f'range c: {i}')

for i in range(2, 8, -1):
    print(f'range d: {i}')
