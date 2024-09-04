sal = float(input('Informe o seu salário: R$'))

if sal < 600:
    sal *= 1.3
    print(f'Seu novo salário é R${sal:.2f}.')
else:
    print('Você não tem direito ao aumento.')