#Calcular e apresentar o valor do volume de uma caixa retangular, utilizando a fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.
alt = float(input('Altura: (cm) '))
comp = float(input('Comprimento: (cm) '))
largura = float(input('Largura: (cm) '))

volume = alt * comp * largura

print(f'O volume da caixa é {volume}cm³.')