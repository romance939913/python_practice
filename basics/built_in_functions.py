# # Functions using iterables: filter, map, sorted, enumerate, zip

# # Filter: creates a new iterable of the same type for every element that 
# # the function returned true
# a = ['apple', 'banana', 'orange', 'grape']
# print(list(filter(lambda ele: len(ele) > 5, a)))

# # Map: creates a new iterable of the same type which includes the result of 
# # calling the function on every item in the iterable
# b = ['bike', 'skateboard', 'shoes', 'car']
# print(list(map(lambda ele: ele + '!', b)))

# # sorted: creates a new sorted list from the items in the iterable
# # parameters: iterable, optional function (key), reverse=True/False
# c = ['Corey', 'Derek', 'Brennan', 'Alvin', 'brennan']
# print(list(sorted(c, key=str.lower, reverse=False)))

# # enumerate: starts with a sequence and converts it to a series of tuples. 
# # Each tuple is made up of two elements: index and value.
# # The parameter start must be set using its name and an equal sign.
# d = ['first', 'second', 'third', 'fourth']
# print(set(enumerate(d, start=1)))

# zip: creates a zip object filled with tuples that combine 1-to-1 items 
# If the iterables have uneven length then zip stops when the shortest runs out
e = ['Atlanta', 'Houston', 'New York', 'Miami', 'Washington']
f = ['Braves', 'Astros', 'Yankes', 'Marlins', 'Nationals']
print(list(zip(e, f)))

# # Analyze iterables using len, max, min, sum, any, all
# g = [4, 2, 6, 3, 7, 5, 9, 1]
# h = [None, None, None]
# j = ['apple', 'banana', '']
# k = []

# print(len(g))
# print(max(g, key=None))
# print(max(5, 3, 6, 7, 2, key=None))
# print(min(g, key=None))
# print(min(5, 3, 6, 7, 2, key=None))
# print(sum(g))
# print(any(h)) # => False
# print(all(g)) # => True
# print(any(k)) # => False
# print(all(j)) # => False
