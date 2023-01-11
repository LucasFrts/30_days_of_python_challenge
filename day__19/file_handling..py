# f = open('./files/reading_file_example.txt')
# print(f)
# txt = f.read().splitlines()
# print(type(txt))
# print(txt)
# f.close()

with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

with open('./files/reading_file_example.txt', 'a') as f:
    f.write('\nThis is text to be appended at end')

with open('./files/writing_file_example.txt', 'w') as f:
    f.write('This text will be written in a newly created file')

import os

if(os.path.exists('./files/example.txt')):
    os.remove('./files/example.txt')
else:
    print('The file does not exists')

import json
# json to dictionary

person_json = '''{
    "name":"Lucas",
    "country":"Brazil",
    "city":"Macapá",
    "skills":["Javascript", "React", "VueJs", "Python"]
}'''

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# dictionary to json

person = {
    "name":"Lucas",
    "country":"Brazil",
    "city":"Macapá",
    "skills":["Javascript", "React", "VueJs", "Python"]
}
json_person = json.dumps(person, indent=4)
print(type(json_person))
print(json_person)

# saving as json file
with open('./files/json_example.json', 'w') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

# file with csv extension
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_cont = 0
    for row in csv_reader:
        if line_cont == 0:
            print(f'Coluumn names are:{", ".join(row)}')
            line_cont += 1
        else:
            print(f'\t {row[0]} is a teacher. He lives in {row[1]}, {row[2]}')
            line_cont += 1
    print(f'Number of lines: {line_cont}')
