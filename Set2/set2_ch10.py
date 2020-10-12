#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 13:46:27 2019

@author: crypto Javier Verbel 
Cryptopals Set 2 Challenge 10
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import codecs

def byte_xor(s1,s2):    
    return bytes([a ^ b for a,b in zip(s1,s2)])

def chunks(text,blocksize):
    """ divide the string text in chunks of size blocksize, it outputs list"""
    num_chunks = len(text) // blocksize
    chu = [] 
    for i in range(num_chunks):
        chu.append(text[i*blocksize: (i+1)*blocksize])
    return chu

def enc_cbc_mode(cipher, plaintext, IV):
    """here we asusme len(IV) == cipher.block_size and plaintext is unpadded"""
    pad_plaintext = pad(plaintext,len(IV),style = 'pkcs7')
    xor_text = IV
    plain_blocks = chunks(pad_plaintext, len(IV))
    cipher_blocks = []
    for block in plain_blocks:
        c_block = cipher.encrypt(byte_xor(xor_text,block))
        xor_text = c_block
        cipher_blocks.append(c_block)
    
    return unpad(b''.join(cipher_blocks))

def dec_cbc_mode(cipher, ciphertext, IV):
    xor_text = IV
    plain_blocks = []
    cipher_blocks = chunks(ciphertext, len(IV))
    for block in cipher_blocks:
        plain_blocks.append(byte_xor(xor_text,cipher.decrypt(block)))
        xor_text = block
    #return unpad(b''.join(plain_blocks),len(IV),style='pkcs7')
    return unpad(b''.join(plain_blocks),len(IV), style='pkcs7')

key = b"YELLOW SUBMARINE"

cipher = AES.new(key, AES.MODE_ECB)

   
#assert dec_cbc_mode(cipher,enc_cbc_mode(cipher,plaintext, IV), IV) == plaintext

with open('input_set2_ch10.txt','rb') as file:
    enc_cipher = file.read()

ciphertext = codecs.decode(enc_cipher,'base64')


#from binascii import unhexlify, b2a_base64, a2b_base64
#ciphertext = b''.join([a2b_base64(line.strip()) for line in open("input_set2_ch10.txt").readlines()])

iv = bytes(chr(0)*AES.block_size,'ascii')
#key = b"YELLOW SUBMARINE"
a = dec_cbc_mode(cipher, ciphertext,iv)
print(a)