# Exemplo real: IMC com funções separadas
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso 🔵'
    elif imc < 25:
        return 'Peso Normal 🟢'
    elif imc < 30:
        return 'Sobrepeso 🟠'
    else: 
        return 'Obesidade 🔴'

nome = input ('Nome: ')
peso = float(input('Peso (Kg): '))
altura = float(input('Altura(m): '))
imc = calcular_imc(peso, altura)
type_imc = classificar_imc(imc)

print (f'{nome}: IMC {imc:.2f} - {type_imc}')

