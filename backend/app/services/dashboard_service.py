from app.database.shalon import obter_conexao as obter_conexao_shalon
from app.database.veracci import obter_conexao as obter_conexao_veracci


from app.queries.dashboard_dia import (
    SQL_PEDIDOS_FEITOS_DIA,
    SQL_ORCAMENTOS_PENDENTES_DIA,
    SQL_PEDIDOS_PENDENTES_DIA,
    SQL_CLIENTES_ATENDIDOS_DIA,
    SQL_META_DIA,
    SQL_PERCENTUAL_META_DIA,
)

from app.queries.dashboard_mes import (
    SQL_PEDIDOS_FEITOS_MES,
    SQL_ORCAMENTOS_PENDENTES_MES,
    SQL_PEDIDOS_PENDENTES_MES,
    SQL_CLIENTES_ATENDIDOS_MES,
    SQL_META_MES,
    SQL_PERCENTUAL_META_MES,
)


def executar_query(cursor, sql, codigo_funcionario):
    cursor.execute(sql, (codigo_funcionario,))
    resultado = cursor.fetchone()

    if not resultado:
        return 0

    return resultado[0] or 0


def buscar_dashboard_dia(codigo_funcionario, obter_conexao):
    conexao = None

    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()

        dados = {
            "pedidosFeitos": executar_query(
                cursor,
                SQL_PEDIDOS_FEITOS_DIA,
                codigo_funcionario
            ),

            "orcamentosPendentes": executar_query(
                cursor,
                SQL_ORCAMENTOS_PENDENTES_DIA,
                codigo_funcionario
            ),

            "pedidosPendentes": executar_query(
                cursor,
                SQL_PEDIDOS_PENDENTES_DIA,
                codigo_funcionario
            ),

            "clientesAtendidos": executar_query(
                cursor,
                SQL_CLIENTES_ATENDIDOS_DIA,
                codigo_funcionario
            ),

            "meta": executar_query(
                cursor,
                SQL_META_DIA,
                codigo_funcionario
            ),

            "percentualMeta": executar_query(
                cursor,
                SQL_PERCENTUAL_META_DIA,
                codigo_funcionario
            ),
        }

        cursor.close()

        return dados

    finally:
        if conexao:
            conexao.close()

def buscar_dashboard_mes(codigo_funcionario, obter_conexao):
    conexao = None

    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()

        dados = {
            "pedidosFeitos": executar_query(
                cursor,
                SQL_PEDIDOS_FEITOS_MES,
                codigo_funcionario
            ),

            "orcamentosPendentes": executar_query(
                cursor,
                SQL_ORCAMENTOS_PENDENTES_MES,
                codigo_funcionario
            ),

            "pedidosPendentes": executar_query(
                cursor,
                SQL_PEDIDOS_PENDENTES_MES,
                codigo_funcionario
            ),

            "clientesAtendidos": executar_query(
                cursor,
                SQL_CLIENTES_ATENDIDOS_MES,
                codigo_funcionario
            ),

            "meta": executar_query(
                cursor,
                SQL_META_MES,
                codigo_funcionario
            ),

            "percentualMeta": executar_query(
                cursor,
                SQL_PERCENTUAL_META_MES,
                codigo_funcionario
            ),
        }

        cursor.close()

        return dados

    finally:
        if conexao:
            conexao.close()

def buscar_dashboard_completo(
    codigo_funcionario_shalon,
    codigo_funcionario_veracci
):
    return {
        "shalon": {
            "dia": buscar_dashboard_dia(
                codigo_funcionario_shalon,
                obter_conexao_shalon
            ),
            "mes": buscar_dashboard_mes(
                codigo_funcionario_shalon,
                obter_conexao_shalon
            )
        },

        "veracci": {
            "dia": buscar_dashboard_dia(
                codigo_funcionario_veracci,
                obter_conexao_veracci
            ),
            "mes": buscar_dashboard_mes(
                codigo_funcionario_veracci,
                obter_conexao_veracci
            )
        }
    }