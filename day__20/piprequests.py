import requests

# url = 'https://www.w3.org/TR/png/iso_8859-1.txt'
# response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.text)

url = 'https://randomuser.me/api/'
response = requests.get(url).json()
# print(response)
# print(response.status_code)
# print(response.headers)

person = response['results'][0]
print(person)
print(person['gender'])