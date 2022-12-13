#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [number for number in numbers if number <= 0]
print(negative_and_zero)

#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatterned_list = [number for array in list_of_lists for row in array for number in row]
print(flatterned_list)

#3
list_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_tuples)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#4
new_list = [[item[0].upper(), item[0][:3].upper(), item[1].upper()] for row in countries for item in row]
print(new_list)
#5
new_countries = [{'country': item[0].upper(), 'city': item[1].upper()} for row in countries for item in row]
print(new_countries)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_names = [name[0] + ' ' + name[1] for row in names for name in row]
print(new_names)

#7
calculate_slope = lambda x_ini, x_end, y_ini, y_end: (x_end - x_ini)/(y_end - y_ini)
print(calculate_slope(10,6,4,1))