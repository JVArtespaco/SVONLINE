from src.database.repositories.package_repository import PackageRepository
from typing import Any


def _just_number_and_comma(value: str) -> bool:
    return all(char.isdigit() or char == "," for char in value)


def _basic_valid_format(value: str) -> bool:
    if value == "":
        return True
    if value[0] == ",":
        return False
    if value.count(",") > 1:
        return False
    return True


def _format_to_two_decimal_places(value: str) -> str:
    if value == "":
        return ""

    if "," not in value:
        return value + ",00"

    part_int, part_dec = value.split(",", 1)
    part_dec = (part_dec + "00")[:2]
    return part_int + "," + part_dec


def validate_currency(value: str) -> tuple[bool, str]:
    """Valida e retorna (True/False, valor_formatado)."""

    if not _just_number_and_comma(value):
        return False, value

    if not _basic_valid_format(value):
        return False, value

    return True, _format_to_two_decimal_places(value)


def validate_digits(new_value: str) -> bool:
    valid, _ = validate_currency(new_value)
    return valid


def _valid_value(valid) -> bool | None:
    """Retorna True se o valor deve entrar no WHERE."""
    return valid not in ("", None)


def verify_fields(values) -> int:
    tot = 0
    for value in list(values.values()):
        if value == "":
            tot += 1
    return tot


def validate_select(var) -> bool:
    if var:
        if var.get() == "Selecionar":
            return False
        else:
            return True
    else:
        return True


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


__all__ = ["validate_currency", "validate_digits", "validate_select",
           "verify_box", "extract_valid_filters", "verify_fields"]