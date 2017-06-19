# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:41:59 2017

@author: Анастасия
"""

s = 'azcbobobegghakl'

alpha = 'abcdefghijklmnopqrstuvwxyz'

step = 0
current = 0
temp = ''
result = ''

while step != len(s):
    if alpha.find(s[step]) >= current:
        temp += s[step]
        current = alpha.find(s[step])
    else:
        temp = s[step]
        current = alpha.find(s[step])
    step += 1
    if len(temp) > len(result):
        result = temp

message = 'Longest substring in alphabetical order is: %s' % (result)
print(message)