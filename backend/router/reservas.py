from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta, time

from database import get_db
from models.reservas import Reserva
from models.usuarios import Usuario
from models.salas import Sala
from schemas.reserva import ReservaCreate

router = APIRouter(prefix="/reservas", tags=["Reservas"])

@router.post("/")
def criar_reserva(dados: ReservaCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == dados.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")

    sala = db.query(Sala).filter(Sala.id == dados.sala_id).first()
    if not sala:
        raise HTTPException(status_code=400, detail="Sala não encontrada")

    duracao_horas = int(dados.status.replace("h", ""))
    inicio = dados.data_reserva
    fim = inicio + timedelta(hours=duracao_horas)

    if inicio.time() < time(8, 0) or fim.time() > time(22, 0):
        raise HTTPException(status_code=400, detail="Horário inválido")

    nova = Reserva(
        usuario_id=dados.usuario_id,
        sala_id=dados.sala_id,
        data_reserva=inicio,
        status=f"{duracao_horas}h",
        observacao=dados.observacao
    )

    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/")
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(Reserva).order_by(Reserva.data_reserva).all()
