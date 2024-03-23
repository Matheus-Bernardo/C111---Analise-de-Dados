import numpy as np
'''
#trabalhando com textos
arr = np.array(['Matheus','Eliana','Leandro'])
print(np.char.find(arr,'M'))
arr2= arr[np.char.find(arr,'M')>=0]
print(arr2)

'''

arr = np.loadtxt('space.csv',delimiter=';',dtype=str,encoding='utf-8')

#questao 1
missao_sucesso = arr[arr[:, -1] == 'Success']
porcentagem = (missao_sucesso.shape[0]/arr.shape[0])*100
print(porcentagem,"%")


#questão 2
# Converter os valores da penúltima coluna para tipo numérico (float)
dados = arr[1:]
gastos = dados[:, -2].astype(float)
gastos_maior_que_zero = gastos[gastos > 0]
# Calcular a média dos gastos
media_gastos = np.mean(gastos_maior_que_zero)
print("Média de gastos de missões espaciais com valores disponíveis maiores que zero:", media_gastos)

#questão 3
dados = arr[1:]
# Extrair a coluna de localização
localizacao = dados[:, 2]
# Contar o número de ocorrências onde a localização contém 'USA'
missoes_EUA = np.count_nonzero(np.char.find(localizacao, 'USA') != -1)
print("Número de missões executadas pelos EUA:", missoes_EUA)

#questao4
dados = arr[1:]
# Filtrar apenas as linhas da empresa "SpaceX"
spacex_dados = dados[dados[:, 1] == 'SpaceX']
# Extrair a coluna de custo e converter para valores numéricos
custo_spacex = spacex_dados[:, -2].astype(float)
# Encontrar o índice do máximo valor de custo
indice_max_custo = np.argmax(custo_spacex)
# Extrair os detalhes da missão mais cara da SpaceX
missao_mais_cara_spacex = spacex_dados[indice_max_custo]
print("Missão mais cara realizada pela SpaceX:", missao_mais_cara_spacex)



#questao 5
dados = arr[1:]
# Criar um dicionário para armazenar o nome das empresas e a contagem de missões
empresas_missões = {}

# Iterar sobre as linhas dos dados
for linha in dados:
    empresa = linha[1]  # Nome da empresa na segunda coluna
    if empresa in empresas_missões:
        empresas_missões[empresa] += 1
    else:
        empresas_missões[empresa] = 1

# Exibir o nome das empresas e a quantidade de missões
for empresa, quantidade_missões in empresas_missões.items():
    print("Empresa:", empresa, "- Quantidade de missões:", quantidade_missões)