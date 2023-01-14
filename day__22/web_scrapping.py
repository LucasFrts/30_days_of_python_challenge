import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
# status = response.status_code
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)

tables = soup.find_all('table', {'cellpadding': '3'})
list_of_td = []
print(len(tables))
# for table in tables:
#     for td in table.find('tr').find_all('td'):
        # print(td)
        # list_of_td.append(td)
# print(len(list_of_td))
# import json 
# json.dumps()