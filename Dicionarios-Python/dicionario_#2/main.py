turma = {
    'Paulo': {'Nota': 9.0, 'Frequência': 90},
    'Brunno': {'Nota': 7.5, 'Frequência': 64},
    'Peter Parker': {'Nota': 8.9, 'Frequência':75},
    'Miles Morales': {'Nota': 5.9, 'Frequência':84},
}

# Acesso aninhado
print(turma['Peter Parker']['Nota'])
print(turma['Miles Morales']['Frequência'])

# Percorrendo e drinking decision
for nome, dados in turma.items():
    ok = dados['Nota'] >= 7.0 and dados['Frequência'] >= 75
    print(f'{nome}: {'Aprovado' if ok else 'Reprovado'}')