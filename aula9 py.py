arquivo = open("arquivo.txt", "w", encoding="utf-8")


nome = input("digite seu nome: \n")
nota = int(input("digite a nota: \n"))
arquivo.write("-"+10)
arquivo.write(f"\naluno: {nome}\n")
arquivo.write(f"\nnota: {nota}\n")
arquivo.write("-"+10)