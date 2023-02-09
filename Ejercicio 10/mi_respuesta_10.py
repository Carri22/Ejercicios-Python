def narcissistic( value ):
    # Code away
    lista = [int(x) for x in str(value)]
    mapped_numbers = list(map(lambda x: x**len(lista), lista))
    suma = 0
    for num in mapped_numbers:
        suma+=num
    print(suma)
    return True if suma == value else False
    

print(narcissistic(326))