print("Calculadora de Ohm")
print("")
print("1 - resistencia")
print("2 - tensao")
print("3 - corrente")
print("4 - resistencia necessaria para um resistor")
print("")

opcao = int(input("Qual opcao desejada: "))


while opcao != 0:


    if opcao == 1:
        print("resistencia")
        print("")
        while True:
            try:
                tensao = float(input("digite a tensao em volts: "))
                if tensao > 0:
                    break
            except ValueError:
                print("valor invalido, digite um numero utilizando o ponto como separador. Ex: 1.0")

    while True:
        corrente = float(input("digite a corrente em amperes: "))
        if corrente > 0:
            break

    resistencia = tensao / corrente

    print(f"a resistencia é de {resistencia} 0")

    elif opcao == 2:
        print("tensao")
        print("")

    resistencia = float(input("digite a resistencia em ohms: "))
    corrente = float(input("digite a corrente em amperes: "))

    tensao = resistencia * corrente

    print(f"a tensao e de {tensao} volts")

elif opcao == 3:
    print("corrente")
    print("")

    tensao = float(input("digite a tensao em volts: "))
    resistencia = float(input("digite a resistencia em ohms: "))

    corrente = tensao / resistencia

    print(f"a corrente e de {corrente} amperes")

elif opcao == 4:
    print("resistencia resitor")
    print("")
    tensao_fonte = float(input("digite a tensao da fonte em volts: "))
    tensao_dispositivo = float(input("digite a tensao do dispositivo em volts: "))
    corrente = float(input("digite a corrente em amperes: "))

    resistencia_resitor = (tensao_forte - tensao_dispositivo) / corrente

    print(f"a resistencia necessaria desse resistor e de {resistencia_resistor} 0")
else:
    print("opcao invalida")

print("Calculadora de Ohm")
print("")
print("1 - resistencia")
print("2 - tensao")
print("3 - corrente")
print("4 - resistencia necessaria para um resistor")
print("")

opcao = int(input("Qual opcao desejada: "))

































