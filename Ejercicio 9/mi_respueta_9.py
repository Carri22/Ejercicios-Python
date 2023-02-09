def array_diff(a, b):
    
    #your code here
    lista = [x for x in a if not x in b ]
    return lista

print(array_diff([1,2,3],[2]))