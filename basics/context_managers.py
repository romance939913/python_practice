# # consider this previously common Python code 
# f = None
# try:
#     f = open('some_file.txt')
#     # do stuff with f like read the file
# finally:
#     if f:
#       f.close()

# # The above code can be changed to read like this with the 'with' keyword
# # allows you to not have to write try/finally blocks everywhere you want to access some 
# # resource whose connection needs to be closed, connections like those to files and databases.
# with open('some_file.txt') as f:
#     pass
#     # do stuff with f like read the file
# # f is now scoped only to the with block


# # The with keyword expects two "dunder" methods on the object created with the "with".
# # These objects are Context managers and the methods are named __enter__ and __exit__
# # __enter__ only takes in arg self to set up data (context) necessary
# # __ exit__ takes in type (of exception raised), value (the actual exception expression)
# # itself, and traceback (stacktrace of the exception raised)
# class WithLogger:
#     def __enter__(self):
#         print("2. In __enter__")
#         return self

#     def __exit__(self, type, value, traceback):
#         print("4. In __exit__", type, value)
#         return True


# print("1. Before with")
# with WithLogger() as logger:
#     print("3. In with block")
# print("5. After with")
# # Prints...
# # 1. Before with
# # 2. In __enter__
# # 3. In with block
# # 4. In __exit__ None None
# # 5. After with

# print("Before with")
# with WithLogger() as logger:
#     raise Exception("OMG!")
# print("After with")
# # Prints...
# # 1. Before with
# # 2. __enter__
# # 4. __exit__ <class 'Exception'> OMG!
# # 5. After with

# # When you return True from the __exit__ method, your code indicates to the Python 
# # runtime that everything is ok. If you return False, then Python will continue raising 
# # the error for other try blocks to intercept and handle.

