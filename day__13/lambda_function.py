#syntax
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(1, 2, 3))


# #named function
# def add_two_nums(a, b):
#     return a + b

# print(add_two_nums(2, 3))

#lets change the aove function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))

print((lambda a,b: a + b)(1, 2))

square = lambda x : x ** 2
print(square(3))
cube = lambda x : x**3
print(cube(3))

#multiple variables
multiple_variables = lambda a, b, c: a**2 - 3*b + 4 * c
print(multiple_variables(5,5,3))

#lambda inside function
def power(x):
    return lambda n: x ** n
cube = power(2)(3)
print(cube)