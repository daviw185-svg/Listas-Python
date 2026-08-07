nome = input('Nome do Aluno: ')
media = int(input('Digite a média da nota do aluno: '))
frequencia = float(input('Qual a frequência do aluno(de 0 a 1, exemplo: 0.85): '))

print(f'{nome} | {media} | {frequencia}')

if media >= 7 and frequencia >= 0.75:
    finalBom = print('Aprovado')
else : 
    finalRuim = print('Reprovado')