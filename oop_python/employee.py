'''
The Child class (subclass) inherits all of the attributes and behavior of 
the Parent class (superclass)

If a child class defines a method that also appears in the parent class, 
objects of the child class will use its own method rather than the parent 
class method

To inherit one class from another, you specify the parent class in 
parentheses after the child class' name
'''

class Employee:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"<Employee ({self.id})>"