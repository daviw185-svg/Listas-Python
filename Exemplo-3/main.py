alunos = ['Carlos',
          'Cauã',
          'David',
          'Michael']

# append, insert, remove, pop
alunos.append('Jackson') # append insere ao final

alunos.insert(0,'Willian') # Eu esolho a posição aonde vai ficar
alunos.remove('Carlos') 
ultimo = alunos.pop()
print(alunos, '| removido: ', ultimo)

# sort vs sorted
alunos.sort() # Modifica no Lugar
nova = sorted(alunos, reverse=True) # Cria uma nova lista
print(alunos, nova)

# in, index, count
print('Michael' in alunos) # Verifica se Michael existe na lista
print(alunos.index('Michael')) # Mostra o índice do nome Michael na lista