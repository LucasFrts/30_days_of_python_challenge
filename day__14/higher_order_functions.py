#function as parameter

def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst): #function as paramter
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1,2,3,4,5,6])
print(result)

#function as a return value

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def high_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = high_order_function('square') 
print(result(3))
result = high_order_function('cube')
print(result(3))
result = high_order_function('absolute')
print(result(-3))

#python closures

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(15))

#python decorators
#normal function

# def greeting():
#     return 'Welcome to python'
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# g = uppercase_decorator(greeting)
# print(g())

#function above with decorator

# '''This decorator function is a higher order function that takes
# a function as a parameter'''
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# @uppercase_decorator
# def greeting():
#     return 'Welcome to python'
# print(greeting())

#applying multiple decorators to a single function

'''These decorator functino are higher order function that take
functions as parameters'''
#First decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
#Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())

#accepting parameters in decorator functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(first_name, last_name))
print_full_name('Lucas', 'Freitas', 'Brazil')

#Built-in higher order functions
# map syntax
# map(function, iterable)

#ex1
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

#lets apply it with a lambda function
numbers_squared = map(lambda x:x ** 2, numbers)
print(list(numbers_squared))

#ex2
numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))

#ex3
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def change_to_upper(x):
    return x.upper()
names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

names_upper_cased_lambda = map(lambda x:x.upper(), names)
print(list(names_upper_cased_lambda))

 # filter syntax
 # filter(function, iterable)

#ex1
def is_even(num):
    return num % 2 == 0

even_numbers_default = filter(is_even, numbers)
print(list(even_numbers_default))

#ex2
def is_odd(num):
    return num % 2 != 0

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

#ex3
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] 
def is_name_long(name):
    return len(name) > 7

long_names = filter(is_name_long, names)
print(list(long_names)) 

# reduce(function, iterable)
from functools import *
numbers_str = ['1', '2', '3', '4', '5'] 
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print(total)