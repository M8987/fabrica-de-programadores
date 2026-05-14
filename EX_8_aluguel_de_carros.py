dias = int(input("Por quantos dias o carro foi alugado: "))
km = float(input("Quantos km o carro rodou: "))

preco = (dias * 60) + (km * 0.15)

print(f"Você andou {km}km por {dias} dias, então o preço a pagar é R${preco:.2f}.")