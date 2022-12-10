#'
def add_two_numbers(number_one = 0, number_two = 0):
    return number_one + number_two
print(add_two_numbers(9, 7))

#2
def area_of_circle(radius = 0):
    area = 3.14 * radius ** 2
    return area
print(area_of_circle(60))

#3
def add_all_nums(*args):
    sum = 0
    for num in args:
        if type(num) == int or type(num) == float:
           sum += num
        else:
            print('%s is not a integer' %num) 
    print(sum)

add_all_nums(10 ,50, 'chuva', 80, 22, 1.32) 

#4
def convert_celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius*9/5) + 32
    return fahrenheit
print(convert_celcius_to_fahrenheit(38))

#5
def check_season(mounth):
    if mounth == 12 or mounth == 1 or mounth == 2:
        print('Winter')
    elif mounth == 3 or mounth == 4 or mounth == 5:
        print('Spring')
    elif mounth == 6 or mounth == 7 or mounth == 8:
        print('August')
    elif mounth == 9 or mounth == 10 or mounth == 11:
        print('Autumn')
check_season(9)

#6
def calculate_slope(ini_x, end_x, ini_y, end_y):
    m = (end_x - ini_x)/(end_y - ini_y)
    return m

import math
#7
def bhaskara(a_value, b_value, c_value):
    x_1 = ((b_value * -1) + math.sqrt(((-1 * 4 * a_value * c_value) + math.pow(b_value, 2))))/(2 * a_value)
    x_2 = ((b_value * -1) - math.sqrt(((-1 * 4 * a_value * c_value) + math.pow(b_value, 2))))/(2 * a_value)
    return f'the result of this quadratic equation is x1 = {x_1} and x2 = {x_2}'
print(bhaskara(1, 4, 3)) 

#8
def print_list(args):
    for item in args:
        print(item)

print_list(['terceiro', 'quarto', 'quinto', 'sexto'])

#9
def reverse_list(list):
    reverse = []
    for i in range(len(list)-1, -1, -1):
        reverse.append(list[i])
    return reverse
print(reverse_list(['oi', 'ta me ouvindo', 'alooooooo']))

#10
def capitalize_items_of_list(list):
    captalize_list = []
    for i in range(0, len(list)):
        captalize_list.append(list[i].capitalize())
    return captalize_list
print(capitalize_items_of_list(['salve', 'galerinha', 'beleza?']))

#11
def add_item(list, item):
    list.append(item)
    return list
print(add_item([1,2,3,4], 5))

#12
def remove_item(list, item):
    if item in list:   
        list.remove(item)
        return list
print(remove_item(['salve', 'treta', 'galerinha', 'beleza'], 'treta'))

#13
def sum_all_numbers(num):
    sum = 0
    for i in range(0, num+1):
        sum += i
    return sum
print(sum_all_numbers(100))

#14
def sum_of_odds(num):
    sum = 0
    for i in range(0, num + 1):
        if i % 2 != 0:
            sum += i
    return sum
print(sum_of_odds(100))

#15
def sum_of_even(num):
    sum = 0
    for i in range(0, num + 1):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_even(50))

#16
def even_and_odds(num):
    even = 0
    odds = 0
    for i in range(0, num + 1):
        print(i)
        if i % 2 == 0:
            even += 1
        else:
            odds += 1
    print(f'the number of odds: {odds}')
    print(f'the number of even: {even}')
even_and_odds(100)

#17
def factorial(num):
    result = 1
    for i in range(1, num):
        result += result*i
    return result
print(factorial(5))

#18
def is_empty(param = 'default'):
    if param == 'default':
        print('nao foram passados parametros')
    else:
        print(f'parametro: {param}')
is_empty()
is_empty(6)

#19

def calculate_mean(list):
    som = 0
    for num in list:
        som += num
    mean = som/len(list)
    return mean
print(calculate_mean([10, 5, 1, 4]))

def calculate_median(list):
    sort = sorted(list)
    if len(list) % 2 == 0:
        two_num = sort[(len(list)//2) -1: (len(sort)//2) + 1]
        result = 0
        for num in two_num:
            result += num
        return result/2
    else:
        num_one = sort[(len(sort)//2) : (len(sort)//2) + 1]
        return num_one[0]
print(calculate_median([8, 5, 2]))

def calculate_moda(list):
    my_variables = dict()
    for num in list:
        my_variables[num] = 0
    for num in list:
        my_variables[num] += 1
    alcual_bigger = 0
    last_value = 0
    for num in my_variables:
        if my_variables[num] > last_value:
            alcual_bigger = num
            last_value = my_variables[num]
    print(f'a moda é {alcual_bigger}')
calculate_moda([1,2,3,3,4,5,1,3])

def calculate_range(list):
    return max(list) - min(list)
print(calculate_range([1, 5, 9, 2, 4, 0]))

def calculate_variance(list):
    mean = calculate_mean(list)
    list_squared = []
    sum = 0
    for num in list:
        deviation = num - mean
        list_squared.append(math.pow(deviation, 2))
    for num in list_squared:
        sum += num
    return sum/(len(list_squared) -1) 
print(calculate_variance([46, 69, 32, 60, 52, 41]))

def calculate_std(list):
    variance = calculate_variance(list)
    return math.sqrt(variance)
print(calculate_std([46, 69, 32, 60, 52, 41]))

#20
def is_prime(num):
    return num % 2 == 0

#21
def is_unique(list):
    set_list = set(list)
    if len(set_list) == len(list):
        return True
    return False
print(is_unique([46, 69, 32, 60, 52, 41]))

#22
def is_same_type(list):
    before_type = type(list[0])
    for i in list:
        if type(i) != before_type:
            return False
        before_type = type(i)
    return True

print(is_same_type([10, 503, 22, '1233', 11]))
