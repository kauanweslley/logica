
import random
def remover_caracter(antigo, remover):
    novo = antigo
    for x in remover:
        novo = novo.replace(x, '')
    return novo


def validation_cpf(cepefe):

    cepefe = remover_caracter(cepefe, '.-')
 
    lista = []
    for n in cepefe:
        lista.append(int(n))


    repeticao = soma = 0
    for n in range(len(lista)):                   
        if lista[0] == lista[n]:
            repeticao += 1
    if repeticao >= 11:

        return False
    else:

        limite = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        for n in range(0, 9):
            soma += lista[n] * limite[n]
        resto_um = soma * 10 % 11
        if resto_um == 10:
            resto_um = 0
        soma = 0

        limite_dois = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        for n in range(0, 10):
            soma += lista[n] * limite_dois[n]
        resto_dois = soma * 10 % 11
        if resto_dois == 10:
            resto_dois = 0
        if resto_um == lista[9] and resto_dois == lista[10]:
            return True
        else:
            return False
            


