# checking for contents
lunch_items = ['spam', 'eggs', 'toast']
print(f'lunch items: {lunch_items}')

fries_in_lunch = 'fries' in lunch_items
print(f'fries in lunch? : {lunch_items}')

# adding to a list
lunch_items.append('fries')
print(f'new lunch items: {lunch_items}')

# removing from a list
lunch_items.remove('eggs')
print(f'lunch items after removal: {lunch_items}')


# adding to a dict
d = {1: 'some', 2: 'other'}
print(f'initial dict: {d}')

# add an entry
d[3] = 'thing'
print(f'dict, updated: {d}')
