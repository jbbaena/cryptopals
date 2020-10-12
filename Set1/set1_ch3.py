#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 19:41:56 2019

@author: crypto
"""

import string 


CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


def get_english_score(byte_string):
    """Given an string od bytes, it returns a score which is the sum of the probabilities in how each letter of the input string
    appears in the English language. Uses the above probabilities.
    """
    score = 0

    for byte in byte_string:
        score += CHARACTER_FREQ.get(chr(byte).lower(), 0)

    return score

def xor_single_char(byte_string, single_byte):
    """both inputs are in bytes"""
    output = b''
    for char in byte_string:
        output += bytes([char ^ single_byte])
        
    return output
    
def dec_sin_char(byte_string):
    '''the input shpuld be a bytes string'''
    ''' It tries all possible keys and out put the decryption with hights score and its corresponging Key'''
    max = 0;
    decryption = '';
    key ='';

    for i in range(256):
        #print(i)
        result = xor_single_char(byte_string,i)
        score = get_english_score(result) 
       # print(score)
        if score > max:
            max = score
            decryption = result
            key = i
            
    return key, decryption
#print(bytes.fromhex(decryption).decode('ascii'))   

#input_string ='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#cipher_text = bytes.fromhex(input_string);
#key, plain_text = dec_sin_char(cipher_text)

#print('Key:', chr(key), ',', 'Plain_Text: ', plain_text.decode('utf-8'))

