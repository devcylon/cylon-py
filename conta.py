menu ="""
 --------Menu--------
 1 - Saque
 2 - Deposito
 3 - Extrato
 4 - Sair
---------------------
"""
saldo_inicial= 1000
saldo = saldo_inicial
limite = 500
extrato =""
messagem=""
numero_saques = 0
LIMITE_SAQUES = 3

messagem += "messagem:".center(26)+"\n"
messagem += "--------------------------"
while True:
    opcao = input(menu)
    if opcao == "1":
        valor = int(input("Digite o valor de saque"))
        if valor < 0:
            print(messagem)
            print("Digite um valor inteiro e \npositivo.")
        elif valor > saldo:
            print(messagem)
            print("Saldo insuficiente".center(26))
        elif valor > limite:
            print(messagem)
            print("O valor passa do limite de \nsaque por operação, limite\n por saque é 500 reais.")
        elif numero_saques == LIMITE_SAQUES:
            print(messagem)
            print("Número de saque excedido \npor dia.".center(26))
        else:
                saldo = saldo - valor
                numero_saques +=1
                extrato+= f"saque de:    R${valor:.2f}\n".replace(".",",")

    elif opcao == "2" :
        valor = int(input("Digite o valor do deposito"))
        if valor < 0:
            print(messagem)
            print("Digite um valor positivo".center(26))
        else:
            saldo = saldo + valor
            extrato+= f"Deposito de: R${valor:.2f}\n".replace(".",",")
    elif opcao == "3":
        print(f"Saldo anterior R${saldo_inicial:.2f}")
        print("Extrato do dia".center(24))
        print("------------------------")
        if not extrato:
            print("sem movimentação no dia")
        print(extrato)
        print("------------------------")
        print(f"Saldo atual:  R${saldo:.2f}".center(20))
    elif opcao == "4":
        break
    else:
        print(messagem)
        print("Digite uma opção valida.".center(26))

    