from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão com o banco do Supabase (PostgreSQL)
DATABASE_URL = (
    "postgresql://postgres:Asrrael88495474@db.sgeleowvmxankfsfxhkl.supabase.co:5432/postgres"
)

# Cria o engine (conexão com o banco)
engine = create_engine(DATABASE_URL)

# Cria a sessão de acesso ao banco
SessaoBanco = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para os modelos
Base = declarative_base()
