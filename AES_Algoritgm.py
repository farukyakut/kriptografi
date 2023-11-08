# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:33:16 2023

@author: fr
"""


from Crypto.Cipher import AES



#anahtar uzunluğu 16 bittir. Anahtar 16,24, 32 bit olabilir.
obj = AES.new('This is a key123'.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8"))
#mesaj uzunluğu 16 bittir
message = "The answer is no".encode("utf8")
#şifreleme
ciphertext = obj.encrypt(message)
ciphertext

print(ciphertext)

obj2 = AES.new('This is a key123'.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8")) 
#şifre 
plainttext = obj2.decrypt(ciphertext)
print(plainttext)
