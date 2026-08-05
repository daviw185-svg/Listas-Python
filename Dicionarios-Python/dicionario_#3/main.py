# Lista de dicionários
produtos = [
    {'Nome': 'Mini Reator Arc', 'Preço': 2359.90, 'Categoria': 'Fonte de Energia'},
    {'Nome': 'Capacete Tamanho Adulto', 'Preço': 349.90, 'Categoria': 'Cabeça'},
    {'Nome': 'Par de luvas de propulsão', 'Preço': 278.90, 'Categoria': 'Propulsão'},
    {'Nome': 'Par de botas de propulsão', 'Preço': 248.90, 'Categoria': 'Propulsão'},
]

# Filtrar
energy = [prod for prod in produtos if prod['Categoria']=='Fonte de Energia'] 
propulsion = [prod for prod in produtos if prod['Categoria']=='Propulsão'] 
print(len(propulsion)) # len - Serve para dizer quantos produtos da categoria "energy" existe
"""
 prod for prod - atribuindo um sobrenome porque o Python 
 não permite usar o nome original da variável, 
 que no caso é "produtos"
"""

# Ordenar por preço
ordem = sorted(produtos, key=lambda prod: prod['Preço']) # Nesse caso, para ordenar pode usar o nome original do dicionário
for prod in ordem: # Buscar o valor dos produtos e guardar na variável "ordem"
    print(f'- {prod['Nome']:30} R$ {prod['Preço']:.2f}')