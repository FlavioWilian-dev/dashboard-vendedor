from pathlib import Path
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routes.auth import router as auth_router
from app.routes.dashboard import router as dashboard_router


# =========================================
# CONFIGURAÇÃO
# =========================================

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parents[2]

FRONTEND_DIR = BASE_DIR / "frontend"


# =========================================
# FASTAPI
# =========================================

app = FastAPI(
    title="Dashboard Vendedor",
    version="1.0.0"
)


# =========================================
# CORS
# =========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================
# API
# =========================================

app.include_router(auth_router)
app.include_router(dashboard_router)


# =========================================
# ARQUIVOS DO FRONTEND
# =========================================

app.mount(
    "/frontend",
    StaticFiles(directory=FRONTEND_DIR),
    name="frontend"
)


# =========================================
# LOGIN
# =========================================

@app.get("/")
def pagina_login():
    return FileResponse(
        FRONTEND_DIR / "src/pages/Login/Login.html"
    )


# =========================================
# DASHBOARD
# =========================================

@app.get("/dashboard")
def pagina_dashboard():
    return FileResponse(
        FRONTEND_DIR / "src/pages/Dashboard/Dashboard.html"
    )


# =========================================
# HEALTH
# =========================================

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "sistema": "Dashboard Vendedor"
    }