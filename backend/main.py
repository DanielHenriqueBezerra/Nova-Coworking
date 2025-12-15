from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.usuarios import router as usuarios_router
from router.salas import router as salas_router
from router.reservas import router as reservas_router

app = FastAPI(title="Nova Coworking API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://nova-coworking.vercel.app",
        "http://localhost:5173",
        "httop://nova-coworking-mvki6k79c-daniel-henriques-projects-2d0b8166.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios_router)
app.include_router(salas_router)
app.include_router(reservas_router)

@app.get("/")
def health():
    return {"status": "API Nova Coworking rodando"}
