from src.database.repositories.package_repository import PackageRepository
from typing import Any


def _valid_value(valid) -> bool | None:
    """Retorna True se o valor deve entrar no WHERE."""
    return valid not in ("", None)


def _return_box(value: str) -> str:
    result = PackageRepository().select_package_by_name(value)
    if result:
        value = result[0][0]
        return value
    else:
        return ""


def verify_box(key: str, value: str) -> str:
    if key == "embalagem":
        value = _return_box(value)
        return value
    else:
        return value


def extract_valid_filters(data: dict) -> dict[Any, Any]:
    """Filtra apenas os valores válidos e retorna um dicionário."""
    return {column: value for column, value in data.items() if _valid_value(value)}


__all__ = ["verify_box", "extract_valid_filters"]