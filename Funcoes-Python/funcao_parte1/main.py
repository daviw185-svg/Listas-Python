# Função simples - sem parâmetros

def saudar():
    print('Olá! Bem-vindo ao SENAI!')
    print('Bons estudos!')

saudar() # Chamando a função 
saudar() # chamar várias vezes a mesma função

# Com Parâmetros

def saudarPessoas(nome, curso):
    print(f'Olá, {nome}')
    print(f'Bem-Vindo ao curso de {curso}')

saudarPessoas('David Willian', 'Python')
saudarPessoas('Daniele', 'Fullstack')

# Parâmetro com valor padrão
def potencia(base, expoente=2):
    return base ** expoente

print(potencia(5)) # 25 (expoente padrão = 2)
print(potencia(2,8)) # 256 
