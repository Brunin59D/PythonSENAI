media = 0

while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        if nota1 < 0 or nota2 < 0 and nota1 > 100 or nota2 > 100:
            print("por favor insira uma nota válida")
        else:
            #calcular
            media = (nota1 + nota2) / 2

            #verificar se o aluno passou de ano

        if media >= 70:
            print("Aprovado")
        elif media < 70:
            print("Reprovado")
        else:
            print("Aluno de recuperação com a média")

    except ValueError:
        print("valor invalido")