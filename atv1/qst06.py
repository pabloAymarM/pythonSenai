#Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deve solicitar a cotação do dólar e também a quantidade de dólares disponível com o usuário.

real = float(input('Quantos reais você quer converter? R$'))
cotacao = float(input('Qual é a cotação?'))

dolar = real/cotacao

print(f'A cotação do dóllar está R${cotacao} e você tem {dolar:.2f} dólares.')