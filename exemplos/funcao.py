from datetime import datetime


def menu_calculadora():
    print("menu calculadora")
    print("1- somar")
    print("2- multiplicar")
    print("3- dividir")
    print("4-subtrair")



def ola_nome(nome):
    print("ola", nome)


def calcula_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade
print("a sua idade é", calcula_idade(2008), "anos")

 # exibir_idade = calcula_idade(2008)
 while True:
     try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        if ano_nascimento > datetime.now().year:
            print("digite um ano valido")
        else:
            return ano_nascimento
    except ValueError:
        print("Digite somente numeros")
        exibir_idade = calcula_idade(ano_nascimento)













 # ola_nome("Bruno")


 # menu_calculadora()