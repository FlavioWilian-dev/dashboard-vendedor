from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.auth_service import autenticar_usuario


router = APIRouter(
    prefix="/api/auth",
    tags=["Autenticação"]
)


class LoginRequest(BaseModel):
    login: str
    senha: str


@router.post("/login")
def login(dados: LoginRequest):

    resultado = autenticar_usuario(
        dados.login,
        dados.senha
    )

    if not resultado:
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha inválidos"
        )

    return resultado