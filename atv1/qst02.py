#Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius.
#A fórmula de conversão é C = (F − 32) × 5/9, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

tempF = float(input('Informe a sua temperatura em ºF: '))
tempC = (tempF-32) * 5/9

print(f'A temperatura vonvertida é {tempF}ºF para {tempC}ºC.')