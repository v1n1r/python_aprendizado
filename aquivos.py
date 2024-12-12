# # Manipulação de arquivos de texto


# # print(f'\Método read():\n')
# # print(manipulador.read())

# # print(f'\Método read():\n')
# # print(manipulador.readline())
# # print(manipulador.readline())

# # print(f'\Método read():\n')
# # print(manipulador.readlines())

# texto = input('Qual termo deseja procurar no aqrquivo?')

# try: 
#     manipulador = open('arquivo.txt', 'r', encoding='utf-8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#             print(f'A string foi econtrada!')
#             print(linha)
#         else:
#             print('Não encaontrado')
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     manipulador.close()

# Escrever em arquivos de texto

# try: 
#     manipulador = open('arquivo.txt', 'w', encoding='utf-8')
#     manipulador.write('Bóson Treinamentos\n')
#     manipulador.write('Como criar um arquivo de texto com Python.')
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     manipulador.close()

# try: 
#     manipulador = open('arquivo.txt', 'a', encoding='utf-8')
#     manipulador.write('Phyton é muito empregado em IA\n')
#     manipulador.write('Inteligência Artificial veio para ficar!')
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     manipulador.close()


# texto = '\nPython é usado em Ciência de dados extensivamente'

# try: 
#     manipulador = open('arquivo.txt', 'a', encoding='utf-8')
#     manipulador.write(texto)
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     manipulador.close()

frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola']
try: 
    manipulador = open('frutas.dat', 'w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()

# Ler o arquivo criado:

try:
    manipulador = open('frutas.dat', 'r', encoding='utf-8')
    print(manipulador.read())
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()