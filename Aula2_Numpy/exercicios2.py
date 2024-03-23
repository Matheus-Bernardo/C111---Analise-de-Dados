import numpy as np
'''
Exercicios propostos 2
'''

arr = np.random.randn(10)
print(arr)
# Definir a semente para reprodutibilidade
np.random.seed(5)

# Criar um array de floats com 10 elementos positivos e negativos entre 0 e 1
array_floats = np.random.uniform(-1, 1, 10)

# Multiplicar os valores por 100
array_multiplicado = array_floats * 100

# Criar um novo vetor com apenas a parte inteira dos números
array_inteiro = np.floor(array_multiplicado).astype(int)

print("Array de floats original:")
print(array_floats)

print("\nArray multiplicado por 100:")
print(array_multiplicado)

print("\nArray com a parte inteira dos números:")
print(array_inteiro)


#2.
# Definir a semente para reprodutibilidade
np.random.seed(10)
# Criar a matriz 4x4 com números inteiros aleatórios entre 1 e 50
matriz = np.random.randint(1, 51, size=(4, 4))
print("Matriz 4x4 com números inteiros aleatórios entre 1 e 50:")
print(matriz)

#3.
# Calcular a média de cada linha e de cada coluna
media_linhas = np.mean(matriz, axis=1)
media_colunas = np.mean(matriz, axis=0)

# Encontrar o maior valor para as linhas e para as colunas
maior_valor_linhas = np.max(media_linhas)
maior_valor_colunas = np.max(media_colunas)

print("\nMédia de cada linha:")
print(media_linhas)
print("\nMédia de cada coluna:")
print(media_colunas)
print(f"\nMaior valor das médias das linhas: {maior_valor_linhas}")
print(f"Maior valor das médias das colunas: {maior_valor_colunas}")


#4
# Contar a quantidade de aparições de cada número na matriz
valores, contagens = np.unique(matriz, return_counts=True)
# Mostrar apenas os números que aparecem duas vezes
numeros_que_aparecem_2_vezes = valores[contagens == 2]
print("\nNúmeros que aparecem duas vezes na matriz:")
print(numeros_que_aparecem_2_vezes)


