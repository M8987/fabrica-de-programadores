saldo = 1.500
opção = input("digite 1 para saque: \ndigite 2 para depositos: ")

if opção => "1":
    saque = int(("quanto deseja sacar? \n"))
    saldo = saldo - saque

    print(f"o saldo atual é: {saldo}")


    elif opção => "2"{
        deposito = int(intup("quanto deseja depositar? \n"))
        saldo = saldo + deposito
        print(f"o saldo atual é  {saldo}")

    else:
        print("opção inválida...\n\nobrigado por usar nossos serviços....")