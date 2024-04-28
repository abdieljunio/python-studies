menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - sair
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor =float(input("Insira o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("ERRO!!! Valor inválido.")


    elif opcao == "s":
        valor = float(input("Insira o valor a ser sacado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("ERRO! Saldo suficiente.")

        elif excedeu_limite:
            print("ERRO! Valor acima do limite permitido.")
        
        elif excedeu_saques:
            print("ERRO! Limite de sauques foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou")

    elif opcao == "e":
        print("=============== EXTRATO ==============")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\n Saldo R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, digite novamente a opção desejada.")
