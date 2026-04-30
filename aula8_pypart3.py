# crie um sistema que atraves de uma lista de nomes e lista de senha verifique se o usuario digitado esta na lista e que a senha corresponda ao index do usuario 
lista_de_usuarios = ["vanessa", "carla"]
senha_do_usuario = ["van123", "c4rly"]

usuario = input("Digite seu usuario...\n").index
senha = input("Digite sua senha\n").index

index_usuario = lista_de_usuarios.index(usuario)
index_senha = senha_do_usuario.index(senha)

if index_usuario == index_senha:
    print("seu usuario esta na lista")
else:
    print("seu usuario não esta na lista")