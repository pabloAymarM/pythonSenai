#Calcular e apresentar em metros por segundo, o valor da velocidade de um projétil, que percorre uma distância em Km a um espaço de tempo em minutos.                 Utilizar a fórmula VELOCIDADE = (DISTANCIA * 1000) / (TEMPO*60).

dist = float(input('Informe a distância percorrida em KM: '))
tempo = float(input('Informe o tempo que foi percorrido em MIN: '))

mPorS = (dist*1000)/(tempo*60)

print(f'A velocidade do projétil foi de {mPorS:.2f}m/s')