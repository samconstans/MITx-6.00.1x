# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:39:49 2017

@author: Анастасия
"""

s = 'azcbobobegghaklbob'

count = 0
countBob = 0

for letter in s:
    count += 1
    if (count+1) < len(s) and letter == 'b' and s[count] == 'o' and s[count+1] == 'b':
        countBob += 1
print('Number of times bob occurs is: ' + str(countBob))