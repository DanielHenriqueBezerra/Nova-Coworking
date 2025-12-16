from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta, time

from database import get_db
from models.reservas import Reserva
from models.usuarios import Usuario
from models.salas import Sala
from schemas.reserva import ReservaCreate

router = APIRouter(prefix="/reservas", tags=["Reservas"])


def _parse_duracao_horas(status_str: str) -> int:
    
    try:
        horas = int(str(status_str).lower().replace("h", "").strip())
        if horas <= 0:
            raise ValueError()
        return horas
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Campo 'status' inválido. Use formato como '2h', '4h'."
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_reserva(dados: ReservaCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == dados.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")

    sala = db.query(Sala).filter(Sala.id == dados.sala_id).first()
    if not sala:
        raise HTTPException(status_code=400, detail="Sala não encontrada")

    duracao_horas = _parse_duracao_horas(dados.status)

    inicio = dados.data_reserva
    fim = inicio + timedelta(hours=duracao_horas)

    
    if inicio.time() < time(8, 0) or fim.time() > time(22, 0):
        raise HTTPException(status_code=400, detail="Horário inválido (permitido 08:00–22:00)")

    existentes = db.query(Reserva).filter(Reserva.sala_id == dados.sala_id).all()
    for r in existentes:
        r_dur = _parse_duracao_horas(r.status)
        r_inicio = r.data_reserva
        r_fim = r_inicio + timedelta(hours=r_dur)

        if inicio < r_fim and fim > r_inicio:
            raise HTTPException(
                status_code=409,
                detail=f"Conflito de horário: a sala já possui reserva em {r_inicio} por {r.status}."
            )

    nova = Reserva(
        usuario_id=dados.usuario_id,
        sala_id=dados.sala_id,
        data_reserva=inicio,
        status=f"{duracao_horas}h",
        observacao=(dados.observacao or "")
    )

    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


@router.get("/")
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(Reserva).order_by(Reserva.data_reserva).all()


@router.delete("/{reserva_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    db.delete(reserva)
    db.commit()
    return None
