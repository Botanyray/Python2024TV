# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:57:10 2024

@author: lpers
"""
### I numeri primi saranno in lista
lista=[]

for k in range(1,101):
    lista.append(k)



n=1
while True:
    
    a=lista[n]
    n=n+1
    if a**2> 101:
        break
    
#creo una nuova lista di appoggio che è la lista prima del setaccio dell'iterazione corrente    
    lista2=lista.copy()
    
    for k in lista2:
        
        
        
        if (k%a==0) and (k!=a):
            lista.remove(k)
            
lista.remove(1)