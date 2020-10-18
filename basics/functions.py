# # lambda functions vs def functions
# # for smaller trivial functions, make them lambdas

# # example: xor functions makes sure args differ
# # def xor(left, right):
# #     return left != right

# # let xor = (left, right) => left !== right;
# xor = lambda left, right: left != right

# print(xor(True, True))
# print(xor(True, False))
# print(xor(False, True))
# print(xor(False, False))

# # example 2: 
# def print_powers_of(base, exp=1):
#     i = 1
#     while i <= exp:
#         print(base**1)
#         i += 1

# print(print_powers_of(15))
# print(print_powers_of(2, 5))
# print(print_powers_of(2, 5))
# print(print_powers_of(2, 5))
# print(print_powers_of(exp=6, base=7)) # add args in any order if specified

# # Functions Returning Functions (lexical closures) are very similar to javascript
# def greeting_maker(salutation):
#     def greeting(name):
#         return f"{salutation}, {name}"
#     return greeting

# hello = greeting_maker('Hello')
# hiya = greeting_maker('Hiya')

# print(hello('Monica'))
# print(hello('Raj'))

# print(hiya('Raul'))
# print(hiya('Tariq'))

# # include extra positional arguments (those without names) 
# # using the * operator in the function declaration
# def add(a, b, *args):
#     total = a + b
#     for n in args:
#         total += n
#     return total

# add(1, 2)  # Returns 3
# add(2, 3, 4, 5) # Returns 14

# # keyword args (conventionally **kwargs) collects all of the "extra" 
# # keyword arguments, put them into a dictionary
# def print_names_and_countries(greeting, **kwargs):
#     for k, v in kwargs.items():
#         print(greeting, k, "from", v)

# print_names_and_countries("Hi", Monica="Sweden", Charles="Britain", Carlo="Portugal")
# # Prints
# # Hi Monica from Sweden
# # Hi Charles from Britain
# # Hi Carlo from Portugal


# Input Validation function: Try and Except
def prompt():
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >= 0 and age < 120:
            print(f"Cool! you are {age} years old")
        else:
            print('Out of range. Please try again.')
            prompt()
    except:
        print('Please enter a number')
        prompt()

prompt()