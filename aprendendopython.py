menu = """
===== MENU BANCÁRIO =====
[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair
=> 
"""

saldo = 0
limite = 500
numero_saques = 0
extrato = ""
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "a":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação Falhou")
    elif opcao == "b":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou excedeu o saldo")
        elif excedeu_limite:
            print("Operação Falhou excedeu o limite")
        elif excedeu_saques:
            print("Operação Falhou limites de saque diário")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação Falhou! O valor é invalido")
    elif opcao == "c":

        print("\n ==================== EXTRATO ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=============================")
    elif opcao == "d":
        break
    else:
        print("Opção Inválida, por favor selecione novamente a operação desejada.")
