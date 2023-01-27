from flask import Flask, Response, request
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from datetime import datetime
import os, json


    # student_list =  [
    #     {
    #         'name':'Asabeneh',
    #         'country':'Finland',
    #         'city':'Helsinki',
    #         'skills':['HTML', 'CSS','JavaScript','Python']
    #     },
    #     {
    #         'name':'David',
    #         'country':'UK',
    #         'city':'London',
    #         'skills':['Python','MongoDB']
    #     },
    #     {
    #         'name':'John',
    #         'country':'Sweden',
    #         'city':'Stockholm',
    #         'skills':['Java','C#']
    #     }
    # ]

app = Flask(__name__)

# Http messages
not_found = {'message': 'Sem resultados para a pesquisa', 'httpcode': 204}
cad_success = {'message': 'Cadastro realizado com sucesso', 'httpcode': 201}
att_success = {'message': 'Atualização realizada com sucesso', 'httpcode': 201}
delete_err = {'message': 'Estudante inexistente', 'httpcode': 204}
delete_sucess = {'message': 'Estudante deletado com sucesso', 'httpcode': 200}
# Mongo config

client = MongoClient("mongodb://localhost:27017")

db = client.thirty_days_of_python

@app.route("/api/ThirtyDaysOfPython/Students", methods = ['GET'])
def students():
    try: 
        students_list = [ student for student in db['students'].find({}, {'_id': 0, 'created_at': 0})]
        return Response(json.dumps(students_list), mimetype='application/json')
    except Exception:
        return Response(json.dumps(not_found), mimetype='application/json')

@app.route("/api/ThirtyDaysOfPython/Student/<id>", methods = ['GET'])
def student(id):
    try:
        single_student = db['students'].find_one({'id' : int(id)}, {'_id': 0, 'created_at': 0})
        if single_student == None:
            raise Exception
        return Response(dumps(single_student), mimetype='application/json')
    except Exception:
        return Response(json.dumps(not_found), mimetype='application/json')
         
@app.route("/api/ThirtyDaysOfPython/Student", methods = ['POST'])
def new_student():
    try:
        max_students = len(list(db['students'].find()))
        data = json.loads(request.data)
        name = data['name']
        country = data['country']
        city = data['city']
        skills = ", ".join(data['skills'])
        bio = data['bio']
        birthyear = data['birthyear']
        created_at = datetime.now()
        student = {
            'id' : max_students + 1,
            'name': name,
            'country': country,
            'city': city,
            'skills':skills,
            'bio': bio,
            'birthyear': birthyear,
            'created_at': created_at
        }
        db['students'].insert_one(student)
        return Response(dumps(cad_success), mimetype='application/json')
    except Exception as err:
        return Response(dumps({'message': err, 'httpcode': 500}), mimetype='application/json')

@app.route("/api/ThirtyDaysOfPython/Student/<id>", methods = ['PUT'])
def update_student(id):
    try:
        data = json.loads(request.data)
        if 'skills' in data:
            data['skills'] = ", ".join(data['skills'])
        print(data)
        db['students'].update_one({'id': int(id)}, {'$set': data})
        return Response(dumps(att_success), mimetype='application/json')
    except Exception as err:
        return Response(dumps({'message': err, 'httpcode': 500}), mimetype='application/json')

@app.route("/api/ThirtyDaysOfPython/Student/<id>", methods = ['DELETE'])
def delete_student(id):
    try:
        db['students'].find_one_and_delete({'id': int(id)})
        return Response(dumps(delete_sucess), mimetype='application/json')
    except: 
        return Response(dumps(delete_err), mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 7001))
    app.run(debug=True, host="0.0.0.0", port=port)