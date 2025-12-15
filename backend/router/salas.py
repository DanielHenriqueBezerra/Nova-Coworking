from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.salas import Sala

router = APIRouter(prefix="/salas", tags=["Salas"])

@router.get("/")
def listar_salas(db: Session = Depends(get_db)):
    return db.query(Sala).all()

@router.post("/")
def criar_sala(nome: str, capacidade: int, recursos: str, db: Session = Depends(get_db)):
    sala = Sala(nome=nome, capacidade=capacidade, recursos=recursos)
    db.add(sala)
    db.commit()
    db.refresh(sala)
    return sala
