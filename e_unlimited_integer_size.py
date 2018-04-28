a = 9_223_372_036_854_775_807  # Biggest value you can store in a 64 bit int
b = 9_223_372_036_854_775_807  # Biggest value you can store in a 64 bit int

c = a * b

print(f'c is {c}')

# Just to show that nothing funny has happened to the type of the value:
print(f'c type is: {type(c)}')
