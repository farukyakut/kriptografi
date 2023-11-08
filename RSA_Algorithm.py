# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 10:36:23 2023

@author: fr
"""

import random
import math

# sayinin asal olup olmadığı kontrol edilir.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0: 
            return False    
    return True

# iki değer arasında asal sayı üretme
def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime    
    
# d (gizli anahtar) üretilir.
def mod_inverse(e,phi):
    for d in range(3,phi):
        if e*d % phi == 1:
            return d            
    raise ValueError("Mod_inverst fonksiyonu çıktı vermedi. (d^-1) bulunamadı")    

    
p , q = generate_prime(1000, 5000),generate_prime(1000, 5000)

while p == q:
    q = generate_prime(1000, 5000)
    

n = p * q

phi_n = (p - 1) * (q - 1)

#e ve phi_n aralarında asal olmalıdır.
e = random.randint(3, phi_n - 1)
# e anahtarı ile phi aralarında asal olmalıdır. Bu yüzden ebobları = 1 olmalı.
while math.gcd(e, phi_n - 1) != 1:
    e = random.randint(3, phi_n - 1)
    
  
d = mod_inverse(e, phi_n)

print("Public Key: ", e)
print("Private Key: ", d)
print("n: ", n)
print("Phi of n: ", phi_n)
print("p: ", p)
print("q: ", q)

message = "Hellomysecretfriend"

#for dingüsünün oluşturulmasının sebebi mesaj karakterlere bölünmektedir.Ardından harfler encode edilir.
message_encoded = [ord(ch) for ch in message]
print("message_encoded: ",message_encoded)

#Şifreleme
# (m^e) mod n = c
ciphertext = [pow(ch,e,n) for ch in message_encoded]
print("ciphertext: ",ciphertext) 

print("--------------------------------------------")
print("--------------------------------------------")

#Şifre Çözme
#(c^d) mod n = m
plaintext_encoded = [pow(ch,d,n) for ch in ciphertext]
print("plaintext_encoded: ",plaintext_encoded)
plainText = "".join(chr(ch) for ch in plaintext_encoded)
print("plainText: ", plainText) 


    

