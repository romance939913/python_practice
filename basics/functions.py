# lambda functions vs def functions
# for smaller trivial functions, make them lambdas

# example: xor functions makes sure args differ
# def xor(left, right):
#     return left != right

# let xor = (left, right) => left !== right;
xor = lambda left, right: left != right

print(xor(True, True))
print(xor(True, False))
print(xor(False, True))
print(xor(False, False))

# example 2: 
def print_powers_of(base, exp=1):
    i = 1
    while i <= exp:
        print(base**1)
        i += 1

print(print_powers_of(15))
print(print_powers_of(2, 5))
print(print_powers_of(2, 5))
print(print_powers_of(2, 5))
print(print_powers_of(exp=6, base=7)) # add args in any order if specified

# Functions Returning Functions (lexical closures) are very similar to javascript

def greeting_maker(salutation):
    def greeting(name):
        return f"{salutation}, {name}"
    return greeting

hello = greeting_maker('Hello')
hiya = greeting_maker('Hiya')

print(hello('Monica'))
print(hello('Raj'))

print(hiya('Raul'))
print(hiya('Tariq'))