

def quicksort(elementos):
    if len(elementos) <=1:
        return elementos

    primer_elemento = elementos[0]
    menores = list(filter(lambda x : x < primer_elemento,elementos ))
    mayores = list(filter(lambda x : x > primer_elemento,elementos))

    return quicksort(menores)+[primer_elemento]+quicksort(mayores)

lista =[5,1,9,8,4,6,7,3]
print(quicksort(lista))