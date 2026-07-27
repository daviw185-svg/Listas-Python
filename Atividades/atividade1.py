temperaturas_registradas = [23.4, 21.2, 24.7, 23.6,23.4, 22.9]

media = sum(temperaturas_registradas) / len(temperaturas_registradas) # Média Aritmética
maximo = max(temperaturas_registradas)
minimo = min(temperaturas_registradas)

# Verificar cada número
days = 0
for temp in temperaturas_registradas:
    if temp > media:
        days += 1

# Colocar as temperaturas registradas em ordem crescente        
nova = sorted(temperaturas_registradas)

print(f'Temperaturas registradas: {temperaturas_registradas}')
print(f'========Relatório Climático=========')
print(f'A média das temperaturas é: {media:.2f}')
print(f'A Temperatura máxima registrada: {maximo:.2f}')
print(f'A Temperatuta mínima registrada: {minimo:.2f}')
print(f'Dias que a temperatura foi maior que a média: {days}')
print(f'Ordem crescente: {nova}')
