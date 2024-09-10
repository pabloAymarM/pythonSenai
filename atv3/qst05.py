#Faça um programa que recebe a quantidade de horas trabalhadas e o valor por hora de um funcionário.                                                                       Se o número de horas for superior a 40, o funcionário receberá um bônus de 50% sobre as horas extras.

qtdHoras = int(input("Informe a quantidade de horas trabalhadas: "))
valHora = float(input("Informe o seu valor p/hora: "))

if qtdHoras > 40:
    valHora *= 1.5
    print(f"Seu novo valor Hora será {valHora}")
else:
    print("Sem bônus.")