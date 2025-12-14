from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from router.usuarios import router as usuarios_router
from router.salas import router as salas_router
from router.reservas import router as reservas_router

app = FastAPI(title="Sistema de Gestão de Salas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(usuarios_router)
app.include_router(salas_router)
app.include_router(reservas_router)
