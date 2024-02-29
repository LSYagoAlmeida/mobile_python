from sqlalchemy import create_engine, Column, Integer, String, insert
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome_usuario = Column(String)
    senha = Column(String)

engine = create_engine("sqlite:///usuarios.db")
Base.metadata.create_all(engine)


def inserir_usuario(nome_usuario, senha):
    """
    Função para inserir um novo usuário no banco de dados.

    Args:
        nome_usuario (str): Nome de usuário do novo usuário.
        senha (str): Senha do novo usuário.

    Returns:
        bool: True se o usuário for inserido com sucesso, False caso contrário.
    """

    engine = create_engine("sqlite:///usuarios.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    usuario = Usuario(nome_usuario=nome_usuario, senha=senha)
    try:
        session.add(usuario)
        session.commit()
        return True
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
        session.rollback()
        return False
    finally:
        session.close()

def visualizar_usuarios():
    """
    Função para visualizar todos os usuários no banco de dados.

    Returns:
        list: Lista de dicionários com os dados dos usuários.
    """

    

    engine = create_engine("sqlite:///usuarios.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    usuarios = session.query(Usuario).all()
    session.close()

    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append({
            "id": usuario.id,
            "nome_usuario": usuario.nome_usuario,
            "senha": usuario.senha,
        })

    return lista_usuarios

def VerificarLoginESenha(nome_usuario,senha):
    nome   = nome_usuario
    senha_ = senha 
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(Usuario).filter_by(nome_usuario=nome, senha=senha_).first()
     