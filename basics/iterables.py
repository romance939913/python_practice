# # Lists
# friends = ['derek', 'kyle', 'robby', 'gabe']

# print(friends[1])
# print(friends[-1])
# print(friends[:-1])
# print(friends[1:])
# print(friends[::2])

# # functions that mutate the list
# supplies = ['crayons', 'pencil', 'paper', 'Kleenex', 'eraser']

# supplies.append('markers')
# print(supplies)

# supplies.remove('pencil')
# print(supplies)

# supplies.sort()
# print(supplies)
# # sorts with capital letters first

# supplies.sort(key=str.lower)
# print(supplies)
# # applies this function to each item for sorting purposes

# # functions that don't mutate original copy
# colors = ['red', 'orange', 'blue', 'pink']

# alphabetical = sorted(colors)
# reversed_colors = list(reversed(colors))

# print(colors)
# print(alphabetical)
# print(reversed_colors)


# # Tuples
# # Just like lists except are immutable
# a = (1, 3, 2, 6, 4, 8, 7, 5)
# b = ('apple', 'banana', 'orange', 'grape', 'pear')

# # sort alphabetically with sorted() which will automatically cast to a list
# alpha_b = tuple(sorted(b))
# print(alpha_b)

# # functions can return tuples of data with the return statement
# scores = (92, 59, 80, 77, 89, 95, 100, 91)

# def min_max(nums):
#     return min(nums), max(nums)

# (lowest, highest) = min_max(scores)
# print(lowest)
# print(highest)

# # declare a single item tuple with a trailing comma
# single = (1,)
# other_single = ('a',)


# # Ranges
# # a set of integers: range(start, end, step) end is exclisive
# items = ['a', 'b', 'c']
# for i in range(len(items)):
#     print(i, items[i])


# # dictionaries
# book = {
#     'title': 'Goodnight Moon', 
#     'rating': 7642, 
#     'stars': 4.8,
#     'author': {
#         'first_name': 'Margaret',
#         'last_name': 'Wise Brown'
#     },
#     'pictures': ['goodnightmoon1.png', 'goodnightmoon2.png'],
# }

# print(len(book))

# del book['stars']
# print(book)

# book['stars'] = 4.8
# print(book)

# for i in book: 
#     print(i, book[i])

# # Dict function parameter options
# pond = dict(depth=10, area='210 square feet', fish=['Mary', 'Bob', 'Carlos'])
# print(pond)

# alligators = dict([
#     ('lifespan', 50),
#     ('length', 3.4),
#     ('species', ['American Alligator', 'Chinese Alligator']),
# ])
# print(alligators)

# keys = ['name', 'homeruns', 'rbis', 'hits']
# values = ['Babe Ruth', 850, 5551, 7612]
# player = dict(zip(keys, values))
# print(player)

# print(dir(player))


# # Set
# # A group of elements in which each is unique
# # Work with sets using operators &, |, -, ^
# # | or union() combines the two sets
# # & or intersection() returns the elements found in both sets
# # - or difference() returns the elements not found in the second set
# # ^ or symmetric_difference() returns the elements found in exactly one set
# a = set('banana')
# b = set('scarab')
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))

# fruit = ['apple', 'banana', 'grape', 'orange', 'banana', 'apple', 'pear']
# fruit = set(fruit)
# print(fruit)

# # e-commerce example
# purchase_emails = ['bob@gmail.com', 'sam@yahoo.com', 'riley@email.com']
# support_emails = ['joe@live.com', 'bob@gmail.com', 'sam@yahoo.com']
# print('Users who made a purchase and also called the help desk')
# print(set(purchase_emails) & set(support_emails))

# # Blog hashtag example
# posts = [
#     {'title': 'All About Lists', 'tags': ('fun', 'informative', 'lists')},
#     {'title': 'Tuple Trouble', 'tags': ('fun', 'tuples')},
#     {'title': 'Sparkling Sets', 'tags': ('informative', 'numbers')},
# ]
# all_tags = []
# for i in range(len(posts)):
#     print(posts[i]['tags'])
#     all_tags.extend(posts[i]['tags'])

# all_tags = list(set(all_tags))
# print(sorted(all_tags))


# # Custom sorting
# users = [
#     {'id': 14235, 'display_name': 'JoeSmith', 'email': 'joe.smith@email.com'},
#     {'id': 32451, 'display_name': 'BobJones', 'email': 'bobjones@yahoo.com'},
#     {'id': 52243, 'display_name': 'AlexChen', 'email': 'alexchen1@gmail.com'},
# ]

# def sorter(user):
#     return user['display_name']

# users.sort(key=sorter)
# print(users)
# print(sorted(users, key=sorter, reverse=True))