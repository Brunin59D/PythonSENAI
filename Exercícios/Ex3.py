while True:
    try:
        print("me fale o ano em que você nasceu")
        ano = int(input("em qual ano você nasceu?: "))
        idade = 2024 - ano

        if idade >= 18:
            print("você é maior de idade")

        else:
            resultado = ("menor de idade")
    except ValueError:
        print("invalido")
