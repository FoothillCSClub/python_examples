numbers = (1, 2, 3)
letters = ('a', 'b', 'c')

a = [i + 1 for i in numbers]
print(f'list comprehension result: {a}')

d = {letter: 'letter ' + letter for letter in letters}
print(f'dict comprehension result: {d}')
