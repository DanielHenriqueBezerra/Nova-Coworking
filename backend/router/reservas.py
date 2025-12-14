from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta, time

from database import SessaoBanco
from models.reservas import Reserva
from models.usuarios import Usuario
from models.salas import Sala
from schemas.reserva import ReservaCreate

router = APIRouter(
    prefix="/reservas",
    tags=["Reservas"]
)

def get_db():
    db = SessaoBanco()
    try:
        yield db
    finally:
        db.close()


# ===============================
# CRIAR RESERVA
# ===============================
@router.post("/")
def criar_reserva(
    dados: ReservaCreate,
    db: Session = Depends(get_db)
):
    # 🔎 Usuário
    usuario = db.query(Usuario).filter(Usuario.id == dados.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")

    # 🔎 Sala
    sala = db.query(Sala).filter(Sala.id == dados.sala_id).first()
    if not sala:
        raise HTTPException(status_code=400, detail="Sala não encontrada")

    inicio = dados.data_reserva

    # ⏱️ Extrair duração do status (ex: "5h")
    try:
        duracao_horas = int(dados.status.replace("h", ""))
    except:
        raise HTTPException(
            status_code=400,
            detail="Duração inválida"
        )

    if duracao_horas < 2:
        raise HTTPException(
            status_code=400,
            detail="Reserva mínima de 2 horas"
        )

    fim = inicio + timedelta(hours=duracao_horas)

    # ⏰ Limite de horário
    if inicio.time() < time(8, 0) or fim.time() > time(22, 0):
        raise HTTPException(
            status_code=400,
            detail="Reservas permitidas apenas entre 08:00 e 22:00"
        )

    # 🔁 Verificar conflitos reais
    reservas_existentes = db.query(Reserva).filter(
        Reserva.sala_id == dados.sala_id
    ).all()

    for r in reservas_existentes:
        try:
            duracao_existente = int(r.status.replace("h", ""))
        except:
            duracao_existente = 2  # fallback seguro

        existente_inicio = r.data_reserva
        existente_fim = existente_inicio + timedelta(hours=duracao_existente)

        # 🔴 Conflito de intervalo
        if inicio < existente_fim and fim > existente_inicio:
            raise HTTPException(
                status_code=400,
                detail="Conflito de horário com outra reserva"
            )

    # ✅ Criar reserva
    nova_reserva = Reserva(
        usuario_id=dados.usuario_id,
        sala_id=dados.sala_id,
        data_reserva=inicio,
        status=f"{duracao_horas}h",
        observacao=dados.observacao
    )

    db.add(nova_reserva)
    db.commit()
    db.refresh(nova_reserva)

    return nova_reserva


# ===============================
# LISTAR RESERVAS
# ===============================
@router.get("/")
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(Reserva).order_by(Reserva.data_reserva).all()


# ===============================
# EXCLUIR RESERVA
# ===============================
@router.delete("/{reserva_id}")
def excluir_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()

    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    db.delete(reserva)
    db.commit()

    return {"message": "Reserva excluída com sucesso"}
