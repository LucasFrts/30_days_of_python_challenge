import statistics
import uuid
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class UseStatiscs():
    def __init__(self, lista):
        lista.sort()
        self.data = lista
    def count(self):
        return f'{len(self.data)}'
    def sum(self):
        return f'{sum(self.data)}'
    def min(self):
        return f'{min(self.data)}'
    def max(self):
        return f'{max(self.data)}'
    def range(self):
        return f'{eval(self.max()) - eval(self.min())}'
    def mean(self):
        return f'{eval(self.sum())/eval(self.count())}'
    def median(self):
        lista = self.data
        return f'{lista[len(self.data)//2]}'
    def mode(self):
        numbers = self.frequency()
        alcual_bigger = 0
        last_value = 0
        for num in numbers:
            if numbers[num] > last_value:
                alcual_bigger = num
                last_value = numbers[num]
        return f'{alcual_bigger}'
    def frequency(self):
        numbers = dict()
        for num in self.data:
            numbers[num] = 0
        for num in self.data:
            numbers[num] += 1
        return numbers
    
    def variance(self):
        squared_differences = [(i - eval(self.mean()))**2 for i in self.data]
        sample_variance =  sum(squared_differences)/(len(squared_differences) -1)
        return f'{sample_variance}'
    
    def std(self):
        return f'{eval((self.variance()))**1/2}'
    def freq_dist(self):
        numbers = self.frequency()
        keys = numbers.keys()
        return [(key, numbers[key]) for key in keys]
    def describe(self):
        print('Count:', self.count())
        print('Sum: ', self.sum())
        print('Min: ', self.min())
        print('Max: ', self.max())
        print('Range: ', self.range())
        print('Mean: ', self.mean())
        print('Median: ', self.median())
        print('Mode: ', self.mode())
        print('Standard Deviation: ', self.std())
        print('Variance: ', self.variance())
        print('Frequency Distribution: ', self.freq_dist())
data = UseStatiscs(ages)
# data.describe()

from tabulate import tabulate
class Moviment():
    def __init__(self, value, description):
        self.id = uuid.uuid4()
        self.value = value
        self.description = description

class PersonAccount():
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.expanses = set()
        self.incomes = set()
        self.balance = 0
    def total(self, sets):
        values = [i.value for i in sets]
        return sum(values)
    def total_income(self):
        print(f'Total income: {self.total(self.incomes)}')
        detailed = input('Abrir detalhes? ("S"/"n")')
        self.total_income_detailed() if detailed.upper() == 'S' else None
    def total_income_detailed(self):
        for income in self.incomes:
            print(f"Value: {income.value}, description: {income.description}")
    def add_income(self, value, description):
        obj = Moviment(value, description)
        self.incomes.add(obj)
        self.balance = self.balance + value
    def total_expanse(self):
        print(f'Total expanses: {self.total(self.expanses)}')
        detailed = input('Abrir detalhes? ("S"/"n")')
        self.total_expanse_detailed() if detailed.upper() == 'S' else None
    def total_expanse_detailed(self):
        for expanse in self.expanses:
            print(f"Id: {expanse.id}, Value: {expanse.value}, description: {expanse.description}")
    def add_expanse(self, value, description):
        obj = Moviment(value, description)
        self.expanses.add(obj)
    def account_info(self):
        print(tabulate([[self.user_name(), self.balance, self.total((self.incomes)), self.total((self.expanses)), self.id]], headers=["Name", "Balance", "Incomes", "Expanses", "id"]))
    def user_name(self):
        return f'{self.first_name} {self.last_name}'
    # def pay_debit(self, id):
        # expanse = filter()

person = PersonAccount('Lucas', 'Freitas', '05050678200')
person.account_info()
person.add_income(1600, 'Salário')
person.add_income(150, 'divida amigo')
person.add_expanse(450, 'faculdade')
person.add_expanse(257, 'bar do seu roberto')
person.account_info()
person.total_expanse()