saldo = 0
saques_feitos = 0
limite_saques_diarios = 3
limite_saque_valor = 500
transacoes = []

while True:
    print("\nMenu:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor = float(input("Digite o valor a depositar: "))
        if valor > 0:
            saldo += valor
            transacoes.append(f'Depósito de R${valor:.2f}')
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print("Valor de depósito inválido. O valor deve ser maior que zero.")
    elif opcao == '2':
        valor = float(input("Digite o valor a sacar: "))
        if saques_feitos < limite_saques_diarios and valor <= limite_saque_valor and valor <= saldo:
            saldo -= valor
            saques_feitos += 1
            transacoes.append(f'Saque de R${valor:.2f}')
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
            print(f'Você ainda pode fazer {limite_saques_diarios - saques_feitos} saques hoje.')
        else:
            print('Operação de saque não autorizada.')
    elif opcao == '3':
        print('Extrato:')
        for transacao in transacoes:
            print(transacao)
        print(f'Saldo atual: R${saldo:.2f}')
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
