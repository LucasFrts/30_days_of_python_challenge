a = 3
if a > 0:
    print('A is apositive number')


if a < 0:
    print('A is anegative number')
else:
    print('A is a positive number')

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

a = 3

print('A is positive') if a > 0 else print('A is negative')

a = 0
if a  > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

if a > 0 and a % 2 == 0:
    print('A is even and a postive integer')
elif a > 0 and a%2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

user = 'James'
acess_level = 3
if user == 'Admin' or acess_level >= 4:
    print('Acess granted')
else:
    print('Acess denied')
    