import mariadb

def show_error_maria_db(error: Exception) -> str:
    if isinstance(error, mariadb.IntegrityError):
        return ("Violação de integridade: já existe um registro "
                "com esses dados (SKU e Nome devem ser únicos).")

    elif isinstance(error, mariadb.OperationalError):
        return "Erro de operação no banco. Verifique conexão, tabelas e permissões."

    elif isinstance(error, mariadb.ProgrammingError):
        return "Erro de programação SQL. Verifique a consulta e os parâmetros passados."

    elif isinstance(error, mariadb.InterfaceError):
        return "Erro na interface com o banco. Verifique instalação do driver ou a conexão."

    elif isinstance(error, mariadb.DatabaseError):
        return "Erro no banco de dados. Consulte os logs para mais detalhes."

    return "Ocorreu um erro inesperado."

__all__ = ["show_error_maria_db"]