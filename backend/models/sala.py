from sqlalchemy import Column, Integer, String
from database import Base

class Sala(Base):
    __tablename__ = "salas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    localizacao = Column(String(255), nullable=False)
    fotourl = Column(String(255))
    recursos = Column(String(255))
