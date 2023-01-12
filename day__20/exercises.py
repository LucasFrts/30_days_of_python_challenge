import requests
import re
import numpy as np
from tabulate import tabulate
from bs4 import BeautifulSoup
import os
def quantify_paragraph(word, paragraph):
    regex = rf'([^\w]{word}[^\w])|(^{word}[^\w])|([^\w]{word}$)'
    results = re.findall(regex, paragraph)
    return (len(results), word)

# 1
def romeo_and_juliet():
  response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
  if response.status_code == 200:
      romeo_and_juliet = response.text.lower()
      regex = r'[^A-Za-z\s]'
      text_cleaned = re.sub(regex, '', romeo_and_juliet)
      regex = r'[\s]{2,}'
      new_text = re.sub(regex, ' ', text_cleaned)
      all_words = new_text.split(' ')
      unique_words = set(all_words)
      list_of_words = []
      for word in unique_words:
          list_of_words.append(quantify_paragraph(word, new_text))
      list_of_words.sort(reverse=True)
      top_ten = [list_of_words[i] for i in range(9)]
      print(top_ten)
# romeo_and_juliet()

def cats_api():
    response = requests.get('https://api.thecatapi.com/v1/breeds')
    if response.status_code == 200:
        cats_list = response.json()
        cats_weight = [eval(re.sub('[-]','+',i['weight']['metric']))/2 for i in cats_list]
        numpy_w_array = np.array(cats_weight)
        w_min = np.amin(numpy_w_array)
        w_max = np.amax(numpy_w_array)
        w_mean = np.mean(numpy_w_array)
        w_median = np.median(numpy_w_array)
        print(f'min: {w_min} - max: {w_max} - mean: {w_mean} - median: {w_median}')
        cats_lifespan = [eval(re.sub('[-]', '+', i['life_span']))/2 for i in cats_list]
        numpy_l_array = np.array(cats_lifespan)
        l_min = np.amin(numpy_l_array)
        l_max = np.amax(numpy_l_array)
        l_mean = np.mean(numpy_l_array)
        l_median = np.median(numpy_l_array)
        print(f'min: {l_min} - max: {l_max} - mean: {l_mean} - median: {l_median}')

        cats_origin = [i['origin'] for i in cats_list]
        numpy_origin_array = np.array(cats_origin)
        unique_origin, counts_elements = np.unique(numpy_origin_array, return_counts=True)
        print("Frequency of origin:")
        print(tabulate([[unique_origin[i], counts_elements[i]] for i in range(len(unique_origin))], headers=["Origin", "Frequency"], tablefmt="orgtbl"))

        cats_breed = [i['name'] for i in cats_list]
        numpy_breed_origin = np.array(cats_breed)
        unique_breed, counts_breed = np.unique(numpy_breed_origin, return_counts=True)
        print('Frequency of Breed')
        print(tabulate([[unique_breed[i], counts_breed[i]]for i in range(len(unique_breed))], headers=["Breed", "Frequency"], tablefmt="orgtbl"))
# cats_api()

def web_scrapping():
    response = requests.get('https://archive.ics.uci.edu/ml/datasets.php').text
    soup = BeautifulSoup(response)
    with open('./scrapped.html', 'w') as f:
        f.write(soup.prettify())
web_scrapping()