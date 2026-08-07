produto = [
    (1200, 'Volante Racing Wheel', 6, 3),
    (1321, 'Fone Headset', 8, 8),
    (1201, 'Controle Dualshock 3', 3, 1),
    (909, 'PlayStation 4 Slim', 12, 13),
    (1189, 'HD Externo', 0, 3)
]

for produtos in produto: 
   codigo, nome, garantia, meses_de_uso = produtos
   print(f'\nCódigo: {codigo} \nNome: {nome} \nGarantia: {garantia} meses.\n')

if meses_de_uso <= garantia:
   print(f'Em garantia! Restam {garantia - meses_de_uso} meses')
elif garantia == 0:
   print(f'Garantia: Indisponível')
else:
   print(f'Venceu há {garantia - meses_de_uso} meses')

