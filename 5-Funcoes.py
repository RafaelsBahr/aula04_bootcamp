# =============================================================================
# FUNÇÕES — Exercícios (16 a 20)
# =============================================================================


# Exercício 16: Soma de Lista
# Escreva uma função que receba uma lista de números como argumento
# e retorne a soma de todos eles.
# Teste a função com: [1, 2, 3, 4, 5]

# numeros = [1, 2, 3, 4, 5]
# def soma(n: list):
#     return sum(n)

# print(soma(numeros))



# Exercício 17: Número Primo
# Crie uma função que receba um número inteiro e retorne True se ele
# for primo, ou False caso contrário.
# Lembre-se: um número primo é divisível apenas por 1 e por ele mesmo.
# Teste com os valores: 2, 7, 10, 13, 1
numero = [2, 7, 10, 13, 1]

# def teste_primo(n: int):
#     eh_primo = True
#     if n <= 1:
#         eh_primo = False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 eh_primo = False
#                 break
#     if eh_primo:
#         print(f"O numero {n} é primo!")
#         return True
#     else:
#         print(f"O numero {n} NÃO é primo!")
#         return False

# for num in numero:
#     teste_primo(num)


# Exercício 18: String Revertida
# Desenvolva uma função que receba uma string como argumento
# e retorne essa mesma string com os caracteres em ordem inversa.
# Teste com: "engenharia"
# text = "engenharia"
# def reverse_text(text):
#         return text[::-1]
# print(reverse_text(text))


# Exercício 19: Pares que Somam a um Alvo
# Implemente uma função que receba dois argumentos:
#   - uma lista de números
#   - um número alvo
# A função deve retornar todas as combinações de pares da lista
# cujos valores somem exatamente ao número alvo.
# Teste com: lista = [1, 2, 3, 4, 5], alvo = 5


# def combinacao_alvo(lista_numeros: list, n_alvo: int):
#     lista_de_combinacoes = []
#     for numero1x in range(len(lista_numeros)):
#         for numero2x in range(numero1x + 1, len(lista_numeros)):
#             if lista_numeros[numero1x] + lista_numeros[numero2x] == n_alvo:
#                 combinacoes = []
#                 combinacoes.append(lista_numeros[numero1x])
#                 combinacoes.append(lista_numeros[numero2x])
#                 lista_de_combinacoes.append(combinacoes)
#     return lista_de_combinacoes
            
# lista = [1, 2, 3, 4, 5]
# alvo = 5
# print(combinacao_alvo(lista, alvo))


# Exercício 20: Chaves Ordenadas de um Dicionário
# Escreva uma função que receba um dicionário como argumento
# e retorne uma lista com suas chaves em ordem alfabética.
# Teste com: {"banana": 3, "maçã": 1, "cereja": 2}

dicionario = {"banana": 3, "maçã": 1, "cereja": 2}

def funcao(dicionario:dict):
    lista_chaves_ordem_alfabetica = []
    for i in dicionario:
        lista_chaves_ordem_alfabetica.append(i)
    lista_chaves_ordem_alfabetica.sort()
    return lista_chaves_ordem_alfabetica

print(funcao(dicionario))

