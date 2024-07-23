import random

def gera_numeros():
    saida= []
    saida.append(random.randint(1,99))
    while len(saida)<3:
        proxNum = random.randint(1,99)
        if proxNum != saida[-1]:
            saida.append(proxNum)
    errado = random.randint(0,2)
    soma=0
    for n in saida: 
        if n != saida[errado]:
            soma += n
    saida.append(soma)

    return saida
print(gera_numeros())