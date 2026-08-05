aluno = {} # vazio
aluno['nome'] = 'Carlos'
aluno['idade'] = 17
aluno['nota'] = 8.5
print(aluno)

# Forma compacta
aluno2 = {'Nome': 'Cauã', 
          'Idade': 18, 
          'Nota': 9.0 }

print(aluno2.get('Nome')) # Puxa somente o 'Nome'
print(aluno2.get('email')) # None - sem erro
print(aluno2.get('email', 'N/A')) # Valor Padrão

# Percorrendo
for chave, valor in aluno2.items():
    print(f'{chave}: {valor}')