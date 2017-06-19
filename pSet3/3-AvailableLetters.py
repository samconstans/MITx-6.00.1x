# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:55:34 2017

@author: Анастасия
"""

import string
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def getAvailableLetters(lettersGuessed):
    strAvailable = ''
    strList = []
    for i in string.ascii_lowercase:
        strList.append(i)
    for letter in lettersGuessed:
        if letter in strList:
            strList.remove(letter)
    strAvailable =strAvailable.join(strList)
    return strAvailable

    
print(getAvailableLetters(lettersGuessed))
print(string.ascii_lowercase)