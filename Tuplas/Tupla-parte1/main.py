# Criar Tupla
coordenada = (-15.77, -47.92)
#               0        1     - Posição
rgb = (255, 0, 0)
unit = (42,)

lat, lon = coordenada
print(f'Brazilia: {lat}, {lon}')

# Retorno múltiplo de função
def minmax(lista):
    return min(lista), max(lista)

notas = [7.5, 9.0, 5.5, 8.2]
menor, maior = minmax(notas)
print(f'Menor: {menor} Maior: {maior}')

# Tentando modificar uma tupla
coordenada[0] = -12.10 # TypeError