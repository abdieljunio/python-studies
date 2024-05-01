def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"deposito: R${valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("ERRO! Valor Inválido.")
    
    return saldo , extrato

def sacar(saldo, valor, limite, extrato, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("ERRO! Saldo Insuficiente.")
    elif excedeu_limite:
        print("ERRO! Valor acima do limite permitido.")
    elif excedeu_saques:
        print("ERRO! Limite de saques foi excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação Falhou")

    return saldo , extrato, numero_saques

def imprimir_extrato(saldo, /, *, extrato):
    print("=============== EXTRATO ==============")
    print("Não foram realizadas operações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("======================================")
    return extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (APENAS NÚMEROS): ")
    usuario = filtrar(cpf, usuarios)

    if usuario:
        print("Este CPF já está cadastrado!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Insira o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "CPF": cpf, "endereço": endereco})
    print("Cadastro feito com sucesso!")

def filtrar(cpf, usuarios):
    filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return filtrados[0] if filtrados else None

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar(cpf, usuarios)

    if usuario:
        print("\nConta registrada com sucesso!")
        contas.append({"agência": agencia, "numero_conta": numero_conta, "usuario": usuario})
    else:
        print("Usuário não encontrado, criação de conta encerrada!") 

def listar(contas):
    for conta in contas:
        linha = f"""\
        Agência: {conta['agência']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    menu = """
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [nu] - Cadastrar novo usuário
    [nc] - Cadastrar nova conta
    [l] - Listar contas
    [q] - Sair

    => """

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor_deposito = float(input("Informe o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)
        elif opcao == "s":
            valor_saque = float(input("Informe o valor a ser sacado: "))
            saldo, extrato, numero_saques = sacar(saldo, valor_saque, limite, extrato, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            imprimir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            criar_conta(AGENCIA, len(contas)+1, usuarios, contas)
        elif opcao == "l":
            listar(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, digite novamente a opção desejada.")

main()