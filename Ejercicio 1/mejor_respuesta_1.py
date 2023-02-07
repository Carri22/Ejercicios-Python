#Encuentre el valor atípico de paridad
'''
Se le proporciona una matriz 
(que tendrá una longitud de al menos 3, pero podría ser muy grande)
que contiene números enteros. La matriz está completamente compuesta por enteros impares o completamente compuesta por enteros pares excepto por un solo entero N. 
Escriba un método que tome la matriz como argumento y devuelva este "valor atípico" N.

Ejemplos:

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)'''
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]