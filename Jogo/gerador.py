import random

def gera_numeros():
    saida= []
    saida.append(random.randint(1,99)) #Seleciona 1° Num

    while len(saida)<3: #Adiciona mais 2 números diferentes
        proxNum = random.randint(1,99)
        if proxNum not in saida:
            saida.append(proxNum)
    errado = random.randint(0,2)
    soma=0
    for n in saida: 
        if n != saida[errado]:
            soma += n
    saida.append(soma)

    return (saida,errado) #Retorna a lista de numeros e a posição do errado
