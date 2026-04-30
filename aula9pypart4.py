contador = 0
while contador <14:
    contador = contador +1
    arquivo = open("arquiuvo2.txt", "a", enconding="utf-8")
    nome = input("digite o nome da sua cidade: \n")
    arquivo.write(f"\n{nome}\n"+15)


    arquivo.close()
    print("\n-"+15,"\narquivo criado com sucesso\n","-"+15)