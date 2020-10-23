'''
Classes are a way of combining information and behavior

Class names are defined in upper camel case (Pascal Case)
Leave a comment at the beginning of your class describing it

Python classes don't support private instance variables/methods.
Use a lead underscore to indicate that.

If you know the instance variables that you want to use, 
you can use a "dunder class variable" named __slots__() to reserve
memory for the instance variables that you know you will use.

Override the memory address default when printing an object with
instance "dunder method" __repr__()

Decorators start with the @ symbol and allows us to change the way methods 
get invoked. There's a built-in decorator named property that you can apply to a 
method to make it seem like a readable property
'''

# (description) Class for a simple angry birds game
class AngryBird:
    __slots__ = ['_x', '_y']

    def __init__(self):
        self._x = 0
        self._y = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            value = 0
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0:
            value = 0
        self._y = value

    def move_vertically(self, delta):
        self._y += delta

    def move_horizontally(self, delta):
        self._x += delta

    def __repr__(self):
        return f"<AngryBird ({self._x}, {self._y})>"

bird = AngryBird()
print(bird)
print(bird.x, bird.y)  #> 0 0

# Do not add argument for self. Python does that automatically
bird.move_vertically(8)
print(bird)
print(bird.x, bird.y)  #> 0 8

