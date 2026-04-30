lista_de_usuarios = ["vanessa", "carla"]
senha_do_usuario = ["van123", "c4rly"]

usuario = input("Digite seu usuario...\n").index
senha = input("Digite sua senha\n").index

index_usuario = lista_de_usuarios.index(usuario)
index_senha = senha_do_usuario.index(senha)

if index_usuario == index_senha:
    print("login bem sucedido!!!")
else:
    print("seu usuario ou senha está incorreto")
