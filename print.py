# Sintaxe:
# print(objetos, argumentos)

mensagem = 'Função print()'
print(mensagem)
print('Aula de Python')

nome = 'Fábio dos Reis'
canal = 'Bóson Treinamentos'
print(canal,' - ', nome)

nome = input('Digite seu nome: ')
msg ='Olá ' + nome + '! Bem-vindo ao curso de Python!'
print(msg)
print('Outro texto')

print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na linha.', end='')
print(' Continuo na mesma linha!')

nome = 'Maria'
idade = 30
msg_formatada = 'O nome dela é {0} e ela tem {1} anos'.format(nome, idade)
print(msg_formatada)

nome = 'Fábio'
peso = 73.50
print(f'Olá, meu nome é {nome} e eu peso {peso} quilos.')

a = 10
b = 5
res = f'A soma de {a} com {b} é igual a {a+b}'
print(res)

valor = 125.579637
print(f'O valor é \'{valor:.2f}\'')

nome = 'João'
idade = 32
print(f'Nome: {nome}\tIdade:  {idade}')
