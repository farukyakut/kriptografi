# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 08:28:49 2023

@author: fr
"""

import math




#Euler totien fonksiyonu kendinden küçük ve kendiyle aralarında asal olan rakamların sayisini verir. eğer verilen rakam asal sayi ise
#totien fonksiyonu kendinin bir eksiğidir
def EulerTotientFunc(sayi):
    
    rakam = 0
    for i in range(sayi):
        #aralarında asal olan sayiların ebobu 1 olur
        ebob=math.gcd(sayi,i)
        if(ebob == 1):
            rakam += 1
    return rakam  

EulerTotientFunc(7) 
         