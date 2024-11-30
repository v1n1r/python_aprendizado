# Crie um script que peça para o usuário digitar o nome de 
# 5 bebidas favorita dele, armazenando esses valores em uma lista
# Na sequência, exiba na tela os elemetos da lista em ordem alfabética, um por linha,
# usando um laço de repetição for.

bebidas = []
i = 0

print('Digite o nome de 5 Bebidas')

while(i<5):

    print(f'Digite o nome da {i+1} bebida:')

    bebidas.append(input())
    i = i + 1

bebidas.sort()

print('A lista de bebidas em ordem alfabética é: ')
for bebida in bebidas:
    
    print(bebida)



    
