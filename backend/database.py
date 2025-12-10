from sqlalchemy import create_engine  # Importa o mecanismo de conexão com o banco
from sqlalchemy.ext.declarative import declarative_base  # Base para criar os modelos
from sqlalchemy.orm import sessionmaker  # Cria sessões para interagir com o banco

# Configuração da URL de conexão com Neon
SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_uMbo1EsCp5NL@ep-spring-moon-acanqskn-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
# EXPLICAÇÃO:
# postgresql:// → driver do PostgreSQL
# USUARIO → usuário do Neon
# SENHA → senha do Neon
# HOST → host fornecido pelo Neon
# PORT → porta do Neon (geralmente 5432)
# gestao_salas → nome do banco de dados

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal → objeto que cria sessões para ler e escrever dados

Base = declarative_base()
# Base → classe base para todos os modelos (tabelas)
# Cria sessões → para executar operações no banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)