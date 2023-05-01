import usefull
import time

def inicializar_cache(tamanho_cache):
    cache = {}
    for i in range(tamanho_cache):
        cache[i] = -1
    return cache

def imprimir_cache(cache):
    print("-" * 32)
    print("Posição Cache" + "|" + "Posição na memória")
    print("-" * 32)
    for i in cache:
        print(f"      {i}       |      {cache[i]}       ")
        print("-" * 32)

def mapeamento_direto(tamanho_cache, pos_memoria, hit=0, miss=0):
    cache = inicializar_cache(tamanho_cache)
    print(f"Tamanho da cache {tamanho_cache}") #Preferi fazer aqui e não na funçao imprimir, para não imprimir o tamanho da cache em toda a iteração, menos poluição visual ao usuário
    imprimir_cache(cache)
    time.sleep(10) #Pausa de alguns segundos para que o usuário possa acompanhar o processo
    for i in range (len(pos_memoria)):
        print(f"Linha {i} | Posição da memória requisitada: {pos_memoria[i]}")
        x = pos_memoria[i] % tamanho_cache
        if (pos_memoria[i] == cache[x]):
            print ("Status: Hit")
            hit += 1
        else:
            print("Status: Miss")
            miss += 1
            cache[x] = pos_memoria[i]
        imprimir_cache(cache)
        time.sleep(10) #Pausa de alguns segundos para que o usuário possa acompanhar o processo
    print(f"- Total de posições de memórias acessadas: {len(pos_memoria)}")
    print(f"- Total de Hits: {hit}")
    print(f"- Total de Misses: {miss}")
    print(f"- Total de acerto: {(hit/len(pos_memoria)) * 100}%")


#tam, mem = usefull.menu_direto();
#mapeamento_direto(tam,mem)