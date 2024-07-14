import textwrap

def menu ():
    menu = """\n
        ##########Seja Bem Vindo###########
        ----------Selecione a operação:
        [a]\tDepositar
        [b]\tSacar
        [c]\tExtrato
        [d]\tSair
        """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
         saldo += valor
         extrato += f" Depósito: R$ {valor} \n"

         print(f"Foi adicionado em sua conta R$ {valor:.2f}, Obrigado!")
    else:
        print(f"Desculpa a operação falhou!.\n O Valor não pode ser negativo")
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUE):
     
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
        elif valor > 0:

            saldo -= valor
            limite -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor}\n"

            print(f"O seu saldo actual é de R$ {saldo}\n E o seu Limite de Saque R$ {limite}!")

        return saldo, extrato

def exibir_extrato( saldo, /,*, extrato):
      print("\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("==========================================")
        
def outra_operacao(escolha):
     rel = """\n
            ##########Deseja Realizar outra operação?###########

            [1]\tPara realizar outra operação
            [0]\tPara sair do sistema
            """
     return escolha

def main():
     
    saldo = 0
    extrato = """"""
    limite= 500
    numero_saques = 0
    LIMITE_SAQUE = 3

    while True:
        opcao = menu()

        if opcao == "a":

            valor = float(input("Digite o valor a depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)

            
        elif opcao == "b":
            valor = float(input("Digite o valor que pretende sacar: "))
            saldo, extrato =sacar(
                 saldo = saldo,
                 valor = valor,
                 extrato = extrato,
                 limite = limite,
                 numero_saques = numero_saques,
                 LIMITE_SAQUE = LIMITE_SAQUE
            )
        

        
        elif opcao == "c":
            return exibir_extrato(saldo, extrato=extrato)

        elif opcao == "d":
            print("Obrigado pela preferencia")
            break

        else:
            print("Entrada Invalida! Tente novamente")

        

main()
        