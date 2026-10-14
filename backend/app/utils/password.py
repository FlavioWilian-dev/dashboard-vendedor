import hashlib


def gerar_md5(senha: str) -> str:
    return hashlib.md5(
        senha.encode("utf-8")
    ).hexdigest().upper()


def validar_senha(senha: str, senha_md5: str) -> bool:
    if not senha_md5:
        return False

    senha_digitada_md5 = gerar_md5(senha)

    return senha_digitada_md5 == senha_md5.upper()