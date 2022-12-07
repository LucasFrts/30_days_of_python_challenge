# Day 2:30 Days of Python programming

first_name = input('Digite o primeiro nome: ')
last_name = input('Digite o ultimo nome: ')
full_name = first_name + ' ' + last_name
country = input('Digite o país: ')
city = 'Macapá'
age = input('Digite a idade: ')
year = 2022
is_married = True
is_true = False
is_light_on = False
is_father_or_mother = False; is_kid = False

print('is father or mother : ', is_father_or_mother)
print('is kid : ', is_kid)

#exercices

print(first_name)
print(last_name)
print(country)
print(age)

print(len(first_name))
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))

print(len(first_name) == len(last_name))

num_one = 5
num_two = 4

num_one_plus_two = num_one + num_two

print(num_one_plus_two)

num_one_sub_two = num_one - num_two

print(num_one_sub_two)

num_one_div_two = num_one/num_two

print(num_one_div_two)

module_num_two_num_one = num_two%num_one

print(module_num_two_num_one)

expoent = num_one.__pow__(num_two)

print(expoent)

floor_division = num_one//num_two

print(floor_division)

radius = float(input('Digite o raio do circulo'))


area_of_circle = 3.14*radius**2

print('Area do circulo: ', area_of_circle)

circum_of_circle = 2*radius*3.14

print('Circumferencia do circulo', circum_of_circle)
