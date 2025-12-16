opcao = -1

while opcao !=0:
    opcao = int(input("[1] Efetuar Saque \n[2] Verificar Extrato \n[0] Sair \nDigite a opção desejada:"))

    if opcao == 1:
        print("Aguarde enquanto efetuamos o seu SAQUE!! $$")
        print("")
    elif opcao == 2:
        print("Extrato Bancário:")
        print("20/12/2025 - Saída R$200,00")
        print("21/12/2025 - Saída R$300,00")
        print("")
else: #opcional
    print("Finalizando...")
    print("Obrigado por utilizar nosso caco de sistema")