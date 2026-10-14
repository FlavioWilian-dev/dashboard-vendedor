from app.database.shalon import obter_conexao as conexao_shalon
from app.database.veracci import obter_conexao as conexao_veracci


def testar_banco(nome, funcao_conexao):
    conexao = None

    try:
        conexao = funcao_conexao()

        cursor = conexao.cursor()
        cursor.execute("SELECT DB_NAME()")

        banco = cursor.fetchone()[0]

        print(f"[OK] {nome}: conectado ao banco {banco}")

    except Exception as erro:
        print(f"[ERRO] {nome}: {erro}")

    finally:
        if conexao:
            conexao.close()


if __name__ == "__main__":
    testar_banco("SHALON", conexao_shalon)
    testar_banco("VERACCI", conexao_veracci)