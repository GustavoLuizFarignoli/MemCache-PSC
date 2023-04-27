def inicializar_cache(tamanho_cache,blocos,palavras=2):
    cache = {}
    for i in range(tamanho_cache):
        bloco = []
        for j in range(blocos):
            palavra = []
            for z in range(palavras):
                palavra.append(-1)
            bloco.append(palavra)
        cache[i] = bloco
    return cache

def imprimir_cache(cache):
    print("-" * 32)
    print("Posição Cache" + "|" + "Posições na memória")
    print("-" * 32)
    for i in range(len(cache)):
        #print(f"      {i}       |      {cache[i][0][0]}       ")
        for j in range(len(cache[i])):
            for k in range(len(cache[i][j])):
                if (j != 0 or k != 0):
                    print(f"              |      {cache[i][j][k]}       ")
                else:
                    print(f"      {i}       |      {cache[i][j][k]}       ")
            print("-" * 32)



a = inicializar_cache(2,2)
imprimir_cache(a)
