#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:25:01 2019

@author: dan
"""
import sys

from generate import generate


if __name__ == '__main__':
    try:
        title = sys.argv[1]
        generate(title)
    except IndexError:
        print('usage')