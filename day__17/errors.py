def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst =[1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. he is {age} years old'
dct = {'name': 'Lucas', 'country': 'Brazil', 'city' : 'Macapá', 'age': 88}
print(unpacking_person_info(**dct))

def sum_all(*args):
    s = 0 
    for i in args:
        s+=i
    return s

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name = 'Lucas', country = 'Brazil', city = 'Macapá', age = 22))

lst_one = [1,2,3]
lst_two = [4,5,6,7]
lst = [0, *lst_one, *lst_two]
print(lst)

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']

nordic_countries = [*country_lst_one, *country_lst_two]

print(nordic_countries)

for index, item in enumerate([20,30,40]):
    print(index, item)

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']

fruit_and_veges = []
for f, v in zip(fruits, vegetables):
    fruit_and_veges.append({'fruit': f, 'veg': v})

print(fruit_and_veges)