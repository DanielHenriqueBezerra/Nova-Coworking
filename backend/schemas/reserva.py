from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ReservaCreate(BaseModel):
    usuario_id: int
    sala_id: int
    data_reserva: datetime
    status: Optional[str] = None
    observacao: Optional[str] = None

    class Config:
        from_attributes = True


class ReservaUpdate(BaseModel):
    data_reserva: Optional[datetime] = None
    status: Optional[str] = None
    observacao: Optional[str] = None