#Faixa de Renda Anual Bruta                           Alíquota
#Até R$ 56.072,00                                                0%
#De R$ 56.072,01 a R$ 238.532,00                    7,50%
#De R$ 238.532,01 a R$ 522.400,00                  15%
#De R$ 522.400,01 a R$ 987.600,00                 22,50%
#Acima de R$ 987.600,00                                   27,50%
while True:
    while True:
        try:
            salario_anual = float(input("Digite o salario bruto anual:"))
            if salario_anual <= 0:
                print("Coloque um valor inválido.")
            else:
                break
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")
    if salario_anual <= 56072:
        print(f"Sua renda é: {salario_anual:.2f},00 portanto não haverá desconto.")
    elif salario_anual <= 238532:
        renda = salario_anual * 0.075
        print(f"Sua renda é: {salario_anual:2f},00 portanto o de o desconto é {renda:.2f}")
    elif salario_anual <=522400:
        renda = salario_anual * 0.15
        print(f"Sua renda é: {salario_anual:.2f},00 portanto o de o desconto é {renda:.2f}")
    elif salario_anual <= 987600:
        renda = salario_anual * 0.225
        print(f"Sua renda é: {salario_anual:.2f},00 portanto o de o desconto é {renda:.2f}")
    else:
        renda = salario_anual * 0.275
        print(f"Sua renda é: {salario_anual:.2f},00 portanto o de o desconto é {renda:.2f}")


