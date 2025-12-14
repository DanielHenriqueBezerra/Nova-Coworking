from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base  # Importa a Base do SQLAlchemy

class Usuario(Base):
    __tablename__ = "usuarios"  # Nome da tabela no banco

    id = Column(Integer, primary_key=True, index=True)  # ID auto increment
    nome = Column(String(100), nullable=False)          # Nome obrigatório
    email = Column(String(100), unique=True, nullable=False)  # Email único
    senha = Column(String(255), nullable=False)        # Senha
    data_cadastro = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")  # Data cadastro
