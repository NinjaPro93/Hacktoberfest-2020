'''
exc 7
Preencher uma lista com 5 números e guardar o cubo dos números em outro lista. 
Mostrar as duas listas.
'''
lista11 = []
cubos = []

for i in range(5):
    x = float(input("Digite um número:"))
    lista11.append(x)

for i in range(5):
    y = lista11[i]**3
    cubos.append(y)

print('='*30)

print('''
Nºs originais: {}
Elevados ao cubo: {}
'''.format(lista11[:],cubos[:]))
