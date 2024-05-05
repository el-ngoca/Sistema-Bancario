menu = """
[a] - Depositar
[b] - Sacar
[c] - Extrato
[d] - Sair

 => """

escolha = """
##########Deseja Realizar outra operação?###########

[1] - Para realizar outra operação
[0] - Para sair do sistema
=>"""

saldo = 0
valor = 0
extrato = """"""
limite= 500
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "a":

        valor = float(input("Digite o valor a depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f" Depósito: R$ {valor} \n"

            print(f"Foi adicionado em sua conta R$ {valor:.2f}, Obrigado!")
        else:
            print(f"Desculpa a operação falhou!.\n O Valor não pode ser negativo")
    
    elif opcao == "b":
        valor = float(input("Digite o valor que pretende sacar: "))

        excedeu_limite = valor > limite
        excedeu_saldo = valor > saldo
        excedeu_saques = numero_saques >= LIMITE_SAQUE
        valor_negativo = valor < 0

        if excedeu_limite:
            print(f"Desculpa excedeu o limmite de levantamento diario R$ {limite}!")
        elif excedeu_saldo:
            print(f" Desculpa o seu saldo é inferior ao que pretende levantar.\n saldo R$ {saldo}!")
        elif excedeu_saques: 
            print(f"Desculpa excedeu numero de saques diarios!Limite de Saques{LIMITE_SAQUE}")
        elif valor_negativo:
            print("Não é possivel sacar valores negativos")
       

        if valor > 0:

            saldo -= valor
            limite -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor}\n"

            print(f"O seu saldo actual é de R$ {saldo}\n E o seu Limite de Saque R$ {limite}!")
    
    elif opcao == "c":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "d":
        print("Obrigado pela preferencia")
        break

    else:
        print("Entrada Invalida! Tente novamente")

    outra_operação= input(escolha)
    
    if outra_operação =="1":
        opcao
    elif outra_operação =="0":
        print("Obrigado pela preferência!")
        break


    