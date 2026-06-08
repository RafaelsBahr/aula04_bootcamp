# =============================================================================
# DICIONÁRIOS — Exercícios (11 a 15)
# =============================================================================


# Exercício 11: Atualização de Dados
# Dada a lista de produtos abaixo, atualize o preço do produto com id 2 para 90
# e imprima a lista atualizada.
#
# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# for produto in produtos:
#     if produto["id"] == 2:
#         produto["preço"] = 90
# print(produtos)


# Exercício 12: Fusão de Dicionários
# Dados os dois dicionários abaixo, crie um único dicionário que contenha
# todos os pares chave-valor de ambos e imprima o resultado.
#
# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}
# dicionario_completo = {}
# for chave in dicionario1:
#     dicionario_completo[chave] = dicionario1[chave]
# for chave in dicionario2:
#     dicionario_completo[chave] = dicionario2[chave]
# print(dicionario_completo)


# Exercício 13: Filtragem de Dados em Dicionário
# Dado o dicionário de estoque abaixo, crie um novo dicionário contendo
# apenas os produtos com quantidade maior que 0.
#
# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
# em_estoque = {item: estoque[item] for item in estoque if estoque[item] > 0}
# # for item in estoque:
# #     if estoque[item] > 0:
# #         em_estoque[item] = estoque[item]
# print(em_estoque)



# Exercício 14: Extração de Chaves e Valores
# Dado o dicionário abaixo, crie duas listas separadas:
# uma com todas as chaves e outra com todos os valores.
#
# dicionario = {"a": 1, "b": 2, "c": 3}
# chaves = [chave for chave in dicionario]
# valores = [dicionario[valor] for valor in dicionario]
# # for chave in dicionario:
# #     chaves.append(chave)
# print(chaves)
# # for valor in dicionario:
# #     valores.append(dicionario[valor])
# print(valores)

# Exercício 15: Contagem de Frequência de Itens
# Dada a string abaixo, conte quantas vezes cada caractere aparece
# e armazene o resultado em um dicionário.
# Dica: espaços também são caracteres e devem ser contados.
#
texto = "engenharia de dados"
contador_caractere = {}
for letra in texto:
    if letra not in contador_caractere:
        contador_caractere[letra] = 1
    else:
        contador_caractere[letra] += 1
print(contador_caractere)