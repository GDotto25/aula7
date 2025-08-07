#lista vazia
#usuario quem informa o que será incluido na lista

print('Lista de Frutas Master Top')
fruta =[]
for i in range(3):
    x = input(f'Digite o nome da {i+1}ª fruta: ')
    fruta.append(x)
    print(f'Lista de frutas {fruta}')