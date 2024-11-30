# São imutáveis

# tupla = (2,4,6,7,9)
# print(tupla)

# halogenios = ('F', 'Cl', 'Br', 'I', 'At')
# gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
# elementos = halogenios + gases_nobres
# t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)
# print(t1.count(3))

# halogenios = ('F', 'Cl', 'Br', 'I', 'At')
# gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
# elementos = halogenios + gases_nobres
# print(halogenios[:3])

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
print('Cl' in halogenios)

# Operações não disponíveis em tuplas: .sort(), .append(), .reverse(), .pop()...

# for elemento in elementos:
#     print(f'Elemento químico: {elemento}')

# grupo17 =list(halogenios)
# grupo17[0] = 'H'
# print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(type(alcalinos))

print(sorted(alcalinos))

# print(alcalinos.sort()) teste de erro