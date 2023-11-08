# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 10:56:55 2023

@author: fr
"""

import hashlib, binascii

hash = hashlib.pbkdf2_hmac('sha512', b'SuperSecretPassword', b'saltthepassword', 100000)

print(hash)

print("----------------------------------------")

hash = binascii.hexlify(hash)

print(hash.hex())

print("----------------------------------------")

print(hash)
