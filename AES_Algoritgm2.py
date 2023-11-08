# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 12:59:30 2023

@author: fr
"""

#16 bit data için mode cbc olmalı

from Crypto.Cipher import AES

#anahtar uzunluğu 16 bittir. Anahtar 16,24, 32 bit olabilir
def paddedKey(key):
    while len(key) % 8 != 0:
        key += " "

    return key

#mesaj uzunluğu 16 bittir
def paddedText(text):
    while len(text) % 16 != 0:
        text += " "

    return text



text = input("Mesajınızı giriniz")
planinText = paddedText(text)


key = input("16-32 karakter arası bir anahtar giriniz")
key = paddedKey(key)

obj = AES.new(key.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8"))

planinText = planinText.encode("utf8")
#şifreleme
ciphertext = obj.encrypt(planinText)
ciphertext

print(ciphertext)

obj2 = AES.new(key.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8")) 
#şifre 
plainttext = obj2.decrypt(ciphertext)
print(plainttext)