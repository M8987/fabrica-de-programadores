contador = 0
while contador <19:
    contador = contador +1
    arquivo = open("arquiuvo2.txt", "a", enconding="utf-8")
    nome = input("digite um nome: \n")
    arquivo.write(f"\n{nome}\n")


    arquivo.close()
print("\n-"+20,"\narquivo criado com sucesso\n","-"+20)