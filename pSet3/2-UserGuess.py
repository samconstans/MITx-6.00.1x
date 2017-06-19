# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:53:32 2017

@author: Анастасия
"""

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    wordsFilled = ''
    for i in secretWord:
        if i in lettersGuessed:
            wordsFilled += i
        else:
            wordsFilled += '_'
    return wordsFilled
    
print(getGuessedWord(secretWord, lettersGuessed))