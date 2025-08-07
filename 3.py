fruta = ['maça','banana','laranja','mamão','pitaya']
# print(f'Todas as frutas ===>{fruta}')
# print(f'Todas as frutas  ===> {fruta[4]}')
# tamanho = len(fruta) 
# print(f'O tamanho da lista é {tamanho}')
# print('---------')
# fruta[1] = 'uva'
# print(f'Todas as frutas ===> {fruta}')
# fruta.insert(1,'abacaxi')
# print(f'Lista atualizada ===> {fruta}')
# fruta.insert(3,'tangerina')
# print(f'Lista atualizada2 ===> {fruta}')

# removendo pelo índice
print(fruta)
fruta.pop(1)
print(fruta)
frutanova = fruta.copy()
print(f'lista de frutas{fruta}')
print(f'lista de frutas nova {frutanova}')
#inserir item na frutanova
frutanova.append('melância')
print(f'lista de frutas{fruta}')
print(f'lista de frutas nova {frutanova}')
