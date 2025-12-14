from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessaoBanco
from models.salas import Sala

router = APIRouter(
    prefix="/salas",
    tags=["Salas"]
)
def get_db():
    db = SessaoBanco()
    try:
        yield db
    finally:
        db.close()
@router.get("/")
def listar_salas(db: Session = Depends(get_db)):
    salas = db.query(Sala).all()
    return salas

@router.post("/")
def criar_sala(
    nome: str,
    capacidade: int,
    recursos: str,
    db: Session = Depends(get_db)
):
    sala = Sala(
        nome=nome,
        capacidade=capacidade,
        recursos=recursos
    )

    db.add(sala)
    db.commit()
    db.refresh(sala)

    return sala