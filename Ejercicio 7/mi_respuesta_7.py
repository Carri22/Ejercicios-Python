'''
Te van a dar una palabra. Su trabajo es devolver el carácter medio de la palabra. Si la longitud de la palabra es impar, devuelve el carácter del medio. Si la longitud de la palabra es par, devuelve los 2 caracteres del medio.

#Ejemplos:

Kata.getMiddle("prueba") debería devolver "es"

Kata.getMiddle("testing") debería devolver "t"

Kata.getMiddle("medio") debería devolver "dd"

Kata.getMiddle("A") debería devolver "A"
#Aporte

Una palabra (cadena) de longitud 0 < str < 1000 (en javascript puede obtener un poco más de 1000 en algunos casos de prueba debido a un error en los casos de prueba). No necesita probar para esto. Esto solo está aquí para decirle que no necesita preocuparse por el tiempo de espera de su solución.

#Producción

Los caracteres del medio de la palabra representada como una cadena.
'''

def get_middle(s):
    return s[(len(s)//2)-1:(len(s)//2)+1] if len(s)%2==0 else s[(len(s)//2):(len(s)//2)+1]