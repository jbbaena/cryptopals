#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:05:56 2019

@author: crypto

HEX_XOR function takes two hex string inputs outputs his HOX in hex
int('0xstring', 16), convert the hex strinf 0xstring to integer 
it can also be used as int('string,16)
bin(inte) convert the integer inte to binary
"""
import codecs

def HEX_XOR(str1, str2):
    return str(hex(int(str1,16) ^ int(str2,16))[2:])
    

str1 = '1c0111001f010100061a024b53535009181c'
str2 = '686974207468652062756c6c277320657965'

#print(chr(a))
bstr1 = bytes.fromhex(str1)
bstr2 = bytes.fromhex(str2)

def byte_xor(s1,s2):    
    return bytes([a ^ b for a,b in zip(s1,s2)])

a = byte_xor(bstr1,bstr2)
b_a = codecs.encode(a,'hex')
print(b_a.decode())