'''
Cuente el número de duplicados
Escriba una función que devuelva el recuento de caracteres alfabéticos y dígitos numéricos distintos que no distinguen entre mayúsculas y minúsculas que aparecen más de una vez en la cadena de entrada. Se puede suponer que la cadena de entrada contiene solo letras (tanto mayúsculas como minúsculas) y dígitos numéricos.

Ejemplo
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibilidad" -> 1 # 'i' occurs six times
"Indivisibilidades" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''

def duplicate_count(text):
    # Your code goes here

    text = text.lower()
    contador = 0
    alfabeto = {}
    for l in text:
        if l in alfabeto:
            alfabeto[l] += 1
        else:
            alfabeto[l] = 1
            
    for i in alfabeto:
        if alfabeto[i] > 1:
            contador+=1
    
    return contador