# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)

#Second way: list comprehension
lst = [i for i in language]
print(type(lst))
print(lst)

#generating numbers
numbers = [i for i in range(11)]
print(numbers)

#mathematics operations in list comprehension
squares = [i * i for i in range(100)]
print(squares)

#its also possible to make a list of tuples
numbers = [(i, i*i) for i in range(11)]
print(numbers)

#generating even numbers

even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

#generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

#filter numbers: let's filter out positive even numbers from list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_numbers_even_numbers = [number for number in numbers if number >= 0 and number % 2 == 0]
print(positive_numbers_even_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)