
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 23:07:56 2019

@author: crypto
"""

from Crypto.Util.Padding import pad

block_size = 20

a = b"YELLOW SUBMARINE";

print(pad(a, block_size,style='pkcs7')) #style can be 'iso 7816' and 'x923'
