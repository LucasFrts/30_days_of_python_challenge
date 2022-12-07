company = "Coding For All"

print(company)

print(len(company))

company = company.upper()
print(company)

company = company.lower()
print(company)

company = company.title()
print(company)

company = company.swapcase()
print(company)

company = company.capitalize()
print(company)

# arr = company.split()
# company = company.replace(arr[0], '')
# print(company)

company.find('coding')

company = company.replace('all', 'python')
print(company)

'Python for Everyone'.replace('Everyone', 'All')

company = company.replace('python', 'All')
company.find('C')

company = company.title()
company.find('F')

company.rfind('l')


'You cannot end a sentence with because because because is a conjunction'.find('because')
'You cannot end a sentence with because because because is a conjunction'.rfind('because')
'You cannot end a sentence with because because because is a conjunction'.replace('because ', '')
'Coding For All'.startswith('Coding')
'Coding For All'.startswith('coding')
'    Coding For All   '.strip(' ')
'thirty_days_of_python'.isidentifier()
' - '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])

print("I am enjoying this challenge.\nI just wonder what is next")

print("Name\tAge\tCountry\tCity\nLucas\t21\tBrazil\tMacapá")

radius = 10
area = 3.14*radius**2
print('The area of circle with radius {} is {} meters square'.format(radius, area))

a = 8
b = 6

sentence = f'''
{a} + {b} = {a+b}
{a} - {b} = {a-b}
{a} * {b} = {a*b}
{a} / {b} = {a/b:.2f}
{a} % {b} = {a%b}
{a} // {b} = {a//b}
{a} ** {b} = {a**b}
'''
print(sentence)