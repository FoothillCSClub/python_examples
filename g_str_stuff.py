a = "Monty"
b = "Python"

concatenated_str = a + " " + b
print(f'concatenated str: {concatenated_str}')

# Strings in Python can be multiplied

menu = "spam " * 10
print(f'string product: {menu}')

# Substring
# Get characters from 0 (default start) up to but not including 10.
substring = 'some string to substring'[:10]
print(f'substring: {substring}')

substring2 = 'some string to substring'[10:]
print(f'substring 2: {substring2}')

# Common methods
contains_ham = 'ham' in menu
print(f'contains ham: {contains_ham}')

starts_with_spam = menu.startswith('spam')
print(f'starts with spam: {starts_with_spam}')

option_a = menu.replace('spam', 'eggs')
print(f'option a: {option_a}')

option_b = menu.replace('spam', 'eggs', 1)
print(f'option b: {option_b}')


# format string
formatted_str_a = f'Example formatted string: {5}'

# old style format (pre-3.6 Python)
formatted_str_b = 'Example formatted string: {}'.format(5)

# even older style (c-style) (python2)
formatted_str_c = 'Example formatted string: %s' % 5

print(formatted_str_a)
print(formatted_str_b)
print(formatted_str_c)
