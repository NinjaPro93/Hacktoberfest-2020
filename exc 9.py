'''
exc 99
Neste exercício temos duas listas com 5 posições (0 a 4). Em cada lista entraremos com cinco números. 
Mostrar os números e depois somar números que pertençam a mesma posição ou seja: [0]+[0], [1]+[1]
'''
lista12 = []
lista13 = []
lista14 = []

for i in range(5):
    x = float(input("Digite um número para a 1º lista:"))
    lista12.append(x)

for i in range(5):
    y = float(input("Digite um número para a 2º lista:"))
    lista13.append(y)

for i in range(5):
    z = (lista12[i])+(lista13[i])
    lista14.append(z)

print('='*30)

print('''
Listas originais:
{}
{}
Soma das listas:
{}
'''.format(lista12[:],lista13[:],lista14[:]))
