# # Simple Input and Formatted strings
# # - Prompt with input()
# # - Formatted printing 4 ways

# name = input("What is your name? ")
# # print(name)

# # print('hi, ' + name + '.')
# # print('hi, %s.' % name)
# # print('hi, {0}.'.format(name))
# print(f'hi, {name}.')

# # Joining a string
# shopping_list = ['bread', 'eggs', 'milk']
# print(', '.join(shopping_list))

# # Pythons formatting engine is very powerful, observe:
# print('{:,}'.format(1234567890))
# # '1,234,567,890'

# d = datetime.datetime(2020, 7, 4, 12, 15, 58)
# print('{:%Y-%m-%d %H:%M:%S}'.format(d))
# # '2020-07-04 12:15:58'

# points = 190
# total = 220
# print('Correct answers: {:.2%}'.format(points/total))
# # Correct answers: 86.36%

width=8
print(' decimal      hex   binary')
print('-'*27)
for num in range(1,16):
    for base in 'dXb':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()