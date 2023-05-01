import usefull
from direto import mapeamento_direto
import time
import math

def inicializar_cache(tamanho_cache,blocos,palavras=2):
    cache = {}
    for i in range(tamanho_cache):
        bloco = []
        for j in range(blocos):
            palavra = []
            for k in range(palavras):
                palavra.append(-1)
            bloco.append(palavra)
        cache[i] = bloco
    return cache

def imprimir_cache(cache):
    print("-" * 32)
    print("Posição Cache" + "|" + "Posições na memória")
    print("-" * 32)
    for i in range(len(cache)):
        for j in range(len(cache[i])):
            for k in range(len(cache[i][j])):
                if (j != 0 or k != 0):
                    print(f"              |      {cache[i][j][k]}       ")
                else:
                    print(f"      {i}       |      {cache[i][j][k]}       ")
            print("-" * 32)

def mapeamento_associativoconjunto(tamanho_cache, blocos, palavras, pos_memoria, hit=0, miss=0):
    washit = False
    if (blocos == 1):
        mapeamento_direto(tamanho_cache,pos_memoria)
        return
    cache = inicializar_cache(tamanho_cache,blocos,palavras)
    print(f"Tamanho da cache {tamanho_cache}") 
    imprimir_cache(cache)
    time.sleep(10)
    for i in range (len(pos_memoria)): # LIFO
        print(f"Linha {i} | Posição da memória requisitada: {pos_memoria[i]}")
        x = math.floor((pos_memoria[i] / palavras) % tamanho_cache) #descobrindo o número do conjunto
        for j in range (len(cache[x])):
            if (pos_memoria[i] in cache[x][j]):
                print("Status: Hit")
                hit += 1;
                washit = True
                break
        if (washit == False):
            saved = False
            print("Status: Miss")
            miss += 1
            for j in range (len(cache[x])):
                if (-1 in cache[x][j]):
                    if ((pos_memoria[i] % 2) ==  0):
                        cache[x][j] = [pos_memoria[i],pos_memoria[i]+1]
                    else:
                        cache[x][j] = [pos_memoria[i]-1,pos_memoria[i]]
                    saved = True
                    break
            if (saved is False):
                if ((pos_memoria[i] % 2) ==  0):
                    cache[x][-1] = [pos_memoria[i],pos_memoria[i]+1]
                else:
                    cache[x][-1] = [pos_memoria[i]-1,pos_memoria[i]]
        washit = False
        imprimir_cache(cache)
        time.sleep(10) #Pausa de alguns segundos para que o usuário possa acompanhar o processo
    print(f"- Total de posições de memórias acessadas: {len(pos_memoria)}")
    print(f"- Total de Hits: {hit}")
    print(f"- Total de Misses: {miss}")
    print(f"- Total de acerto: {(hit/len(pos_memoria)) * 100}%")


tam, bloco, palavras, pos = usefull.menu_assocon()
mapeamento_associativoconjunto(tam, bloco, palavras, pos)
#print(math.floor((1 / 2) % 2))