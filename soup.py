# Python program to crawl a web page and get most frequent words

"""
The task is to count the most frequent words, which extracts data from dynamic sources.
First, create a web-crawler or scraper with the help of requests module and beautiful soup module, 
which will extract data from the web-pages and store them in a list. There might be some undesired words or symbols 
(like special symbols, blank spaces), which can be filtered in order to ease the counts and get the desired results. 

After counting each word, we also can have the count of most (say 10 or 20) frequent words.
"""

from collections import Counter
import requests
from bs4 import BeautifulSoup
import re

l = []
url = 'https://en.wikipedia.org/wiki/Airplane'
r = requests.get(url)

soup = BeautifulSoup(r.text)

for i in soup.find_all('p'):
    i = i.text
    words = i.lower().split()

    for j in words:
        l.append(j)

    clean_list = []
    for word in l:
        symbols = "!@#$%^&*()_-+={[}]|;:\"<>?/., "
 
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)


print(Counter(clean_list))