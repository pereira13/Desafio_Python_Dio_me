menu = """

[1] Depositar
[2] Sacar
[3] extrato
[4] Sair
=> """

saldo =  0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Deposito \n")
        valor = float(input("Insira o valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operação não realizada, valor invalido! ")

    elif opcao == "2":
        print("Saque")
        valor = float(input("Insira o valor de saque desejado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não autorizada, saldo insulficiente!")

        elif excedeu_limite:
            print("Operação nao realizada, O valor de limite diario excedido!")

        elif excedeu_saques:
            print("Operação nao realizada, limite diario de saque excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não realizada, valor invalido! ")
   
    elif opcao == "3":
        visual = " Extrato "
        print(visual.center(29, "*"))
        print("Nao foram realizada movimentações" if not extrato else extrato)
        print(f"\n saldo: R$ {saldo:.2f}")
        print(visual.center(29, "*"))
    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecionar novamente a operação desejada")


