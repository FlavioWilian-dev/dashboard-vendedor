from app.config.settings import settings
from app.database.connection import criar_conexao


def obter_conexao():
    return criar_conexao(settings.db_shalon)