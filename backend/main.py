from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from router.usuarios import router as usuarios_router
from router.salas import router as salas_router
from router.reservas import router as reservas_router

app = FastAPI(
    title="Nova Coworking API",
    description="API para gestão de usuários, salas e reservas",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://nova-coworking.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(usuarios_router, prefix="/usuarios", tags=["Usuários"])
app.include_router(salas_router, prefix="/salas", tags=["Salas"])
app.include_router(reservas_router, prefix="/reservas", tags=["Reservas"])


@app.on_event("startup")
def on_startup():
    """
    Apenas garante que os models estão registrados.
    NÃO cria tabelas automaticamente em produção.
    """
    pass


@app.get("/", tags=["Healthcheck"])
def healthcheck():
    return {
        "status": "online",
        "service": "Nova Coworking API"
    }
