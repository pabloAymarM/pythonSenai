#Crie um algoritmo que recebe um número de 0 a 100 e imprime uma mensagem                                                                                                   indicando se o número está na faixa de 0 a 25, 26 a 50, 51 a 75, ou 76 a 100.

num = int(input("Informe um número: "))

if num >= 0 and num <=25:
    print(f"O número {num} está na faixa de 0 a 25.")
elif num > 25 and num <=50:
    print(f"O número {num} está na faixa de 26 a 50.")
elif num > 50 and num <=75:
    print(f"O número {num} está na faixa de 51 a 75.")
elif num > 75 and num <=100:
    print(f"O número {num} está na faixa de 76 a 100.")
