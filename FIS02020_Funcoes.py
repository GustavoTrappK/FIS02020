#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 16:30:41 2025

@author: gustavotk
"""

# Funções
# - funções retorman um único objeto
# - sintaxe;
#   def <nome_da_funcao> (arg1, arg2,...):
#       <corpo_da_funcao>

# Exemplo 1:
def sayHellow(): 
    '''diz Hello!!'''
    print("Hello!!") 
    
print()
r = sayHellow()
print(f'r = {r}')

# Exemplo 2:   
def quadrado(x):
    '''retorna o quadrado de x'''
    return x**2

x2 = 5
y2 = quadrado(x2)

print()
print(f'O quadrado de {x2} é {y2}')

# Exemplo 3:
    
def soma(A,B,C):
    '''retorna a soma de a, b, c'''
    s = A + B + C
    return s
a = 10
b = 15
c = 17
y3 = soma(a,b,c)
print()
print(f'{a} + {b} + {c} = {y3}')

#%% Argumentos com palavras chave 
#                  (key worlds)
def p(a, b, c):
    '''retorna a + b**2 + c***3'''
    return a + b**2 + c**3

print()

y1 = p(10, 20, 30)
print(y1)

y2 = p(30, 10, 20)
print(y2)

y3 = p(c=30, a=10, b=20)
print(y3)

#%% Argumentos posicionais +
#   argumentos com palavras-chave

print()

print( p(30, 10, c=20) )

# print( p(a=30, 10, 10) ) #ERRO
# print( p(30, b=10, 30) )

#%% Parametros com alores
#   padroes (default)

def potencia(x, n=2):
    '''retorna x**n'''
    return x**n

print()

print( potencia(2, 3) )
print( potencia(2) )

#%% Froçando o uso de palavras-chave

def q(a, *, b, c):
    '''retorna a + b**2 + c**3'''
    return a+ b**2 + c**3

print()    
# print( q(10,20,30) ) #ERRO
print ( q(10, b=20, c=30) )
print( q(10, c=30, b=20) )
print( q(a=10, c=30, b=20) )

#%%

def q(a, *, b=0, c=0):
    '''retorna a + b**2 + c**3'''
    return a+ b**2 + c**3

print( q(10) )

#%% Passando uma lista como argumento 

# Exemplo 1

def listar(lista):
    '''lista os elementos de uma lista'''
    
    for elemento in lista:
        print(elemento)

lista1 = {'alfa', 'beta', 'gama'}

listar(lista1)

#%% 

# Exemplo 2 

def p(a, b, c):
    '''retorna a + b**2 + c***3'''
    return a + b**2 + c**3

lista = {10,  20, 30}

print()
print(lista)

print()
print(*lista)


print()
#print( p(lista) ) #ERRO, ELE ENTENDE COMO 1 PARAMETRO APENAS

print( p(*lista) )

#%% Passando um dicionario como argumento de uma funçao

def p(a, b, c):
    '''retorna a + b**2 + c***3'''
    return a + b**2 + c**3

args = dict(a=10, b=20, c=30)

#args = {'a':10, 'b':20, 'c':30}

print()
print(args)

print()
print(*args)

print()
print( p(**args) )

#%% Passando um numero arbitrario de argumentos para uma funcao

def media3 (a, b, c):
    '''retorna a media de a, b, c'''
    return (a + b + c)/3

def media (*valores):
    '''retorna a media de n valores'''
   # soma = 0
   # for n in valores:
   #     soma += n
   
    soma = sum(valores) 
    
    z = len(valores)
    
    med = soma/z
    
    return med


print()
print( media3(10, 11, 12) )

print()
print( media(10, 20, 30, 40) )

#%% Vaiaveis locais e globais

v = 123
g = 456
t = 888

def foo():
    global g
    v = 500
    g = 111
    print(f'foo() = {v} {g} {t}')
    
print(f"Valor de v,g ANTES: {v} {g} {t}")
foo()
print(f"Valor de v DEPOIS: {v} {g} {t}")


