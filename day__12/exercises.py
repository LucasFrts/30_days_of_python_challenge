from random import randint, shuffle
from string import *

#1
def random_user_id():
    opt = hexdigits
    id = ''
    for i in range(0, 6):
        if i == 0:
            id += str(opt[randint(1, 21)])
            continue
        id += str(opt[randint(0, 21)])
    return id  
# print(random_user_id())

#2
def user_id_gen_by_user():
    opt = hexdigits
    ids = []
    num_char = int(input('Insira a quantidade de caracteres: '))
    num_ids = int(input('Insira a quantidade de ids: '))
    for i in range(0, num_ids):
        id = ''
        for j in range(0, num_char):
            if j == 0:
                id += str(opt[randint(1, 21)])
                continue
            id += str(opt[randint(0, 21)])
        ids.append(id)
    return ids        
# print(user_id_gen_by_user())

#3
def rgb_color_gen():
    return 'rgb({}, {}, {})'.format(randint(0, 255), randint(0, 255), randint(0, 255))
# print(rgb_color_gen())

#4
def list_of_hexa_colors(param = 1):
    opt = hexdigits
    list = []
    for i in range(0, param):
        list.append('#{}{}{}{}{}{}'.format(opt[randint(0, 15)], opt[randint(0, 15)], opt[randint(0, 15)], opt[randint(0, 15)], opt[randint(0, 15)], opt[randint(0, 15)]))
    return list
# print(list_of_hexa_colors(9))

#5
def list_of_rgb_colors(param = 1):
    list = []
    for i in range(0, param):
        list.append(rgb_color_gen())
    return list
# print(list_of_rgb_colors(6))

#6
def generate_colors(type, quantity):
    if type.lower() == 'rgb':
        arr = list_of_rgb_colors(quantity)
    elif type.lower() == 'hexa':
        arr = list_of_hexa_colors(quantity)
    else:
        print('Tipo de operação não definida')
        return
    return arr
# print(generate_colors('rgb', 1))

#7
def shuffle_list(list):
    shuffle(list)
    return list
# print(shuffle_list(['a', 'b', 'c', 1, 2 ,3]))

#8
def seven_random():
    numbers = set()
    while len(numbers) < 7:
        numbers.add(randint(0, 9))
    return numbers
print(seven_random())