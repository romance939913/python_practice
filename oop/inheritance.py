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

class Manager(Employee):
    def __init__(self, id):
        super().__init__(id)
        self.employees = []

    def add_direct_report(self, *employees):
        for employee in employees:
            self.employees.append(employee)

    def __repr__(self):
        return f"<Manager ({self.id}, {self.employees})>"

employee1 = Employee(123)
employee2 = Employee(234)
manager1 = Manager(345)
manager1.add_direct_report(employee1, employee2)
print(manager1) # => <Manager (345, [<Employee (123)>, <Employee (234)>])>


class Parent:
    def boop(self):
        print("I am Parent#boop")

class Child(Parent):
    def boop(self):
        print("I am Child#boop")
        super().boop()

Child().boop()
# Prints
# "I am Child#boop"
# "I am Parent#boop"