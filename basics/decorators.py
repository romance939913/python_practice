# # Python decorators are functions that wrap another function to dynamically modify its behavior.

# # In Python, functions are first-class-objects. meaning there are no restrictions 
# # on how the function can be used (so the function can be passed as an argument).
# def say_hi(name):
#     print(f'Hi, {name}!')

# def say_good_morning(name):
#     print(f'Good morning, {name}!')

# def say_something_to_curtis(say_something_func, name):
#     return say_something_func(name)

# say_something_to_curtis(say_hi, 'Curtis')            # Hi, Curtis!
# say_something_to_curtis(say_good_morning, 'Curtis')  # Good morning, Curtis!

# # You can use the built-in dir() function to observe any function object.
# print(dir(say_something_to_curtis))


# # Let's write a new say_hi_to function with a __closure__ say_from
# # The __closure__ tuple holds a cell object for each of the function's enclosed variables.
# def say_hi_to(name):
#     def say_from(author):
#         print(f'Hi, {name}!')
#         print(f'This is a message from {author}.')
#     return say_from

# say_hi_to_ryan_from = say_hi_to('Ryan')
# say_hi_to_ryan_from('Julia')             # Hi, Ryan! This is a message from Julia.
# say_hi_to_ryan_from('Erik')              # Hi, Ryan! This is a message from Erik.
# print(say_hi_to('Ryan')('Kodak'))

# print(say_hi_to_ryan_from.__closure__)   # (<cell at 0x1093cf1f0: str object at 0x1094035f0>,)
# print(say_hi_to.__closure__)   # (<cell at 0x1093cf1f0: str object at 0x1094035f0>,)
# print(say_hi_to_ryan_from.__closure__[0].cell_contents)  # Ryan


# # Decoration happens when you pass a function into a wrapper and assign the 
# # wrapper's name to be the same as the function. 
# def message_decorator(message_func):
#     def message_wrapper(name):
#         from_statement = 'This is a message from ' + name
#         print(message_func() + from_statement)
#     return message_wrapper

# def say_hi():
#     return 'Hi! '

# def say_bye():
#     return 'Bye! '

# print(say_hi)               # <function say_hi at 0x10f1a9280>>
# print(say_hi.__closure__)   # None

# say_hi = message_decorator(say_hi)
# print(say_hi)               # <function message_decorator.<locals>.message_wrapper at 0x10f1a93a0>
# print(say_hi.__closure__)   # (<cell at 0x10f17b1f0: function object at 0x10f1a9280>,)
# print(say_hi.__closure__[0].cell_contents) # <function say_hi at 0x10f1a9280>


# # You simply use @ to preface the name of a decorator function, such as message_decorator
# def message_decorator(message_func):
#     def message_wrapper(name):
#         from_statement = 'This is a message from ' + name
#         print(message_func() + from_statement)
#     return message_wrapper

# @message_decorator  # Replaces the need for `say_hi = message_decorator(say_hi)`
# def say_hi():
#     return 'Hi! '

# print(say_hi)   # <function message_decorator.<locals>.message_wrapper at 0x10d53c310>

