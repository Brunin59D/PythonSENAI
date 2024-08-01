while True:
    try:
        numero = int(input("digite um numero: "))

        if numero < 0:
            resultado = "negativo👎"
        else:
            resultado = "positivo👍"

        print(resultado)
    except ValueError:
        print("valor invalido")