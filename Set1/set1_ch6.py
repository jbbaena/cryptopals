
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:19:53 2019

@author: cryptopasl set 1 challenge 6
"""
from set1_ch3 import dec_sin_char
from set1_ch3 import get_english_score
from set1_ch5 import encrypt_xor
from base64 import b64decode

def hw(a):
    """ a -- the input as an integer"""
    count = 0
    while a:
        # Source: http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan
        a &= a - 1
        count += 1

    return count

def d_ham(bytes_string1,bytes_string2):
    """ string1 and string2 -- the inputs as strings of the same length"""
    if not len(bytes_string1) == len(bytes_string2):
        raise TypeError("The strings must have the same length")
        
    count = 0
    for i in range(len(bytes_string1)):
        count += hw(bytes_string1[i]^bytes_string2[i])

    return count

test_1 = 'this is a test'
test_2 = 'wokka wokka!!!'

#print(d_ham(bytes(test_1,'utf-8'),bytes(test_2,'utf-8')))

def crack_repkey_xor(file_line):
    '''Crack an encrypted file of bytes file_line'''
    a = 5
    distances = {}
    l = len(file_line)
    for KEYSIZE in range(2,40):
        dist = 0
        for j in range(3):
            value1 = file_line[j*KEYSIZE:(j+1)*KEYSIZE]
            value2 = file_line[(j+1)*KEYSIZE:(j+2)*KEYSIZE]
            dist += d_ham(value1,value2)
            
            dist = dist/(3*KEYSIZE)
            distances[KEYSIZE] = dist
            likely_keysize = sorted(distances, key=distances.get)[:a]
    

    '''Trying the a first possible KEY size'''
    
    #print(likely_keysize)

    l = len(file_line)
    
    pos_keys = []
    key = ''
    plaintext =''
    maxscore = 0

    for pos_keysize in likely_keysize:
        
        ''' for each posible keysize, find the possible keyvalue'''
        sub_texts = []
        for i in range(pos_keysize):
            temp = []
            for j in range(0,l-pos_keysize,pos_keysize):
                temp += [file_line[j + i]]
            sub_texts += [temp]
        
        
        temp2 = b''
        
        for j in range(len(sub_texts)):
            temp2 += bytes(chr(dec_sin_char(sub_texts[j])[0]),'utf-8')
        
        pos_keys.append(temp2)
        '''decrypt using a posible key. To decrypt un Xor encrypte text, we need to encrypt again'''
    
        temp3 = encrypt_xor(file_line, temp2)
        temp4 = get_english_score(temp3)
        
        if maxscore < temp4:
            maxscore = temp4
            key = temp2
            plaintext = temp3

    return key,plaintext       



lines = [line  for line in open('input_ch6.txt')]

file = ''.join(lines)
byte_file = b64decode(file)
    
crack = crack_repkey_xor(byte_file)

print("The key is: ", crack[0].decode('utf-8'))
print("The plaintext is :", crack[1].decode('utf-8'))