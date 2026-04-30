nota1 = input("digite sua nota1")

nota2 = input(input('digite sua nota2'))

nota3 = float(input("digite sua nota3"))

média = nota1 + nota2 + nota3

print("a média do aluno é: ", média)
if média >= 7:
    print("aprovado")
elif média > 3:
    print("recuperação")
else:
    print("reprovado") 