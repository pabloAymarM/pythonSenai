#Crie um programa que receba o valor de uma compra e a quantidade de parcelas desejadas (somente de 1 a 24).                                                                O programa deve calcular o valor da parcela, aplicando juros de 1.5% ao mês se o número de parcelas for maior que 12.                                                    Exiba o valor total a ser pago e o valor de cada parcela.

valCompra = float(input("Informe o valor da compra: R$"))
qtdParcelas = int(input("Informe a quantidade de parcelas: "))

if qtdParcelas > 12:
    juros = valCompra * 1.5 * qtdParcelas
    valTotal = valCompra + juros
    valParcela = valTotal / qtdParcelas
    print(f"O valor total do produto será R${valTotal:.2f} e o valor de cada parcela será R${valParcela:.2f}.")
else:
    print("O valor continuaará o mesmo.")
    