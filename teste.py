try:
    # Código que pode gerar uma exceção
    lista = [1, 2, 3]
    indice = int(input("Digite um índice: "))
    elemento = lista[indice]
    print(f"O elemento é {elemento}")
except ValueError:
    # Código a ser executado se o usuário digitar um valor inválido
    print("Digite um índice válido.")
except IndexError:
    # Código a ser executado se o índice estiver fora dos limites da lista
    print("O índice está fora dos limites da lista.")
except:
    # Código a ser executado em caso de qualquer outra exceção
    print("Ocorreu um erro.")