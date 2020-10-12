#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:39:40 2019

@author: cryptopals Set 1 Challenge 5
"""


from binascii import hexlify   

    
def encrypt_xor(plain_text_bytes,private_key_bytes):
    ''' Encrypt the byte string plain_text_bytes by doing reapeated XOR with the key private_key_bytes'''
    len_plain = len(plain_text_bytes);
    len_key = len(private_key_bytes);
    temp2 =  len_plain % len_key
    temp1 = len_plain// len_key
    cipher_text_bytes = b'';
    for i in range(temp1):
        for j in range(len_key):
            cipher_text_bytes += bytes([plain_text_bytes[i*len_key + j] ^ private_key_bytes[j]]);
    
    for k in range(temp2):
        cipher_text_bytes += bytes([plain_text_bytes[temp1*len_key + k] ^ private_key_bytes[k]]);
    
    return cipher_text_bytes

plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal";
privatekey = 'ICE';

hex_ciphertext = hexlify(encrypt_xor(plaintext.encode('utf-8'),privatekey.encode('utf-8'))).decode('utf-8')
print(hex_ciphertext)

#'''Verifying the answer'''
#assert (hex_ciphertext == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")




