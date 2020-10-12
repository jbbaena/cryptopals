#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:30:01 2019

@author: cryptopals: Srt 1, Challenge 4.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 19:41:56 2019

@author: cryptopals
"""

from set1_ch3 import dec_sin_char
from set1_ch3 import get_english_score
   
lines = [line.strip()  for line in open('strings.txt')]

#print(dec_sin_char(lines[2]))

max = 0;
decryption = '';
key ='';


for line in lines:
    temp_key, temp_plain_text = dec_sin_char(bytes.fromhex(line))
    score = get_english_score(temp_plain_text)
    if score > max:
        max = score
        decryption = temp_plain_text
        key = temp_key
        
print('The key is:', chr(key),'and the plain_text is: ',decryption.decode('ascii'))