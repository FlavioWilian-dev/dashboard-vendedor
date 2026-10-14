from app.database.shalon import obter_conexao as obter_conexao_shalon
from app.database.veracci import obter_conexao as obter_conexao_veracci
from app.queries.usuario import SQL_BUSCAR_USUARIO
from app.utils.password import validar_senha


def buscar_usuario(conexao, login: str):
    cursor = conexao.cursor()

    cursor.execute(SQL_BUSCAR_USUARIO, (login,))

    usuario = cursor.fetchone()

    cursor.close()

    return usuario


def autenticar_usuario(login: str, senha: str):
    conexao_shalon = None
    conexao_veracci = None

    try:
        conexao_shalon = obter_conexao_shalon()
        conexao_veracci = obter_conexao_veracci()

        usuario_shalon = buscar_usuario(
            conexao_shalon,
            login
        )

        usuario_veracci = buscar_usuario(
            conexao_veracci,
            login
        )

        if not usuario_shalon and not usuario_veracci:
            return None

        resultado = {
            "usuario": login,
            "shalon": None,
            "veracci": None
        }

        if usuario_shalon:
            if not validar_senha(senha, usuario_shalon.SENHAMD5):
                return None

            resultado["shalon"] = {
                "codigoFuncionario": usuario_shalon.CODIGOFUNCIONARIO.strip()
            }

        if usuario_veracci:
            if not validar_senha(senha, usuario_veracci.SENHAMD5):
                return None

            resultado["veracci"] = {
                "codigoFuncionario": usuario_veracci.CODIGOFUNCIONARIO.strip()
            }

        return resultado

    finally:
        if conexao_shalon:
            conexao_shalon.close()

        if conexao_veracci:
            conexao_veracci.close()