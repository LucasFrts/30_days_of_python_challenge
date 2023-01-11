# 1
def print_lines_and_words(arg):
    with open(arg) as f:
        text = f.read()
        number_of_lines = len(text.splitlines())
        number_of_words = len(text.split(' '))
        print(f'Number of lines: {number_of_lines}')
        print(f'Number of words: {number_of_words}')

# print_lines_and_words('./exercises_files/obama_speech.txt')
# print_lines_and_words('./exercises_files/michelle_obama_speech.txt')
# print_lines_and_words('./exercises_files/melina_trump_speech.txt')

# 2
import re
def quantity_of_item(word, paragraph):
    regex = rf'{word}[\S]'
    results = re.findall(regex, paragraph, re.I)
    return (len(results), word)

import json
def most_spoken_languages(path, quantity):
    with open(path) as f:
        json_text = f.read()
        json_dict_list = json.loads(json_text)
        list_of_lists = list(map(lambda x: x['languages'], json_dict_list))
        list_of_languages = [i for row in list_of_lists for i in row]
        set_of_languages = set(list_of_languages)
        stringified = ", ".join(lang for lang in list_of_languages)
        list_of_tuples = []
        for word in list(set_of_languages):
            list_of_tuples.append(quantity_of_item(word, stringified))
        list_of_tuples.sort(reverse=True)
        return [i for index, i in enumerate(list_of_tuples) if index < quantity]

# print(most_spoken_languages('./exercises_files/countries_data.json', 10))

# 3
def most_populated_countries(path, quantity):
    with open(path) as f:
        json_text = f.read()
        json_dict_list = json.loads(json_text)
        json_dict_list.sort(key = lambda x: x['population'], reverse=True)
        return [ {'name' : i['name'], 'population':i['population']} for index, i in enumerate(json_dict_list) if index < quantity]
# print(most_populated_countries('./exercises_files/countries_data.json', 10))

# 4
def extract_incoming_email(path):
    with open(path) as f:
        txt = f.read()
        regex = r'[A-Z.]+@[A-Z.]+'
        list_of_email = re.findall(regex, txt)
        return set(list_of_email)
# print(extract_incoming_email('./exercises_files/email_exchanges_big.txt'))

# 5
def unique_words_of_text(paragraph):
    regex = r'[\s][A-Za-z]+[\s]'
    words = re.findall(regex, paragraph)
    unique_words = list(set(words))
    return unique_words
def find_most_comon_words(arg, quantity):
    regex = r'^./'
    result = re.findall(regex, arg, re.I)
    if len(result) > 0:
        with open(arg) as f:
            txt = f.read()
            txt = txt.upper()
            unique_words = unique_words_of_text(txt)
            paragraph = txt
    else:
        unique_words = unique_words_of_text(arg)
        paragraph = arg
    result_list = []
    for words in unique_words:
        result_list.append(quantity_of_item(words, paragraph))
    result_list.sort(reverse=True)
    return [i for index, i in enumerate(result_list) if index < quantity]

#6
# print(find_most_comon_words('./exercises_files/obama_speech.txt', 10))
# print(find_most_comon_words('./exercises_files/michelle_obama_speech.txt', 10))
# print(find_most_comon_words('./exercises_files/melina_trump_speech.txt', 10))


# 7
import sys
sys.path.insert(1, './exercises_files')

from stop_words import aux_words
def clean_text(arg):
    regex = r"([0-9.,!?@#$%&;+=$-_])|([\n])"
    return re.sub(regex, "", arg)
def remove_suport_words(arg):
    words_list = arg.split(' ')
    helper_words = aux_words()
    helper_words.extend(['—', 'th', 'r','e', 'ou', 'es', 'nd', 'ow', 'ut', 'ing', '', 'od'])
    without_helper = set(filter(lambda x: x not in helper_words, words_list))
    return list(without_helper)

def check_similarity(comparator, comparable, quantity):
    try:
        with open(comparator) as f:
            txt = f.read()
            cleaned_text = clean_text(txt)
            valid_words = remove_suport_words(cleaned_text)
        with open(comparable) as f:
            text = f.read()
        # count valid words in text
        result_list = []
        for word in valid_words:
            result_list.append(quantity_of_item(word, text))
        result_list.sort(reverse=True)
        return [i for index, i in enumerate(result_list) if index < quantity] 
    except:
        print('sim')

if __name__ == '__main__':
    # relation = check_similarity('./exercises_files/michelle_obama_speech.txt', './exercises_files/melina_trump_speech.txt', 10)
    # print(relation)

    # 8
    # print(find_most_comon_words('./exercises_files/romeo_and_juliet.txt', 10))
    import csv
    with open('./exercises_files/hacker_news.csv') as f:
        javascript = 0;java = 0;python = 0
        csv_reader = csv.reader(f, delimiter=',')
        lista = []
        for row in csv_reader:
            lista.extend( [it for item in row for it in item.split(' ')])
        for i in lista:
            if i.lower() == 'javascript': javascript += 1
            elif i.lower() == 'java': java += 1
            elif i.lower() == 'python': python += 1
        print('python', python)
        print('javascript', javascript)
        print('java', java)

