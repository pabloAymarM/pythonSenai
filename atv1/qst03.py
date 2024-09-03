#Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula: VOLUME = 3.14159 * R² * ALTURA.

print('==== CÁLCULO DE VOLUME ====')

alt = float(input('Altura da garrafa: (cm) '))
raio = float(input('Raio da garrafa: (cm) '))

volume = 3.14159 * raio**2 * alt

print(f'O volume da garrafa é {volume:.1f}cm³.')