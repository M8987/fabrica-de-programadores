minha_garagem = ["bmw", "mercedes-bens", "audi", "aston martin"]
preco = [35.000, 40.000, 20.000, 80.000]

estoque = ["chevrolet", "fiat", "peugeot", "volkswagem", "lexus", "ferrari"]
preco_loja = [1.000, 500, 6.000, 1.99, 2.000]

loja_barato = []
loja_caro = []

for x in estoque:
    if preco[x]< 20000:
        loja_barato.append(x)
    else:
        loja_caro.append(x)

print("carros baratos:", loja_barato)
print("carros caros", loja_caro)