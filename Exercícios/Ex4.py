while True:
    try:
        print("me de dois numeros")
        numero_1 = int(input("Digite o primeiro numero: "))
        numero_2 = int(input("Digite o segundo numero: "))

        if numero_1 > numero_2:
            resultado = f"{numero_1} é maior que {numero_2}"

        elif numero_1 < numero_2:
            resultado = f"{numero_2} é maior que {numero_1}"
    except ValueError:
        print ("valor invalido")

    print(f"{resultado}")

