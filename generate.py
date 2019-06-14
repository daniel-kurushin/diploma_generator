#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:40:14 2019

@author: dan
"""

from rutermextract import TermExtractor

te = TermExtractor()

def generate(title):
    
    print([ _.normalized for _ in te(title)])