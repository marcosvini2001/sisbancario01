menu =  """"

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
num_saq = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor >:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else: 
            print("Valor informado invalido.")

    elif opcao == "2":
        valor = float(input("Informe o valor para sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor >limite
        excedeu_saques = num_saq >= LIMITE_SAQUES 

        if excedeu_saldo:
            print("Você não tem saldo sufuciente.")

        elif excedeu_limite:
            print("Seu saldo de saque foi excedido.")   

        elif excedeu_saques: 
            print("Seu número máximo de saque foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"  
            num_saq += 1

        else:
            print("Operação falhou!")

    elif opcao == "3":
        print("\n========================EXTRATO====================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSAldo: R$ {saldo:.2f}")
        print("======================================================")
    
    elif opcao == "4":
        break

    else:
        print("Operação inválida! selecione uma operação valida.")




















