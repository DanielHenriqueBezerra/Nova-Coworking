from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.salas import Sala

router = APIRouter(prefix="/salas", tags=["Salas"])

@router.get("/")
def listar_salas(db: Session = Depends(get_db)):
    return db.query(Sala).order_by(Sala.nome).all()
