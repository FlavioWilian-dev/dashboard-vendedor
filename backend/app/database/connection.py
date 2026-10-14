import pyodbc

from app.config.settings import settings


def criar_conexao(database: str):
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={settings.db_server},{settings.db_port};"
        f"DATABASE={database};"
        f"UID={settings.db_user};"
        f"PWD={settings.db_password};"
        "TrustServerCertificate=yes;"
    )

    return pyodbc.connect(connection_string)