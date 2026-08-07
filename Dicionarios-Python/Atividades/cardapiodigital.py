# Bahia Peixe - Cardápio Digital

cardapio = {
        'Isca de Peixe': {'Categoria': 'Prato principal' , 'Preço': 67.00},
        'Tilápia': {'Categoria': 'Prato principal' , 'Preço': 75.00},
        'Barca de Sushi': {'Categoria': 'Peças' , 'Preço': 80.00}, 
        'Suco de Laranja': {'Categoria': 'Bebidas' , 'Preço': 7.00}, 
        'Suco de Maracujá': {'Categoria': 'Bebidas' , 'Preço': 7.00}, 
        'Refri Coca-Cola 2L': {'Categoria': 'Bebidas' , 'Preço': 11.00}, 
        'Refri Coca-Cola Zero 2L': {'Categoria': 'Bebidas' , 'Preço': 10.00}
}

def cardapioDigital ():
    type = {}
    for nome, dados in cardapio.items():
        cat = dados['Categoria'] 
        type.setdefault(cat, []).append((nome, dados['Preço']))
    for cat, itens in sorted(type.items()):
        print(f'\n{cat}')
        for nome, preco in itens:
            print(f'{nome:<22} R${preco:<6.2f}')

while True: 
    print(f'\n[1] Exibir cardápio completo \n\n[2] Buscar prato \n\n[3] Adicionar prato \n\n[4] Atualizar preço \n\n[5] Remover prato \n\n[0] Sair')
    consulta = input("Opção: ")
    if consulta == '1':
        cardapioDigital()
    elif consulta == '2':
        nome = input("Nome: ")
        dados = cardapio.get(nome)
        if dados:
            print(f'{nome} {dados['Categoria']} R${dados['Preço']:.2f}')
        else:
            print(f'Prato não encontrado')
    elif consulta == '3':
        nome = input('Adicione um prato novo ou bebida: ')
        if nome in cardapio:
             print(f'Esse prato já existe')
        else:
            cat = input('Categoria do novo prato: ')
            preco = float(input('Preço do novo prato (R$): ')) 
            cardapio[nome] = {'Categoria': cat, 'Preço': preco}
            print(f'Prato Adicionado')
    elif consulta == '4':
        nome = input('Nome do Prato: ')
        if nome in cardapio:
            cardapio[nome]['Preço'] = float(input('Digite o novo preço (R$): '))
            print('Preço Atualizado')
        else: 
             print('Atualização Indisponível')
    elif consulta == '5':
        nome = input('Nome do Prato: ')
        if nome in cardapio:
             del cardapio[nome]
             print('Prato Removido')
        else:
             print('Prato não encontrado')
    elif consulta == '0':
        print('Alright, programa encerrado. Até logo')
        break   
    else:
        print('Opção Inválida')