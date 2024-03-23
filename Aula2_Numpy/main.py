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


