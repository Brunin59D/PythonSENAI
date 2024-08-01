import datetime

nome = ""
while True:
    def saudacao():
        agora = datetime.datetime.now()
        mensagem = ""

        if (agora.hour < 12):
            mensagem = ("Bom dia")
        elif (agora.hour <= 18):
            mensagem = (f"Boa tarde")
        else:
            mensagem = (f"Boa noite", agora.hour)
        return mensagem


    nome = str(input("Qual o seu nome? "))
    tempo = datetime.datetime.now()


    def mes():
        tempo = datetime.datetime.now()
        mes = ""

        if (tempo.month ==  1):
           mes = "Janeiro"
        elif (tempo.month == 2):
            mes = "Fevereiro"
        elif (tempo.month == 3):
            mes = "Março"
        elif (tempo.month == 4):
            mes = "Abril"
        elif (tempo.month == 5):
            mes = "Maio"
        elif (tempo.month == 6):
            mes = "Junho"
        elif (tempo.month == 7):
            mes = "Julho"
        elif (tempo.month == 8):
            mes = "Agosto"
        elif (tempo.month == 9):
            mes = "Setembro"
        elif (tempo.month == 10):
            mes = "Outubro"
        elif (tempo.month == 11):
            mes = "Novembro"
        elif (tempo.month == 12):
           mes = "Dezembro"

    print(f"{saudacao()} {nome}, agora são: {tempo.hour}:{tempo.minute} e estamos no dia {tempo.day} do mês {tempo.month} no ano de {tempo.year}")