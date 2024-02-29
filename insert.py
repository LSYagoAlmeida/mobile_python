from controller.User import inserir_usuario, visualizar_usuarios


# if __name__ == "__main__":
#     nome_usuario = "yago"
#     senha = "yago"

#     sucesso = inserir_usuario(nome_usuario, senha)

#     if sucesso:
#         print("Usuário inserido com sucesso!")
#     else:
#         print("Falha ao inserir usuário.")



if __name__ == "__main__":
    usuarios = visualizar_usuarios()

    for usuario in usuarios:
        print(f"ID: {usuario['id']}")
        print(f"Nome de usuário: {usuario['nome_usuario']}")
        print(f"Senha: {usuario['senha']}")
        print("---")

