# class Person:
#     pass
# print(Person)

# p = Person()
# print(p)

class Person:
    def __init__(self, first_name='Dear', last_name='Programmer', age='999', country='Inner Solar System', city='Earth'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city
        self.skills = []
    def person_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}'
    def add_skill(self, skillname):
        self.skills.append(skillname)

p = Person('Lucas', 'Freitas', 21, 'Brazil', 'Macapá')
w = Person()
# print(p.first_name)
# print(p.last_name)
# print(p.age)
# print(p.country)
# print(p.city)
print(p.person_info())
print(w.person_info()) 
print(p.skills)
p.add_skill('Python')
print(p.skills)

# class Student(Person):
    # pass
# 
# s1 = Student('Maria', 'Eduarda', '16', 'Brazil', 'Rio de Janeiro')
# print(s1.person_info())
# s1.add_skill('Markeding Digital')
# print(s1.skills)

class Student(Person):
    def __init__(self, first_name='Lucas', last_name='Freitas', age=21, country='Brazil',  city='Macapá', gender='male'):
        self.gender = gender
        super().__init__(first_name, last_name, age, country, city)
    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'she'
        return f'{self.first_name} {self.last_name} is {self.age} years old. {gender} lives in {self.city}, {self.country}'

s1 = Student('Fracirley', 'Mestre', 24, 'Brazil', 'Macapá')
s1.add_skill('Python')
print(s1.skills)
print(s1.person_info())