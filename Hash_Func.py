# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 07:23:43 2023

@author: fr
"""

import hashlib
md5 = hashlib.md5()
type(md5)
print(md5)
md5.update(b'python')
print(md5.digest())
print(md5.hexdigest())

print("----------------MD5--------------------")

md5.update(b'Name')
print(md5.digest())
print(md5.hexdigest())


print("----------------SHA1------------------")

sha = hashlib.sha1(b"python").hexdigest()
print(sha)



print(hashlib.algorithms_available)
print("--------------------------------------")
print(hashlib.algorithms_guaranteed)

print("----------------SHA256------------------")

sha256 = hashlib.sha256(b"This a Text").hexdigest()
print(sha256)



print("----------------SHA512------------------")

sha512 = hashlib.sha512(b"This a Text").hexdigest()
print(sha512)



print("----------------SHA224------------------")

sha224 = hashlib.sha224(b"This a Text")

size_of_block = sha224.block_size
size_of_digest = sha224.digest_size

print("Block size :" , size_of_block)

print("Digest size :" , size_of_digest)




