#1
'''
Map is used to iterate an list and return another list from the first list
Filter is used to iterate an list and return another list from an boolean condition
Reduce is also used to iterate an list, but it return an single value
'''
#2
'''
Closures is an function that declare another function inside
HOF is an function that recieves as parameter another function
Decorator is an design pattern that consist in the use of an HOF to add functionalites to another existing function
'''

#3
#4
#5
#6
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)
for name in names:
    print(name)
for number in numbers:
    print(number)

#7
uppercased_countries = map(lambda x: x.upper(), countries)
print(list(uppercased_countries))
#8
numbers_squared = map(lambda x:x ** 2, numbers)
print(list(numbers_squared))
#9
names = list(map(lambda x: x.upper(), names))
print(names)
#10
def is_land_country(x):
    return 'land' in x
land_countries = filter(is_land_country, countries)
print(list(land_countries))
#11
def six_char_string(x):
    return len(x) == 6
six_characters_countries = filter(six_char_string, countries)
print(list(six_characters_countries))
#12
countries_starting_with_e = filter(lambda x:(x[0] == 'E'), countries)
print(list(countries_starting_with_e))
#13
upper_countries_starting_with_e = map(lambda x: x.upper(),list(filter(lambda x: (x[0] == 'E'), countries)))
print(list(upper_countries_starting_with_e))
#14
my_list = ['teste', 1, 'alo',  ['teste', 2, 3], 'number']
string_list = filter(lambda x: (type(x) == str), my_list)
print(list(string_list))
#15
from string import *
from functools import *
def sum_iterables(x, y):
    return int(x) + int(y)
soma  = reduce(sum_iterables, numbers)
print(soma)
#16
def concatenate_string(x, y):
    return str(x) + ' ' + str(y)
contries_string = reduce(concatenate_string, countries) + ' are north European countries'
print(contries_string)
#17
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

filtered_countries = filter(lambda x:('land' in x), countries)
print(list(filtered_countries))

#18
from string import *
letters = set(ascii_letters.upper())
def countries_by_letter(letters, countries):
    my_dict = dict()
    for letter in letters:
        my_dict[letter] = len(list(filter(lambda x: (x[0] == letter), countries)))
    return my_dict
countries_letter_dict = countries_by_letter(letters, countries)
print(countries_letter_dict)
