#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:27:10 2019

@author: cryptopal challenge 7 set 1
"""

from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Util.Padding import unpad



key = b"YELLOW SUBMARINE"

cipher = AES.new(key, AES.MODE_ECB)

with open('input_ch7.txt','rb') as file:
    plaintext = b64decode(file.read())
    

print(unpad(cipher.decrypt(plaintext),AES.block_size).decode('utf-8'))
