deposito = []
saque = []
saldo = 0
saque_menu = 0


def menu():
    print(
        """
    ====== MENU ======

       [1] Depósito
       [2] Saque
       [3] Extrato
       [0] Sair

    ==================
    """
    )


while True:

    # Exibe o menu toda vez que termina uma operação
    menu()

    try:
        opcao_menu = int(input("Opção: "))

        if opcao_menu == 1:
            print(
                "\n========= DEPÓSITO =========\nInforme o valor de depósito\n============================"
            )
            # Adiciona o valor digitado para a última posição da lista
            deposito.append(float(input("R$ ")))

            if deposito[-1] < 0:
                print("Valor de depósito não pode ser negativo.")
                # Remove o valor de depósito informado para que não apareça no extrato
                deposito.pop()
                continue

            # [-1] indica que deve ser utilizada a última posição da lista
            saldo = saldo + deposito[-1]

        elif opcao_menu == 2:
            print(
                "\n========= SAQUE =========\nInforme o valor de saque\n========================="
            )
            print(f"Saldo Atual: R$ {saldo}\n=========================")

            if saque_menu < 3:
                saque.append(float(input("R$ ")))

                if saque[-1] < 0:
                    print("Valor de saque não pode ser negativo.")
                    saque.pop()
                    continue

                if saldo < saque[-1]:
                    print(
                        "Você não possui saldo suficiente para realizar a operação."
                    )
                    # Remove o valor de saque informado para que não apareça no extrato
                    saque.pop()
                else:
                    if saque[-1] <= 500:
                        saldo = saldo - saque[-1]
                        saque_menu += 1
                    else:
                        print("O limite máximo para saque é de R$ 500.00")
                        # Remove o valor de saque informado para que não apareça no extrato
                        saque.pop()
            else:
                print("Você atingiu o limite máximo de 3 saques por dia.")

        elif opcao_menu == 3:
            print("\n======== EXTRATO ========")
            # Irá varrer a lista baseada no seu tamanho (número de itens)
            for i in range(len(deposito)):
                print(f"Depósito {i+1}: R$ {deposito[i]:.2f}")
            for i in range(len(saque)):
                print(f"Saque {i+1}: R$ {saque[i]:.2f}")
            print(f"-------------------------\nSaldo Atual: R$ {saldo:.2f}")

        elif opcao_menu == 0:
            break

    except ValueError:
        print("Valor digitado é inválido.")
