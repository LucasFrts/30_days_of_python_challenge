import requests
from bs4 import BeautifulSoup
import json
def scrapp_one(urll):
    response = requests.get(urll)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        wrapper = soup.find_all('div', class_="facts-wrapper")
        website_information = []
        for lista in wrapper:
            my_dict = dict()
            my_dict['category'] = lista.find('h5').get_text()
            for li in lista.find_all('li'):
                my_dict[li.find('p').get_text()] = li.find('span').get_text()
            website_information.append(my_dict)
        with open('./boston-university-facts-stats.json', 'w') as f:
            f.write(json.dumps(website_information, indent=4))
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
# scrapp_one(url)

def scrapp_two(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table', {'cellpadding': '5', 'border':'1'})
        list_content= []
        header= []
        for table in tables:
            list_of_tr= []
            for index, tr in enumerate(table.find_all('tr')):
                print(index)
                if index == 0:
                    header = [i.find('p').get_text() for i in tr.find_all('td')]
                else:
                    my_dict = dict()
                    for idx,text in enumerate(tr.find_all('p')):
                        if len(tr.find_all('p')) > 3:
                            my_dict[header[idx]] = text.get_text()
                    if len(my_dict) > 0:
                        list_of_tr.append(my_dict)
            list_content.append(list_of_tr)
        with open('./datasets.json', 'w') as f:
            f.write(json.dumps(list_content, indent=4))
url = 'https://archive.ics.uci.edu/ml/datasets.php'
# scrapp_two(url)
import re
def scrapp_three(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table', {'style': 'text-align:center;'})
        list_of_content= []
        for table in tables:
            for index,tr in enumerate(table.find_all('tr')):
                if index == 0:
                    regex = r'(\n)?([.])?(\[\d+\])?(\[\w+\])?'
                    header = [re.sub(regex,'',td.get_text()) for td in tr.find_all('th')]
                    print(header)
                else:
                    my_dict = dict()
                    lista = tr.find_all('td')
                    for idx, text in enumerate(lista):
                        if idx == 0:
                            my_dict[header[idx]] = index +1
                        elif text.find_all('b'):
                            my_dict[header[idx]] = lista[idx - 1].get_text()
                            # print(header[idx])
                            # print(text.find('b').find('a').get_text())
                        else:
                            my_dict[header[idx]] = lista[idx - 1].get_text()

                    list_of_content.append(my_dict)
        with open('./list_of_presidents.json', 'w') as f:
            f.write(json.dumps(list_of_content, indent=4))
scrapp_three('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')

