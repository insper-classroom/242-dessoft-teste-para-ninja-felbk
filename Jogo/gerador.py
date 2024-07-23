import random

def gera_numeros():
    saida= []
    #Seleciona 1° Num
    saida.append(random.randint(1,99)) 

    #Adiciona mais 2 números diferentes
    while len(saida)<3: 
        proxNum = random.randint(1,99)
        if proxNum not in saida:
            saida.append(proxNum)
    #Escolhe a posição da lista para ser o errado
    erradoPos = random.randint(0,2) 

    # Faz a soma com os outros dois números
    soma=0
    for n in saida:  
        if n != saida[erradoPos]:
            soma += n
    saida.append(soma)

    #Retorna a lista de numeros e a posição do errado
    return (saida,erradoPos) 


