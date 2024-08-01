loop = 1
while loop != 0:
    try:
        print("Bem vindo, vamos descobrir o ano!")
        ano = int(input("digite um numero de 1 a 12: "))



        if ano ==  1:
            print("Janeiro")
        elif ano == 2:
            print("Fevereiro")
        elif ano == 3:
            print("Março")
        elif ano == 4:
            print("Abril")
        elif ano == 5:
            print("Maio")
        elif ano == 6:
            print("Junho")
        elif ano == 7:
            print("Julho")
        elif ano == 8:
            print ("Agosto")
        elif ano == 9:
            print("Setembro")
        elif ano == 10:
            print("Outubro")
        elif ano == 11:
            print("Novembro")
        elif ano == 12:
            print("Dezembro")

        else:
            print("esse número não é válido, insira um correto por favor!")

    except ValueError:
        print("esse número não é válido, insira um correto por favor!")

    loop = int(input("digite 0 se quiser sair do jogo: "))