import numpy
import webbrowser

url_list = ['http://www.python.org', 'https://www.w3schools.com/python/ref_list_extend.asp', 'https://www.programiz.com/python-programming/methods/string/count']
for url in url_list:
    webbrowser.open_new_tab(url)

