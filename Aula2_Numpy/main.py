import numpy as np

'''
Exercicios propostos 1
'''

# Criar um array de tamanho 21 com valores linearmente espaçados entre 0 e 1
array_linear = np.linspace(0, 1, 21)
print(array_linear)

#Crie dois arrays de pares entre 0 a 50 e de 52 a 100 e concatene
arr1 = np.arange(0,51,2)
arr2 = np.arange(52,101,2)
arrays_concat = np.concatenate((arr1,arr2))
print(arrays_concat)

#ordene em ordem decrescente o array resultante da questão anterior
arrayDecrescente = np.flip((arrays_concat))
print(arrayDecrescente)

#crie uma matriz formada comente por uns de tamananho 3x4 e depois transforme em em um array de 1-d
# Criar uma matriz 3x4 contendo apenas uns
matriz_uns = np.ones((3, 4))
# Transformar a matriz em um array 1D
array_1d = matriz_uns.ravel()
print("Matriz 3x4 de uns:")
print(matriz_uns)
print("\nArray 1D:")
print(array_1d)



#crie uma matriz de tamanho qualquer.Extraia seu número de linhas e colunas, multiplique-os, e diga se esta matriz poderia tornar um vetor com numero par ou impar de elementos
# Criar uma matriz de tamanho qualquer, por exemplo, 4x3
matriz = np.random.randint(1, 10, size=(4, 3))
# Obter o número de linhas e colunas da matriz
num_linhas, num_colunas = matriz.shape
# Calcular o produto do número de linhas e colunas
total_elementos = num_linhas * num_colunas
# Verificar se o número total de elementos é par ou ímpar
if total_elementos % 2 == 0:
    print("O número total de elementos na matriz é par.")
else:
    print("O número total de elementos na matriz é ímpar.")

print("\nMatriz:")
print(matriz)



'''
Exercicios propostos 2
'''
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

'''

'''
Exercicios propostos 3
'''

