sexo = str(input('Informe o seu sexo (M/F): '))
h = float(input('Informe o sua altura em m: '))

if sexo == 'M' or sexo == 'm':
    peso = (72.7 * h) - 58
    print(f'Seu peso ideal é: {peso:.1f}Kg.')
elif sexo == 'F' or sexo == 'f':
    peso = (62.1 * h) - 44.7
    print(f'Seu peso ideal é: {peso:.1f}Kg.')
else:
    print('Tente Novamente.')