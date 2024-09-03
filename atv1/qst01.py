#Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
# A fórmula de conversão é F = (C * 9/5) + 32, sendo F a temperatura em Fahrenheit e C temperatura em Celsius.

tempC = float(input('Informe a sua temperatura em ºC: '))

tempF = (tempC*9/5) +32

print(f'A temperatura vonvertida é {tempC}ºC para {tempF}ºF.')