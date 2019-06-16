#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:07:20 2019

@author: dan
"""
import sys


from bs4 import BeautifulSoup
from requests import get
from pymorphy2 import MorphAnalyzer
from random import randint

yr = BeautifulSoup(get('https://yandex.ru/referats/').content, 'lxml')
ma = MorphAnalyzer()

def _get_topics(soup):
    div = soup.find('div', {'class':"referats__options"})
    for item in div('div', {'class':"topics__item"}):
        key = item.span.label['for']
        val = ma.parse(item.span.label.text)[0].normal_form
        yield key, val

def _collect_texts(soup):
    import re
    for key, topic in _get_topics(soup):
        for i in range(2):
            try:
                url = 'https://yandex.ru/referats/?t=%s&s=%s' % (key, randint(1, 10000))
                text = BeautifulSoup(get(url).content, 'lxml').find('div', {'class':"referats__text"})
                assert text is not None
                title = re.findall('Тема: «(.*)»', text.strong.text)[0]
                text = ' '.join([ p.text for p in text('p') ])
                yield url, key, topic, title, text
            except (IndexError, AssertionError, AttributeError) as e:
                print(e, url, file = sys.stderr)
            except ConnectionError as e:
                print(e, url, file = sys.stderr)
        
def train():
    print(list(_collect_texts(yr)))
        
if __name__ == '__main__':
    train()