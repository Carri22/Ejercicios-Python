'''
El objetivo de este ejercicio es convertir una cadena en una nueva cadena donde cada carácter de la nueva cadena es "("si ese carácter aparece solo una vez en la cadena original, o ")"si ese carácter aparece más de una vez en la cadena original. Ignore las mayúsculas al determinar si un carácter es un duplicado.

Ejemplos
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
'''
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])