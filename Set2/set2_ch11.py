#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:18:17 2019

@author: Javier Verbel 
Crypotals set2_ch11
"""

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import randint
 
#from set2_ch10 import enc_cbc_mode

def encrypt_oracle(text):
    def ran_append(tex):
        l = randint(5,10)
        return get_random_bytes(l) + tex + get_random_bytes(l)
    pad_text = pad(ran_append(text),AES.block_size, style='pkcs7')    
    a = ord(get_random_bytes(1))%2
    if a == 0:
        cipher = AES.new(get_random_bytes(AES.block_size), AES.MODE_ECB)
        used = "ebc"
    else: 
        cipher = AES.new(get_random_bytes(AES.block_size), AES.MODE_CBC)
        used = "cbc"
    return cipher.encrypt(pad_text), used

def chunks(text,blocksize):
    num_chunks = len(text) // blocksize
    chu = [] 
    for i in range(num_chunks):
        chu.append(text[i*blocksize: (i+1)*blocksize])
    return chu

def repetitions(chunk):
    return len(chunk) - len(set(chunk))

def mode_detector(ciphertext):
    c_blocks = chunks(ciphertext,AES.block_size)
    a = repetitions(c_blocks)
    if a == 0:
        return "Encrypted using CBC mode"
    else:
        return "Encrypted using EBC mode"

with open('input_ch8.txt','rb') as file:
    plaintext = file.read()

print(plaintext)

ciphertext, mode = encrypt_oracle(plaintext)
print(mode)
print(mode_detector(ciphertext))
 


    



#perdictors = {ebc:}

