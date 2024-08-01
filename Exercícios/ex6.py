while True:
    try:
        print("me de dois numeros")
        numero_1 = int(input("Digite o primeiro numero: "))
        numero_2 = int(input("Digite o segundo numero: "))
        numero_3 = int(input("Digite o terceiro numero: "))

        if numero_1 > numero_2 and numero_3:
            resultado = f"{numero_1} é maior que {numero_2}"

        elif numero_2 > numero_1 and numero_3:
            resultado = f"{numero_2} é maior que {numero_1} e {numero_3}"
        elif numero_3 > numero_1 and numero_2:
            resultado = f"{numero_3} é maior que {numero_1} e {numero_2}"
        elif numero_1 == numero_2 == numero_3:
            resultado = f"Os números são iguais."
        elif numero_1 == numero_2 or numero_3 == numero_2 or numero_1 == numero_3:
            print("os dois numeros são iguais")
    except ValueError:
        print ("valor invalido")

    print(f"{resultado}")