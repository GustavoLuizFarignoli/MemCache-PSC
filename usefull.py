def menu_direto ():
    print("Performance em Sistemas Ciberfísicos - Gustavo Luiz")
    print("*" + ("-"*30) + "*")
    print("Primeiramente, digite o tamanho da mémoria cache")
    while True:
        try:
            tamanho_cache = int(input("->"))
            break
        except ValueError:
            print("Por favor, digite um valor válido")
            continue
    print("Agora, digite a lista de posições a serem acessadas. Caso deseje sair digite -1")
    pos_memoria = []
    while True:
        try:
            print("Digite a posição na mémoria")
            x = int(input("->"))
            if(x != -1):
                pos_memoria.append(x)
                continue
            else:
                break
        except ValueError:
            print("Por favor, digite um valor válido")
            continue
    return tamanho_cache, pos_memoria;


def menu_assocon():
    print("Associativo")
    print("Performance em Sistemas Ciberfísicos - Gustavo Luiz")
    print("*" + ("-"*30) + "*")
    print("Primeiramente, digite quantidade de conjuntos na mémoria cache")
    while True:
        try:
            tamanho_cache = int(input("->"))
            break
        except ValueError:
            print("Por favor, digite um valor válido")
            continue
    print("Agora, digite o tamanho deste conjunto (quantos blocos)")
    while True:
        try:
            blocos = int(input("->"))
            break
        except ValueError:
            print("Por favor, digite um valor válido")
            continue
    print("Agora, digite quantas palavras terão no bloco")
    while True:
        try:
            palavras = int(input("->"))
            break
        except ValueError:
            print("Por favor, digite um valor válido")
            continue
    print("Agora, digite a lista de posições a serem acessadas. Caso deseje sair digite -1")
    pos_memoria = []
    while True:
        try:
            print("Digite a posição na mémoria")
            x = int(input("->"))
            if(x != -1):
                pos_memoria.append(x)
                continue
            else:
                break
        except ValueError:
            print("Por favor, digite um valor válido")
            continue
    return tamanho_cache, blocos, palavras, pos_memoria
