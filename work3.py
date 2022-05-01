# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:31:55 2022

@author: Etay
"""
#C:/Users/Etay/Desktop/ex3_text.txt


######################### A #########################

#input index for number of line and file address output the line
def read_line(n, file):
    
    #if n not int
    if type(n) != int:
        return 'invalid input detected'
    
    #if fill not found
    try:
        file = open(str(file))
    except: 'file not found'
    
    #find the line
    i = 1
    for line in file:
        if n == i:
            return line
        i = i+1
    return 'line ' + str(n) + ' doesnt exist'
######################### B #########################

#takes a string representing a file name as an input and returns a list of the first 5 longest words of the txt file
def longest_words(file):
    
    #if fill not found
    try:
        file = open(str(file))
    except: 'file not found'
    
    #make list of a words and there len (key = word value = long of word)
    d_word = {}
    f_word = []
    f_5_word = []
    for line in file:
        line = line.strip()
        line = line.replace('.', ' ').replace('-', ' ').split()
        for word in line:       
            d_word[word] = d_word.get(word, len(word)) 
    
    #Sort by values
    f_word = ( sorted([(v,k) for k,v in d_word.items()], reverse=True))
    
    #for i in range(5):
    #    f_5_word.append(f_word[i][1])
    #return f_5_word
    
    i = 0
    for k,v in f_word:
        f_5_word.append(v)
        if i == 4:
            break
        i=i+1
    return f_5_word
    
