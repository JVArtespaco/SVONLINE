from src.database.repositories.package_repository import PackageRepository
from .validate_utils import extract_valid_filters
from typing import Any


def _construct_condition(column, value) -> str:
    """
    Retorna a condição SQL.
    Strings → LIKE %valor%
    Outros tipos → comparação exata.
    """
    if isinstance(value, str):
        return f"{column} LIKE %s"
    return f"{column} = %s"


def _construct_where_clause(valid_filter: dict[Any, Any]) -> tuple[str, list]:
    """Monta o trecho WHERE e lista de parâmetros."""
    if not valid_filter:
        return "", []

    conditions = []
    parameters = []

    for column, value in valid_filter.items():
        conditions.append(_construct_condition(column, value))

        # Strings → usar %valor%
        if isinstance(value, str):
            parameters.append(f"%{value}%")
        else:
            parameters.append(value)

    where_sql = " WHERE " + " AND ".join(conditions)
    return where_sql, parameters


def montar_select(dados: dict[Any, Any], table: str) -> tuple[str, list]:
    """Função principal: retorna o SELECT completo + params."""
    valid_filters: dict[Any, Any] = extract_valid_filters(dados)
    where_sql, parameters = _construct_where_clause(valid_filters)

    sql = f"SELECT * FROM {table}{where_sql}"
    return sql, parameters


def check_query() -> list | bool:
    result = PackageRepository().list_all()
    if result:
        return result
    else:
        return False


__all__ = ["montar_select", "check_query"]


