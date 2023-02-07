def duplicate_count(text):
    # Your code goes here
    lista = [y.lower()for x,y in enumerate(text) if y!=text[x+1]]
    return len(lista)

#ARREGLAR