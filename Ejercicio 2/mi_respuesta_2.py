'''Algunos números tienen propiedades divertidas. Por ejemplo:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Dado un entero positivo n escrito como abcd... (a, b, c, d... siendo dígitos) y un entero positivo p

queremos encontrar un entero positivo k, si existe, tal que la suma de las cifras de n elevadas a las sucesivas potencias de p sea igual a k * n.
En otras palabras:

¿Existe un número entero k como: (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

Si es el caso devolveremos k, si no devolveremos -1.

Nota : n y p siempre se darán como números enteros estrictamente positivos.'''

import math

def dig_pow(n, p):
    # your code
    lista=[int(x) for x in str(n)]
    elevado = 0
    for i in lista:
        elevado += i**p
        p+=1
    return elevado/n if elevado%n==0 else -1
