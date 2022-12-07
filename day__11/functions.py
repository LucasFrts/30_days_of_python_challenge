def generate_full_name(first_name = 'Python', last_name='Programmer'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print('Full name default: ', generate_full_name())
print('Full name: ', generate_full_name('Lucas', 'Freitas'))
print('Full name without order: ', generate_full_name(last_name='Freitas', first_name='Lucas'))

def sum_two_numbers(num_one, num_two):
    total = num_one + num_two
    return total

print('Sum of two numbers: ',sum_two_numbers(2, 7))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Calculating age: ', calculate_age(2022, 2001))

def weight_of_object(mass, gravity = 9.81):
    weigth = str(mass * gravity) + ' N'
    return weigth
print('Weight of object: ', weight_of_object(100))

def greeting(name = 'Programmer'):
    message = 'Welcome to python for everyone, %s!' % name
    return message
print(greeting('Lucas'))
print(greeting())

def add_ten(num):
    number = num + 10
    return number

print(add_ten(157))

def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total
print(sum_of_numbers(100))

def is_even(num):
    return num % 2 == 0
print(is_even(2))
print(is_even(3))

def find_even_numbers(num):
    list = []
    for i in range(num + 1):
        if i % 2 == 0:
            list.append(i)
    return list
print(find_even_numbers(100))

def sum_all_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_numbers(100,25,32,47))

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('T1', 'TeamOne', 'TimeUm')


