while True:
    try:
        print("Bem vindo, vamos descobrir o dia!")
        dia = int(input("digite um numero de 1 a 7: "))



        if dia ==  1:
            print("Hoje é domingo")
        elif dia == 2:
            print("hoje é segunda feira")
        elif dia == 3:
            print("hoje é terça feira")
        elif dia == 4:
            print("hoje é quarta feira")
        elif dia == 5:
            print("hoje é quinta feira")
        elif dia == 6:
            print("hoje é sexta feira ihuuuuu")
        elif dia == 7:
            print("hoje é sabado ihuuuu")

        else:
            print("esse número não é válido, insira um correto por favor!")

    except ValueError:
        print("esse número não é válido, insira um correto por favor!")