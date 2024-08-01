def solicita_temperatura():
    while True:
        try:
            celcius = float(input('Informe a temperatura em celcius: '))
            return celcius
        except ValueError:
            print ('Informe uma temperatura em celcius: ')
def tranformar_em_f_ou_k():
    while True:
        try:
            transformar = float(input("1 para fahrenheit ou 2 para kelvin: "))
            if transformar in (1,2):
                return transformar
            else:
                print("escolha f/k")
        except ValueError:
            print("digite f ou k")

def converte_celcius_em_fahrenheit(celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit
def converte_celcius_em_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

temperatura = solicita_temperatura()
opcao = tranformar_em_f_ou_k()
if opcao == 1:
    print(converte_celcius_em_fahrenheit(temperatura))
elif opcao == 2:
    print(converte_celcius_em_kelvin(temperatura))