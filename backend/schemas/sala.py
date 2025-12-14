from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base
from typing import Optional

class Sala(Base):
    __tablename__ = "salas"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    localizacao = Column(String(255), nullable=False)
    fotourl = Column(String(255))
    recursos = Column(String(255))
    capacidade = Column(Integer, nullable=False)

class SalaUpdate(BaseModel):
    nome: Optional[str] = None
    localizacao: Optional[str] = None
    capacidade: Optional[int] = None
    fotourl: Optional[str] = None
    recursos: Optional[str] = None

