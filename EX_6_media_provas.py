print("| ______________________________ |")
print("| SISTEMA DE PROVAS")
print("| ______________________________ |")

nome = input("| Nome do aluno: ")
nota1 = float(input("| Nota da primeira prova: "))
nota2 = float(input("| Nota da segunda prova: "))
nota3 = float(input("| Nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3

print("| ______________________________ |")
print(f"| Aluno: {nome}")
print(f"| Média: {media:.2f}")

if media >= 7:
    print("| Aluno aprovado")
else:
    print("| Aluno reprovado")

print("| ______________________________ |")