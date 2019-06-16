#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:05:48 2019

@author: dan
"""
from json import dumps

class JsonSet(set):
    def __repr__(self):
        return dumps(list(self))
    
if __name__ == '__main__':
    x = set([ _ for _ in range(10) if _ % 2 == 0 ])
    y = set([ _ for _ in range(10) if _ % 2 != 0 ])
    print(JsonSet(x) | y)