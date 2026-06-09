# =============================================================================
# LISTAS — Exercícios intermediários (6 a 10)
# =============================================================================


# Exercício 6: Eliminação de Duplicatas
# Dada a lista de emails abaixo, crie uma nova lista que contenha
# apenas os emails únicos (sem repetição).
#
# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = []
# for email in emails:
#     if email not in emails_unicos:
#         emails_unicos.append(email)
# print(emails_unicos)

# Exercício 7: Filtragem de Dados
# Dada a lista de idades abaixo, crie uma nova lista contendo apenas
# as idades maiores ou iguais a 18.
#
# idades = [22, 15, 30, 17, 18]
# idade_valida = [idade for idade in idades if idade >= 18]
# print(idade_valida)

# Exercício 8: Ordenação Personalizada
# Dada a lista de dicionários abaixo, ordene as pessoas pelo campo "nome".
#
# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]
# def ordenar_por_nome(e):
#     return e["nome"]
# pessoas.sort(key=ordenar_por_nome)
# print(pessoas)

# Exercício 9: Agregação de Dados
# Dado o conjunto de números abaixo, calcule e imprima a média dos valores.
#
# numeros = [10, 20, 30, 40, 50]
# media = sum(numeros) / len(numeros)
# print(media)


# Exercício 10: Divisão de Dados em Grupos
# Dada a lista de valores abaixo, separe os números em duas listas:
# uma com os valores pares e outra com os valores ímpares.
#
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []
for numero in valores:
    if numero % 2:
        impares.append(numero)
    else:
        pares.append(numero)
print(pares)
print(impares)
