# Meaning of Truth in Python
# - numeric types equivalent, but not strings
# - conditionals (if, elif, else)
# - truth equivalence

a = 1
b = 1.0
c = "1"

e = 0
f = ''
g = None
h = []


# print(a == b)
# print(a == c)
# print(b == c)

# truthiness
if h:
    print('truthy')
else: 
    print('falsy')