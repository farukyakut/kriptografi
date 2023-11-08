# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 06:00:07 2023

@author: fr
"""

from Crypto.Cipher import DES

key = '12345678'

def pad(text):
    while len(text) % 8 !=0:
        text += " "

    return text     

text1 = 'this is a encrption application'

des = DES.new(key.encode("utf8"),DES.MODE_ECB)

padded_text = pad(text1)

#şifreleme
enctypition_text = des.encrypt(padded_text.encode("utf8"))

print(enctypition_text) 
print(enctypition_text.hex())   
 
#şifre Çözme
print(des.decrypt(enctypition_text))