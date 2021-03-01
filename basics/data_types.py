# Lists (heterogeneous, mutable)
# Very similar to the array data type in javascript. Typically used to store
# a sequence of items that are all the same type
empty_list = []
departments = ['HR', 'Engineering', 'Sales', 'Finance', 'Customer Support']
specials = list() # initiates an empty list

print('HR' in departments)

# Tuples (usually homogeneous, immutable)
# Very similar to lists, can be initiated with or without parantheses
time_blocks = ('AM', 'PM')
colors = 'red', 'green', 'blue'
numbers = 1, 2, 3

print(1 in numbers)
print('yellow' in colors)

# Ranges (homogeneous, immutable)
# A list of numbers in order, often used with for loops
# declared with three parameters range(start, stop, step) stop is exclusive
print(range(5))
print(range(1, 5))
print(range(0, 25, 5))
print(range(0))
print(range(5, 0, -1))

# Dictionaries (heterogeneous, mutable)
# a mapple collection where a hashable value is used as a key to refrencable
# objects stored in dictionaries. declared with curly braces or dict()
# dictionaries with the same values return true when testing equality
a = {'one': 1, 'two': 2, 'three': 3}
b = dict(one=1, two=2, three=3)

print(a == b) # => True
print('one' in a) # => true

# Set (heterogeneous, mutable, but can be immutable))
# A set is an unordered  collection of distinct objects. dups will be dropped. 
# Objects are hashable and support mathmatical operations

school_bag = { 'book', 'paper', 'pencil', 'book', 'eraser', 'pencil' }
letters = set('abracadabra')

print(school_bag)
print(letters)