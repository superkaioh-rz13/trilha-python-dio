def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("retire sua grana")

    print("Obrigado por utilizar nosso sistema")

sacar(100)

def depositar(valor):
    saldo = 500

    if valor > 0:
        saldo += valor
        print("Valor depositado!")
        print("Seu novo saldo é:", saldo)

    print("Obrigado por utilizar nosso sistema")

depositar(300)