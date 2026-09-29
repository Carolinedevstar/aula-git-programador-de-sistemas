# # criando a lista
numeros = [10, 4, 6, 24, 56, 6, 87]

# # exibindo o tamanho da lista
# tamanho = len(numeros)
# print(f"O tamanho da lista é: {tamanho} elementos")

# # exibindo elementos específicos
# primeiro_elemento = numeros[0]
# terceiro_elemento = numeros[2]
# ultimo_elemento = numeros[-1]


# print(f"O primeiro elemento(indice 0) é: {primeiro_elemento} ")
# print(f"O terceiro elemento(indice 2) é: {terceiro_elemento} ")
# print(f"O último elemento(indice -1) é:{ultimo_elemento}")


for numero in sorted(numeros, reverse=True):
    print(numero)
