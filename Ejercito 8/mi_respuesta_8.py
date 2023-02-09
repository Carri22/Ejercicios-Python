
'''
Complete la solución para que la función rompa la tripa de camello, usando un espacio entre palabras.

Ejemplo
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''
    

import re

def solution(s):
    
    x = re.search("[A-Z]+", s)
    s = re.sub("[A-Z]+", " "+ x.group(), s)
    return s

print(solution("holaComoEstas"))