dist = float(input('Informe a distância percorrida em KM: '))
carro = int(input('Informe o tipo de carro: [1, 2, 3] '))

if carro == 1:
    consumo = dist / 8
    print(f'O seu carro consumirá {consumo:.1f}L/Km')
elif carro == 2:
    consumo = dist / 9
    print(f'O seu carro consumirá {consumo:.1f}L/Km')
elif carro == 3:
    consumo = dist / 12
    print(f'O seu carro consumirá {consumo:.1f}L/Km')
else:
    print('Tente Novamente.')