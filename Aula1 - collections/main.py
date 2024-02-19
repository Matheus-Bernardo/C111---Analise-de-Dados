#Coleções

#1. Tupla() - Coleção imutavél
#nomes = ('Goku','Vegeta','Trunks','Gohan')
#print(nomes)

# #slicing
# print(nomes[0])
# print(nomes[:2])
# print(nomes[1:3])
# print(nomes[-2])

#2. Listas[] - Absolutamente mutavel
# nomes = ['Goku','Vegeta','Trunks','Gohan']
# #add elementos
# nomes.append('Picollo')
# #update
# nomes[0] = 'Bulma'
# #delete
# nomes.remove('Trunks')#remove por valor
# del nomes[1] #remoção por indice
# #select
# print(nomes)

#3.Conjunto {} - não guarda a ordem dos elementos
#não guarda elementos repetidos
#Nao tem updates
#nomes = {'Goku','Vegeta','Trunks','Gohan'}
#add
#nomes.add('Bulma')
#nomes.add('Goku')
#print(nomes)
#delete
#nomes.remove('Trunks')


#4.Dicionario {}
#indices Customizaveis
pessoa = {
    'nome': 'Goku',
    'idade':42
}
pessoa1 = {
    'nome': 'Bulma',
    'idade':22
}

#add
pessoa['sexo'] = 'M'
#delete
del pessoa['idade']
#update
pessoa['nome'] = 'gohan'

pessoas = [pessoa,pessoa1]
print(pessoas[0])