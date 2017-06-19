# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:49:53 2017

@author: Анастасия
"""

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    if (len(secretWord) > 0):
        return secretWord[0] in lettersGuessed and isWordGuessed(secretWord[1:], lettersGuessed)
    else:
        return True
        
print(isWordGuessed(secretWord, lettersGuessed))