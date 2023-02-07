'''
Escribe una función, persistence, que tome un parámetro positivo numy devuelva su persistencia multiplicativa,
 que es el número de veces que debes multiplicar los dígitos numhasta llegar a un solo dígito.

Por ejemplo (Entrada --> Salida) :

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
'''
def persistence(n):
    
    # your code
    lista = [int(x) for x in str(n)]
    num = 1
    cont = 0
    while(True):
        if n <10:
            return 0
        else:
            for i in lista:
                num *= i
            cont += 1
            if num <10:
                return cont
            else:
                lista = [int(x) for x in str(num)]
                num = 1
#ARREGLAR
print(persistence(39))