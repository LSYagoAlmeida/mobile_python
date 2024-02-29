from flet import * 
import flet as ft
from controller.UserLogin import login

def StartLogin(page: ft.Page):
    page.title = "Tela de Login"     
    
    # Define a imagem de plano de fundo
    # background_image = ft.Image(src="https://down-br.img.susercontent.com/file/5df26f148c1510a47958e48ad7abfcd2", width=500, height=500, opacity=80, fit="cover")

    # Cria os widgets de login
    email_field = ft.TextField(label="Nome", hint_text="Digite seu nome")
    password_field = ft.TextField(label="Senha", hint_text="Digite sua senha", password=True, can_reveal_password=True)
    
    # Cria os botões
    login_button = ft.TextButton(text="Login", on_click=login_clicked(any,email_field.value, password_field.value))
    cancel_button = ft.TextButton(text="Cancelar", on_click=cancel_clicked)   

    # Define o layout da tela
    page.add( 
      ft.Container
      (
        # background_image,
        image_fit=ImageFit.COVER,
        expand=True        
      ),
      ft.Column
      (            
        [
          email_field,
          password_field,
          ft.Row
          (
            [
              login_button,
              cancel_button,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
           ),
        ],
            alignment=ft.alignment.center,
      )                
    )
    

def login_clicked(e,username, password):
    # Insira aqui o código para verificar as credenciais de login
    print("Login clicked!")  
    """
    Função para realizar o login na API.

    Args:
        username (str): Nome de usuário.
        password (str): Senha do usuário.

    Returns:
        dict: Dicionário com o token de acesso ou mensagem de erro.
    """

    # Importe as bibliotecas necessárias
    import requests

    # URL da rota de login
    url = "http://localhost:5000/login"

    # Dados da requisição
    data = {"nome_usuario": username, "senha": password}

    # Envio da requisição
    response = requests.post(url, json=data)

    # Verificação do status code
    if response.status_code == 200:
        # Retorna o token de acesso
        return response.json()["token"]
    else:
        # Retorna a mensagem de erro
        return response.json()["erro"]

# Exemplo de uso
username = "admin"
password = "senha123"

token =''
# = login(username, password)

if token:
    print(f"Token de acesso: {token}")
else:
    print("Erro ao realizar o login.")


def cancel_clicked(e):
    # Insira aqui o código para cancelar o login
    print("Cancel clicked!")


ft.app(target=StartLogin)    