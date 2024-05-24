precos_produtos = {
    'banana': 2.50,
    'maça': 3.50,
    'laranja': 2.00,
    'pera': 4.00,
}

# imposto = []
# for produto in precos_produtos:
#     imposto.append(precos_produtos[produto] * 0.1)
# print(imposto)
impostos = [precos_produtos[produto] * 0.1 for produto in precos_produtos]

print(impostos)

#create a set exercice for me
# Path: codigo_diversos.py
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = []
# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)
# print(pares)
pares = [numero for numero in range(1, 11) if numero % 2 == 0]
print(pares)

# Path: codigo_diversos.py
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# quadrados = []
# for numero in numeros:
#     quadrados.append(numero ** 2)
# print(quadrados)
quadrados = [numero ** 2 for numero in range(1, 11)]
print(quadrados)

# Path: codigo_diversos.py
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# cubos = []
# for numero in numeros:
#     cubos.append(numero ** 3)
# print(cubos)
cubos = [numero ** 3 for numero in range(1, 11)]
print(cubos)

