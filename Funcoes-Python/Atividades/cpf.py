def validar_cpf(cpf):
    if len(cpf) != 11: 
        return False

    if len(set(cpf)) == 1:
        return False
    return True
"""
len(cpf) - Conferir a quantidade de carcteres
len(set(cpf)) == 1 - Conferir se todos os caracteres são iguais, se for, será um cpf inválido
return True - não foi necessário o uso do else, ele já vai direto
digitos_unicos = len(set(cpf)) - a variável de verificação
"""
cpf = input('Digite o seu CPF (Insira somente números, exatamente 11 caracteres, sem ponto e traço): ')
digitos_unicos = len(set(cpf))
print(f'CPF: {cpf} - {validar_cpf(cpf)}')