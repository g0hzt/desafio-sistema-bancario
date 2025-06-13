# Variáveis globais
saldo = 0
cadastro = {}
deposito = []
saque = []
saque_limite = 3
agencia = "0001"
extrato = ""


def menu():
    print(
        """
    ====== MENU ======

       [1] Cadastro
       [2] Contas
       [3] Depósito
       [4] Saque
       [5] Extrato
       [0] Sair

    ==================
    """
    )


def cadastrar():
    print("\n========= CADASTRO =========\n")
    cpf = int(input("CPF: "))
    cadastro[cpf] = {"nome": input("Nome: "), "cpf": cpf}

    return cadastro


def criar_conta():
    print("\n======== CRIAR CONTA ========\n")
    cpf = input("Digite o CPF do usuário: ")

    return cpf


def depositar():
    print("\n========= DEPÓSITO =========\nInforme o valor de depósito")
    print("============================")
    # Adiciona o valor digitado para a última posição da lista
    deposito.append(float(input("R$ ")))

    if deposito[-1] < 0:
        print("Valor de depósito não pode ser negativo.")
        depositar()

    return deposito


def sacar():
    print("\n========= SAQUE =========\nInforme o valor de saque")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Saldo Atual: R$ {saldo}\n~~~~~~~~~~~~~~~~~~~~~~~~~")

    if saque_limite == 0:
        print("Você atingiu o limite máximo de 3 saques por dia.")
        return 0

    saque.append(float(input("R$ ")))

    if saque[-1] < 0:
        print("Valor de saque não pode ser negativo.")
        sacar()

    elif saldo < saque[-1]:
        print("Você não possui saldo suficiente para realizar a operação.")
        sacar()

    elif saque[-1] > 500:
        print("O limite máximo para saque é de R$ 500.00")
        sacar()

    else:
        return saque


def mostrar_extrato():
    print("\n======== EXTRATO ========\n")
    print(f"{extrato}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")


while True:

    # Exibe o menu toda vez que termina uma operação
    menu()

    try:
        opcao_menu = int(input("Opção: "))

        match opcao_menu:
            case 1:
                cadastrar()
                for chave in cadastro:
                    saida_cadastro = [
                        f"Nome: {cadastro[chave]["nome"]}\nCPF: {cadastro[chave]["cpf"]}"
                    ]
                    print(", ".join(saida_cadastro))
            case 2:
                criar_conta()
            case 3:
                depositar()
                saldo += deposito[-1]
                extrato += f"Depósito: R$ {deposito[-1]:.2f}\n"
            case 4:
                sacar()
                if saque_limite > 0:
                    saldo -= saque[-1]
                    saque_limite -= 1
                    extrato += f"Saque: R$ {saque[-1]:.2f}\n"
            case 5:
                mostrar_extrato()
            case 0:
                break
            case _:
                print("Valor digitado é inválido.")

    except ValueError:
        print("Exception: Valor digitado é inválido.")
