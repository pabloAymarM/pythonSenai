#4. Escreva um programa que recebe o salário de um funcionário e calcula o imposto de renda baseado nas seguintes condições:                                               a. Até R$ 1.900, isento                                                                                                                                                     b. De R$ 1.901 até R$ 2.800, 7.5% de imposto                                                                                                                               c. De R$ 2.801 até R$ 3.700, 15% de imposto                                                                                                                                  d. Acima de R$ 3.700, 22.5% de imposto

print("===== IMPOSTO =====")
salario = float(input("Informe o seu salário: "))

if salario <= 1900:
    print("Insento de Imposto.")
elif salario > 1900 and salario <= 2800:
    imposto = salario * 0.075
    print(f"Do seu salário é retirado {imposto}, 7.5% dele.")
elif salario > 2800 and salario <= 3700:
    imposto = salario * 0.15
    print(f"Do seu salário é retirado {imposto}, 15% dele.")
elif salario > 3700:
    imposto = salario * 0.225
    print(f"Do seu salário é retirado {imposto}, 22.5% dele.")