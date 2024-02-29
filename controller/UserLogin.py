from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from controller.User import *

app = Flask(__name__)

# Configuração do JWT
app.config["JWT_SECRET_KEY"] = "uma-chave-secreta"  # Altere para uma chave segura
jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nome_usuario = data["nome_usuario"]
    senha = data["senha"]
    
    usuario = VerificarLoginESenha(nome_usuario,senha)

    if usuario is None:
        return jsonify({"erro": "Usuário ou senha inválidos"}), 401

    token = create_access_token(identity=usuario.nome_usuario)
    return jsonify({"token": token}), 200

@app.route("/teste", methods=["GET"])

@jwt_required()
def teste():
    return jsonify({"mensagem": "Você está autenticado!"}), 200

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)
