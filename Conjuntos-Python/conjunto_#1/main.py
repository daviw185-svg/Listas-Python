numeros = {1, 2, 3, 2, 1}
print(numeros) # {1, 2, 3} duplicatas sumidas

# Remover duplicatas de lista
lista = [1, 2, 3, 3, 3, 4]
print(set(lista)) # {1, 2, 3, 4}

# Operações 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) # União de dois conj.
print(a & b) # Interseção
print(a - b) # Diferença(o que "a" tem que "b" não tem)
print(a ^ b) # Diferença simétrica

# CASO 1: Detectar CPF duplicado em cadastro

cpfs = ['123.456.789-00', '345.435.357-24',
        '105.843.361-59', '345.435.357-24']

unicos = set(cpfs)
duplicados = len(cpfs) - len(unicos)
print(f'Total cadastrados: {len(cpfs)}')
print(f'CPFs únicos: {len(unicos)}')
print(f'Duplicados:{duplicados}')

# CADO 2: Coordenadas GPS - Tuplas garante que ninguém muda a posição

SENAI_SIG = (-15.8311, -48.0500)
lat, lon = SENAI_SIG
print(f'SENAI está em: {lat}, {lon}')

# CASO 3: Função que retorna múltiplos valores
def estatisticas(notas):
# Retorna média, maior e menor nota como tupla
 return sum(notas)/len(notas), max(notas), min(notas)

media, maior, menor = estatisticas([8.5, 7.0, 9.2, 6.5])
print(f'Média: {media:.2f} Maior: {maior:.2f} Menor: {menor:.2f}')