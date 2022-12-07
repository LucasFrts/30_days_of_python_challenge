# age = int(input('Insira a sua idade: '))
# if (age >= 18):
#     print("You're old enough to drive!")
# elif (age > 0):
#     print(f'You need to wait for more {18 - age} years!')
# else:
#     print('Invalid age')


# my_age = 21

# your_age = int(input('Insira a sua idade: '))
# if(my_age > your_age):
#     if(my_age - your_age > 1):
#         print(f'Sou {my_age - your_age} anos mais velho')
#     else:
#         print(f'Sou {my_age - your_age} ano mais velho')
# else:

#     if(your_age - my_age > 1):
#         print(f'Você é {your_age - my_age} anos mais velho')
#     else:
#         print(f'Você é {your_age - my_age} ano mais velho')



# number_a = int(input('Insira o valor A: '))
# number_b = int(input('Insira o valor B: '))

# if(number_a > number_b):
#     print(f'{number_a} is bigger than {number_b}')
# elif(number_b > number_a):
#     print(f'{number_a} is smaller than {number_b}')
# else:
#     print(f'{number_a} is equal to {number_b}')

# score = int(input('Insira o score: '))
# if(score < 50):
#     print('Nota F')
# elif(score >= 50 and score < 60 ):
#     print('Nota D')
# elif(score >= 60 and score < 70):
#     print('Nota C')
# elif(score >= 70 and score < 90 ):
#     print('Nota B')
# else:
#     print('Nota A')

# autumn = ['September', 'October', 'November']
# winter = ['December', 'January', 'February']
# spring = ['March', 'April', 'May']
# summer = ['June', 'July', 'August']

# mounth = input('Type a mounth: ')
# mounth = mounth.capitalize()

# if(mounth in autumn):
#     print(f'{mounth} makes part of the autumn')
# elif(mounth in winter):
#     print(f'{mounth} makes part of the winter')
# elif(mounth in spring):
#     print(f'{mounth} makes part of the spring')
# elif(mounth in summer):
#     print(f'{mounth} makes part of the summer')
# else:
#     print('Invalida mounth')


# import sys

# fruits = ['banana', 'orange', 'mango', 'lemon']

# fruit = input('Insira uma fruta: ')
# for frutas in fruits:
#     if frutas.capitalize() == fruit.capitalize():
#         print(f'{fruit} makes part of the {frutas}')
#         sys.exit()

# fruits.append(fruit)
# print(fruits)


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'first_name' in person:
    print(person['skills'][len(person['skills'])//2:len(person['skills'])//2 + 1])
if 'skills' in person:
    print('Python' in person['skills'])

if len(person['skills']) == 2 and 'Javascript' in person['skills'] and 'React' in person['skills']:
    print('person is a frontend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('person is a fullstack developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('person is a backend developer')
else:
    print('unknown title')


print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He {"is" if person["is_married"] else "is not"} married')