a = int(input('Informe um valor inteiro: '))
b = int(input('Informe outro valor inteiro: '))
c = int(input('Informe outro valor inteiro: '))
d = int(input('Informe outro valor inteiro: '))

# 4
if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
    print(f'{a},{b},{c},{d}')
    
# 3
elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print(f'{a},{b},{c}')
elif a % 2 == 0 and b % 2 == 0 and d % 2 == 0:
    print(f'{a},{b},{d}')
elif a % 2 == 0 and c % 2 == 0 and d % 2 == 0:
    print(f'{a},{c},{d}')
elif b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
    print(f'{b},{c},{d}')

# 2
elif a % 2 == 0 and b % 2 == 0:
    print(f'{a},{b}')
elif a % 2 == 0 and c % 2 == 0:
    print(f'{a},{c}')
elif a % 2 == 0 and d % 2 == 0:
    print(f'{a},{d}')
elif b % 2 == 0 and c % 2 == 0:
    print(f'{b},{c}')
elif b % 2 == 0 and d % 2 == 0:
    print(f'{b},{d}')
elif b % 2 == 0 and d % 2 == 0:
    print(f'{c},{d}')

#1
elif a % 2 == 0:
    print(f'{a}')
elif b % 2 == 0:
    print(f'{b}')
elif c % 2 == 0:
    print(f'{c}')
elif d % 2 == 0:
    print(f'{d}')
else:
    print('Nenhum número divisível por dois.')