def solicita_altura():
    while True:
        try:
            altura = float(input('Digite sua altura em cm: '))
            break
        except ValueError:
            print("digite uma altura valida em cm")
    return altura


def solicita_peso():
    while True:
        try:
            peso = float(input('Digite sua peso em kg: '))
            if peso > 0:
                break

        except ValueError:
            print("digite um peso valida em kg")
    return peso


def calculo(altura, peso):
    imc = peso / (altura * altura)
    return imc
solicita_altura()
solicita_peso()

print(calculo(solicita_peso(), solicita_altura()))