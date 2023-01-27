from flask import Flask, render_template
from pymongo import MongoClient
from bson import ObjectId
import dns
import os



# Mongo DataBase local
client = MongoClient("mongodb://localhost:27017/")

print(client.list_database_names())

# Creating database
db = client.thirty_days_of_python

# Creating collection and pushing info
db['Student'].insert_one({'name':'Lucas', 'country': 'Brazil', 'city': 'Macapá', 'age': 999})

print(client.list_database_names())
# print(db['Student'])

students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
]
# Inserting many documents
# for student in students:
#     db['Student'].insert_one(student)

# finding one Document

# student = db['Student'].find_one()
# print(student)

# Finding one by id
# student = db['Student'].find_one({'_id': ObjectId('63d3da6190411b2292191c49')})
# print(student)

# find all ocurrences
students = db['Student'].find()
for student in students:
    print(student)

# choosing fields to include (0 not include, 1 include)
students = db['Student'].find({}, {'_id': 0, 'name': 1, 'country':1})
for student in students:
    print(student)

# find with Query
query = {
    'country': 'Finland'
}
students = db['Student'].find(query)
for student in students:
    print(student)

query = {
    'city': 'Stockholm'
}
students = db['Student'].find(query)
for student in students:
    print(student)

# find Query with modifiers

query = {
    'country': 'Finland',
    'city': 'Helsinki'
}
students = db['Student'].find(query)
for student in students:
    print(student)

query = {
    "age":{"$gt":30}
}
students = db['Student'].find(query)
for student in students:
    print(student)

# limit documents
students = db['Student'].find().limit(3)
for student in students:
    print(student)

# find with sort
students = db['Student'].find().limit(10).sort('name')
for student in students:
    print(student)
# descending order
students = db['Student'].find().limit(10).sort('name', -1)
for student in students:
    print(student)

students = db['Student'].find().limit(10).sort('age', -1)
for student in students:
    print(student)

# Update with query
query = {
    "age": 999
}
new_value = {
    '$set': {'age': 21}
}
# to update one
db['Student'].update_one(query, new_value)

# to update many
db['Student'].update_many(query, new_value)
students = db['Student'].find().sort('age', -1)
for student in students:
    print(student)

# Delete one from document
query = {
    'name':'John'
}
db['Student'].delete_one(query)

for student in db['Student'].find():
    print(student)

# lets check the result if the age is modified
for student in db['Student'].find():
    print(student)


# Delete many
db['Student'].delete_many(query)

for student in db['Student'].find():
    print(student)

# drop database
db['Student'].drop()
print(db)
app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 9002))
    app.run(debug=True, host='0.0.0.0', port=port)