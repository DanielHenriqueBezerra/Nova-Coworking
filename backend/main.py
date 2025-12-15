from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.usuarios import router as usuarios_router
from router.salas import router as salas_router
from router.reservas import router as reservas_router

app = FastAPI(title="Nova Coworking API")

# ⚠️ CORS TEM QUE VIR ANTES DOS ROUTERS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://nova-coworking.vercel.app",
        "https://nova-coworking.onrender.com",
        "http://localhost:5173",          # desenvolvimento local
        
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS DEPOIS
app.include_router(usuarios_router)
app.include_router(salas_router)
app.include_router(reservas_router)

@app.get("/")
def health():
    return {"status": "ok"}
