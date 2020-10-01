# Duck typing
# "if it looks like a duck, and quacks like a duck..."
# "easier than type checking for functions"

name = 4545
arr = ['dog', 'cat', 'watermelons']

# try:
#     print(len(name))
# except TypeError:
#     print(f'object {name} has no len()')

try:
    print(len(name))
except NameError:
    print(f'object {name} is not defined')
else:
    print('hit the else statement')
finally:
    print('hit the finally statement')