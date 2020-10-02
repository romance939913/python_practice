# Identity vs. Equality
# - is vs. ==
# - working with literals
# - isInstance()

a = 1
b = 1.0
c = '1'

# print(a == b)
# print(a is b)

# print(c == '1')
# print(c is '1')

# print(b == 1)
# print(b is 1)

# to avoid syntaxWarning, use isinstance(b, int)
print(b == 1 and isinstance(b, int)) # false

print(str(a) is c)
print(str(a) == c)