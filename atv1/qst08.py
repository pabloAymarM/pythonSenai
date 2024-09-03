#Construir um algoritmo em pseudocódigo que calcule o índice de massa corpórea (IMC) de uma pessoa.
#O IMC é calculado dividindo-se o peso da pessoa, em kg, pelo quadrado da sua altura, em metros.

print('==== CÁLCULO DE IMC ====')
peso = float(input('Informe o seu peso em KG: '))
alt = float(input('Informe o sua altura em m: '))

imc = peso/(alt**2)