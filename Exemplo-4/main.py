matriz = [[1, 2, 3], [4,5,6], [7,8,9]]
print(matriz[1][2]) # 6

# Enumerate
frutas = ['maçã', 'laranja', 'uva']
for i, frutas in enumerate(frutas):
    print(f'{i}: {frutas}')

# zip
nomes = ['David', 'Kalleb', 'Abenilton']
notas = [9.0, 7.5, 8.2]
for nome, nota in zip(nomes, notas):
    print(f'{nome}: {nota}')