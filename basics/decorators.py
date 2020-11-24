# # Python decorators are functions that wrap another function to dynamically modify its behavior.

# # In Python, functions are first-class-objects. meaning there are no restrictions 
# # on how the function can be used (so the function can be passed as an argument).
# def say_hi(name):
#   print(f'Hi, {name}!')

# def say_good_morning(name):
#   print(f'Good morning, {name}!')

# def say_something_to_curtis(say_something_func, name):
#   return say_something_func(name)

# say_something_to_curtis(say_hi, 'Curtis')            # Hi, Curtis!
# say_something_to_curtis(say_good_morning, 'Curtis')  # Good morning, Curtis!

# # You can use the built-in dir() function to observe any function object.
# print(dir(say_something_to_curtis))

# Let's write a new say_hi_to function with a __closure__ say_from

def say_hi_to(name):
  def say_from(author):
    print(f'Hi, {name}!')
    print(f'This is a message from {author}.')
  return say_from

say_hi_to_ryan_from = say_hi_to('Ryan')
say_hi_to_ryan_from('Julia')             # Hi, Ryan! This is a message from Julia.
say_hi_to_ryan_from('Erik')              # Hi, Ryan! This is a message from Erik.

print(say_hi_to_ryan_from.__closure__)   # (<cell at 0x1093cf1f0: str object at 0x1094035f0>,)
print(say_hi_to.__closure__)   # (<cell at 0x1093cf1f0: str object at 0x1094035f0>,)
print(say_hi_to_ryan_from.__closure__[0].cell_contents)  # Ryan