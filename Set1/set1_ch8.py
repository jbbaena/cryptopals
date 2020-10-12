#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 13:21:20 2019

@author: cryptopal challenge 7 set 1
"""

with open('input_ch8.txt','r') as file:
     ct = file.readlines()
     


def chunks(text,blocksize):
    num_chunks = len(text) // blocksize
    chu = [] 
    for i in range(num_chunks):
        chu.append(text[i*blocksize: (i+1)*blocksize])
    return chu

def repetitions(chunk):
    return len(chunk) - len(set(chunk))

myDict = {} 
blocksize = 16

for text in ct:
    myDict[text] = repetitions(chunks(text.strip(),blocksize))
    
values = list(myDict.values())

values.sort(reverse = True)

for text, rep in myDict.items():
    if rep ==values[0]:
        text_ebc = text
        print(text)
        
for i in range(len(ct)):
    if repetitions(chunks(ct[i].strip(),blocksize)) == values[0]:
        print(i)