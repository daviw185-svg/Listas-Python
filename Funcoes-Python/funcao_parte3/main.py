# Escopo variável
def minha_funcao():
    variavel_local = 'Só existe aqui dentro'
    print(variavel_local) # funciona

minha_funcao()
# Print(variavel_local) # Name Error - não existe aqui

# Variável global
mensagem = 'Sou Global'

def outra_funcao():
    print(mensagem) # pode ler variável global

outra_funcao()