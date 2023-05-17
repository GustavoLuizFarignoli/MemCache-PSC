from usefull import menu_assocon
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

def mapeamento_associativoconjunto(tamanho_cache, blocos, palavras, pos_memoria):
    if (blocos == 1):
        mapeamento_direto(tamanho_cache,pos_memoria)
        return
    cache = inicializar_cache(tamanho_cache,blocos,palavras)
    print(f"Tamanho da cache {tamanho_cache}") 
    imprimir_cache(cache)
    print("Escolha a técnina de substituição:" + "\n-Lifo\n-Fifo\n-LRU\n-LFU")
    tec = input("->")
    print(tec.lower())
    if(tec.lower() == "lifo"):
        hit, miss = lifo(tamanho_cache, palavras, pos_memoria, cache)
    elif(tec.lower() == "fifo"):
        hit, miss = fifo(tamanho_cache, palavras, pos_memoria, cache)
    elif(tec.lower() == "lru"):
        hit, miss = lru(tamanho_cache, palavras, pos_memoria, cache)
    elif(tec.lower() == "lfu"):
        hit, miss = lfu(tamanho_cache, blocos, palavras, pos_memoria, cache)
    print(f"- Total de posições de memórias acessadas: {len(pos_memoria)}")
    print(f"- Total de Hits: {hit}")
    print(f"- Total de Misses: {miss}")
    print(f"- Total de acerto: {math.floor((hit/len(pos_memoria)) * 100)}%")


def lifo(tamanho_cache, palavras, pos_memoria, cache, hit=0, miss=0):
    washit = False
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
    return hit, miss

def fifo(tamanho_cache, palavras, pos_memoria, cache, hit=0, miss=0):
    washit = False
    for i in range (len(pos_memoria)): # LIFO
        print(f"Linha {i} | Posição da memória requisitada: {pos_memoria[i]}")
        x = math.floor((pos_memoria[i] / palavras) % tamanho_cache) #descobrindo o número do conjunto
        for j in range (len(cache[x])):
            if (pos_memoria[i] in cache[x][j]):
                print("Status: Hit")
                hit += 1
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
                cache[x].pop(0)
                if ((pos_memoria[i] % 2) ==  0):
                    cache[x].append([pos_memoria[i],pos_memoria[i]+1])
                else:
                    cache[x].append([pos_memoria[i]-1,pos_memoria[i]])             
        washit = False
        imprimir_cache(cache)
        time.sleep(10) #Pausa de alguns segundos para que o usuário possa acompanhar o processo
    return hit, miss

def lru(tamanho_cache, palavras, pos_memoria, cache, hit=0, miss=0):
    washit = False
    mru = []
    for i in range (len(pos_memoria)): # LIFO
        print(f"Linha {i} | Posição da memória requisitada: {pos_memoria[i]}")
        x = math.floor((pos_memoria[i] / palavras) % tamanho_cache) #descobrindo o número do conjunto
        for j in range (len(cache[x])):
            if (pos_memoria[i] in cache[x][j]):
                print("Status: Hit")
                hit += 1
                washit = True
                mru = cache[x][j]
                cache[x].remove(mru)
                cache[x].append(mru)
                break
        if (washit == False):
            print("Status: Miss")
            miss += 1
            cache[x].pop(0)
            if ((pos_memoria[i] % 2) ==  0):
                cache[x].append([pos_memoria[i],pos_memoria[i]+1])
            else:
                cache[x].append([pos_memoria[i]-1,pos_memoria[i]])             
        washit = False
        imprimir_cache(cache)
        time.sleep(10) #Pausa de alguns segundos para que o usuário possa acompanhar o processo
    return hit, miss

def lfu(tamanho_cache, blocos, palavras, pos_memoria, cache, hit=0, miss=0):
    lfu = {}
    washit = False
    for i in range(tamanho_cache):
        lfubloco = []
        for j in range(blocos):
            lfubloco.append(0)
        lfu[i] = lfubloco;
    for i in range (len(pos_memoria)):
        print(f"Linha {i} | Posição da memória requisitada: {pos_memoria[i]}")
        x = math.floor((pos_memoria[i] / palavras) % tamanho_cache) #descobrindo o número do conjunto
        for j in range (len(cache[x])):
            if (pos_memoria[i] in cache[x][j]):
                print("Status: Hit")
                hit += 1
                washit = True
                lfu[x][j] += 1;
                break
        if (washit == False):
            print("Status: Miss")
            miss += 1
            lowestfrequency = 100000
            leastused = 0
            for l in range (len(lfu[x])): # percorrer o lfu e ver qual bloco foi menos usado
                if (lfu[x][l] < lowestfrequency):
                    lowestfrequency = lfu[x][l]
                    leastused = l
            lfu[x][leastused] = 1
            if ((pos_memoria[i] % 2) ==  0):
                cache[x][leastused] = [pos_memoria[i],pos_memoria[i]+1]
            else:
                cache[x][leastused] = [pos_memoria[i]-1,pos_memoria[i]]           
        washit = False
        imprimir_cache(cache)
        print(lfu)
        time.sleep(10) #Pausa de alguns segundos para que o usuário possa acompanhar o processo
    return hit, miss


tam, bloco, palavras, pos = menu_assocon()
mapeamento_associativoconjunto(tam, bloco, palavras, pos)