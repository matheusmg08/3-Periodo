def quickSort(lista):
    quickSortOrdena(lista, 0, len(lista)-1)

def quickSortOrdena(lista, esq, dir):
    if esq < dir:
        indice = particao(lista, esq, dir)
        quickSortOrdena(lista, esq, indice-1)
        quickSortOrdena(lista, indice+1, dir)


def particao(lista, esq, dir):
    pivo = lista[esq]
    # particionamento
    i = esq
    j = dir
    while i <= j:
        # encontrar elemento maior do que o pivô
        while i <= dir and lista[i] <= pivo:
            i += 1
        while j >= esq and lista[j] > pivo:
            j -= 1
            #se indices se cruzarem
        if i >= j:
            break

        lista[j], lista[i] = lista[j], lista[i]
    lista[esq], lista[j] = lista[j], lista[esq]

    #retorna o índice que o pivô está
    return j

lista = [7, 2, 4, 3, 7, 6, 1]
quickSort(lista)
print(lista)

