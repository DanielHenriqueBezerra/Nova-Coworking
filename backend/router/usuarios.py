from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException


from database import SessaoBanco
from models.usuarios import Usuario
from schemas.usuario import UsuarioUpdate

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


def get_db():
    db = SessaoBanco()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

@router.post("/")
def criar_usuario(
    nome: str,
    email: str,
    senha: str,
    db: Session = Depends(get_db)
):
    usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)


    return usuario
@router.delete("/{usuario_id}")
def excluir_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        return {"message": "Usuário não encontrado"}

    db.delete(usuario)
    db.commit()

    return {"message": "Usuário excluído com sucesso"}

@router.put("/{usuario_id}")
def editar_usuario(
    usuario_id: int,
    dados: UsuarioUpdate,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    if dados.nome is not None:
        usuario.nome = dados.nome
    if dados.email is not None:
        usuario.email = dados.email

    db.commit()
    db.refresh(usuario)
    return usuario
