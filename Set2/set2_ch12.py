#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 12:01:38 2019

@author: Javier Verbel
Cryptopals set2_ch12. 
"""

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import codecs

skey = get_random_bytes(AES.block_size)
toappend = b"Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"


def encrypt_oracle(text):
    new = text +  codecs.decode(toappend, 'base64')
    pad_text = pad(new,AES.block_size, style='pkcs7')  
    cipher = AES.new(skey, AES.MODE_ECB)
    return cipher.encrypt(pad_text)

def chunks(text,blocksize):
    num_chunks = len(text) // blocksize
    chu = [] 
    for i in range(num_chunks):
        chu.append(text[i*blocksize: (i+1)*blocksize])
    return chu

def repetitions(chunk):
    return len(chunk) - len(set(chunk))

def mode_detector(ciphertext,blocksize):
    c_blocks = chunks(ciphertext,blocksize)
    a = repetitions(c_blocks)
    if a == 0:
        return "Encrypted using CBC mode"
    else:
        return "Encrypted using EBC mode"
    
def get_blocksize():
    app = b""
    inlen = len(encrypt_oracle(app))
    culen = inlen
    while inlen == culen:
        app += b"A"
        culen = len(encrypt_oracle(app))

    return culen - inlen

""" Here we add the block b"A"*40 because we know for sure it has repeted blocks"""
print(mode_detector(encrypt_oracle(b"A"*40),get_blocksize()))


def recover(n):
    """Here n is the number of bytes you want to recover"""
    recovered = b""
    b_size = get_blocksize() 
    rep = (n//b_size)+1
    for j in range(n):
        app = b"A"*((rep*b_size -(len(recovered)+1))) + recovered
        first = encrypt_oracle(b"A"*(rep*b_size - (len(recovered)+1)))[(rep-1)*b_size:rep*b_size]
        i = 0
        while i< 256:
            if first == encrypt_oracle(app + bytes(chr(i),'utf-8'))[(rep-1)*b_size:rep*b_size]:
                recovered += bytes(chr(i), 'utf-8')
                i = 256
            i+=1
    return recovered

print(recover(138))
#print(len(recover()))
        