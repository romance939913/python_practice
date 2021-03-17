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
# say_something_to_curtis(say_good_morning, 'Kodak')  # Good morning, Kodak!

# # You can use the built-in dir() function to observe any function object.
# print(dir(say_something_to_curtis))


# # Let's write a new say_hi_to function with a __closure__ say_from
# # The __closure__ tuple holds a cell object for each of the function's enclosed variables.

# def say_hi_to(name):
#     def say_from(author):
#         print(f'Hi, {name}! This is a message from {author}.')
#     return say_from

# say_hi_to_ryan_from = say_hi_to('Ryan')
# say_hi_to_ryan_from('Julia')             # Hi, Ryan! This is a message from Julia.
# say_hi_to_ryan_from('Erik')              # Hi, Ryan! This is a message from Erik.
# say_hi_to('Ryan')('Kodak')               # Hi, Ryan! This is a message from Kodak.

# print(say_hi_to_ryan_from.__closure__)                   # (<cell at 0x1093cf1f0: str object at 0x1094035f0>,)
# print(say_hi_to.__closure__)                             # None
# print(say_hi_to_ryan_from.__closure__[0].cell_contents)  # Ryan


# # Decoration happens when you pass a function into a wrapper and assign the 
# # wrapper's name to be the same as the function. 

# def message_decorator(message_func):
#     def message_wrapper(name):
#         from_statement = f'This is a message from {name}.'
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
# print(say_hi("Brennan"))    # Hi! This is a message from Brennan.


# # Syntactic Sugar
# # You simply use @ to preface the name of a decorator function, such as message_decorator

# def message_decorator(message_func):
#     def message_wrapper(*args):
#         name, author = args
#         print(f'{message_func(name)} This is a message from {author}.')
#     return message_wrapper

# @message_decorator
# def say_hi(name):
#     return f'Hi {name}!'

# @message_decorator
# def say_bye(name):
#     return f'Bye {name}!'

# say_hi('Julia', 'Ryan')  # Hi, Julia! This is a message from Ryan.
# say_bye('Kodak', 'Gucci')   # "Bye, Kodak! This is a message from Gucci."


# # The @property decorator references Python's built-in property() function to get a class attribute.
# # It can be used to define the getter of a class property (also has associated setters and deleters)

# class Ring:
#     def __init__(self):
#         self._nickname = "Shiny ring"

#     @property
#     def nickname(self):
#         return self._nickname

#     @nickname.setter
#     def nickname(self, value):
#         self._nickname = value

#     @nickname.deleter
#     def nickname(self):
#         del self._nickname
#         print('Oh no! The ring is gone!')

# ring = Ring()
# print(ring.nickname)                  # Shiny ring
# ring.nickname = "Gollum's precious"
# print(ring.nickname)                  # Gollum's precious
# del ring.nickname                     # Oh no! The ring is gone!


# # This is a helpful pattern that allows the same object to be globally accessed.
# # The @singleton_decorator below nests the @wraps decorator from the Functools module. 
# # The wraps decorator is used to preserve the class information, for example its name (__name__) and docstring (__doc__).

# from functools import wraps

# def singleton_decorator(class_definition):
#     @wraps(class_definition)
#     def class_wrapper():
#         if not class_wrapper.instance:
#             class_wrapper.instance = class_definition()
#         return class_wrapper.instance
#     class_wrapper.instance = None
#     return class_wrapper
 
# @singleton_decorator
# class OneRingToRuleThemAll:
#     """
#     This is a class for The Ring from Lord of the Rings.
#     """
#     def __init__(self):
#         self._nickname = "Gollum's precious"
 
# first_ring = OneRingToRuleThemAll()
# second_ring = OneRingToRuleThemAll()
# third_ring = OneRingToRuleThemAll()
# print(first_ring)   # <__main__.OneRingToRuleThemAll object at 0x1023981f0>
# print(second_ring)  # <__main__.OneRingToRuleThemAll object at 0x1023981f0>
# print(third_ring)   # <__main__.OneRingToRuleThemAll object at 0x1023981f0>
# print(OneRingToRuleThemAll.__name__)  # OneRingToRuleThemAll
# print(OneRingToRuleThemAll.__doc__)   # This is a class for The Ring from Lord of the Rings.