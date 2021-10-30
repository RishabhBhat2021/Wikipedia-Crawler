from bs4 import BeautifulSoup
import requests

import re

home_page = "https://en.wikipedia.org/"

search = str(input("Enter anything to search: "))

words_check = [search]

while search != "Philosophy" and words_check.count(search) <= 1:
    search_page = home_page + "wiki/" + search

    request = requests.get(search_page)
    content = request.text
    soup = BeautifulSoup(content, 'lxml')

    first_paragraph = soup.find('p', class_=None)

    # Find all paragraphs (i.e. 'p' tags)
    for paras in soup.find_all('p', class_=None):
        try:
            # Check wheather the paragraph is first or not
            if paras.b.get_text() == search.capitalize(): 
                # print(paras.b.get_text())
                first_paragraph = paras
        except:
            pass

    # Remove the hyperlinks which are in brackets
    first_paragraph_s = str(first_paragraph)
    string=re.sub("\(.*?\)","()",first_paragraph_s) 
    cut_para = BeautifulSoup(string, 'lxml')

    try:
        for tag in cut_para.find_all('a'):
            if tag.text[0] == "[":
                tag.decompose()
    except:
        pass

    # print(cut_para.find('a'))

    try:
        if cut_para.find('a') != None:
            search = cut_para.find('a').attrs['title']
    except:
        pass

    if search not in words_check:
        print(search)

    words_check.append(search)