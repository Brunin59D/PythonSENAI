import datetime
horas = datetime.datetime.now().hour
def bom_dia_princesa():
    while True:
        try:
            name = input('Qual o nome do seu nome? ')
            if name.isalpha():
                break
            else:
                print("coloque o seu nome por favor")
        except ValueError:
            print("coloque seu nome corretamente")


    horas = datetime.datetime.now().hour

    if 0 <= horas <= 5:
        print(f"Boa madrugada {name} ")
    elif 5 <= horas <= 12:
        print(f"Bom Dia {name} ")
    elif 12 <= horas <= 19:
        print(f"Boa Tarde {name} ")
    else:
        print(f"Boa Noite {name} ")
bom_dia_princesa()