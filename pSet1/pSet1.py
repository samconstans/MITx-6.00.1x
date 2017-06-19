# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:40:40 2017

@author: Анастасия
"""

s = 'azcbobobegghakl'

vowels = 'auioe'
count = 0

for letter in s: 
    if letter in vowels:
        count += 1
print('Number of vowels:' + ' ' + str(count))