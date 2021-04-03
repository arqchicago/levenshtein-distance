# -*- coding: utf-8 -*-
"""
Created on Wed Apr 1 20:20:38 2021

@author: Ahmad
"""
import numpy as np

def levenshtein_distance(word, target, case=True):
    if case==False:
        word = word.lower()
        target = target.lower()

    n = len(word)
    m = len(target)
    
    if n==0:
        return m, np.zeros(shape=(0,0))
    
    if m==0:
        return n, np.zeros(shape=(0,0))
        
    matrix = np.zeros(shape=(n+1,m+1))
    matrix[0], matrix[:,0]  = range(0,m+1), range(0,n+1)
    
    s__, t__ = list(word), list(target)

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s__[i-1] == t__[j-1]:
                cost = 0
            else:
                cost = 1

            matrix[i,j] = min(matrix[i-1,j]+1, matrix[i,j-1]+1, matrix[i-1,j-1]+cost)

    return matrix[n,m], matrix
    

if __name__ == '__main__':
    
    word_1 = 'honda'
    word_2 = 'honda'
    l_distance, matrix = levenshtein_distance(word_1, word_2)
    print(f'word 1 = {word_1}  word 2 = {word_2} --> levenshtein_distance = {l_distance}')
    
    word_3 = 'hyundai'
    l_distance, matrix = levenshtein_distance(word_1, word_3)
    print(f'word 1 = {word_1}  word 3 = {word_3} --> levenshtein_distance = {l_distance}')
    
    word_4 = 'jeep'
    l_distance, matrix = levenshtein_distance(word_1, word_4)
    print(f'word 1 = {word_1}  word 4 = {word_4} --> levenshtein_distance = {l_distance}')