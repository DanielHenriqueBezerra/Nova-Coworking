from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from database import Base


class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    sala_id = Column(Integer, ForeignKey("salas.id"), nullable=False)
    data_reserva = Column(TIMESTAMP, nullable=False)
    status = Column(String(50))
    observacao = Column(String(255))
