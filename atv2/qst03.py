sal = float(input('Informe o seu salário: R$'))
finan = float(input('Informe o valor do financiamento: R$'))

conversao = sal * 5

if finan <= conversao:
    print('Financiamento concedido.')
else:
    print('Financiamento negado.')
    
print('===== Obrigado por nos consultar =====')