from fastapi import APIRouter, HTTPException

from app.services.dashboard_service import (
    buscar_dashboard_completo
)


router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("")
def dashboard(
    codigo_funcionario_shalon: str,
    codigo_funcionario_veracci: str
):
    try:
        return buscar_dashboard_completo(
            codigo_funcionario_shalon,
            codigo_funcionario_veracci
        )

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao carregar dashboard: {str(erro)}"
        )