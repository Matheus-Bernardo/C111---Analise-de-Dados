#Exercício 1

top_5_times = ['Manchester City','Real Madrid','Bayer de Munique','Arsenal','Liverpool']
print(top_5_times[:3])
print(top_5_times[-2:])
top_5_times.sort()
print(top_5_times)
if(top_5_times.count('Barcelona') > 0):
    posicaoBarca = top_5_times.index('Barcelona')
    print(posicaoBarca)
else:
    print('O barcelona não está na lita')


#Exercício 2
loja1 ={'Motog30','Galaxy S30','Iphone Pro Max 15'}
loja2 ={'Motog45','Galaxy A32','Iphone Pro Max 15'}

print("Loja 1 vende:",loja1, "Loja 2 vende:" , loja2)
print("Total de opções para comprar:",(len(loja1) + len(loja2)))
print(loja1&loja2)


#Exercicio 3
nome = input("Informe seu nome: ")
media = float(input("Qual é sua média " + nome+ "?"))

aluno ={
    'nome':nome,
    'media':media
}

if(aluno['media'] > 50):
    print("AP")
    aluno['situacao'] = "AP"
else:
    print("RP")
    aluno['situacao'] = "RP"

print(aluno)
