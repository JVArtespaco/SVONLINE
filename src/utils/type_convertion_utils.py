#from classes.widgets.alert import CTkAlert
from typing import Any

def parse_float(value: str) -> float:
    try:
        value = float(value.replace(",", "."))
        return value
    except ValueError:
        raise ValueError("Não foi possivel converter para float")


def parse_float_alert(value, parent) -> float | bool:
    """
    Converte string para número float, aceitando ',' ou '.' como separador decimal.
    """
    try:
        return float(value.replace(",", "."))
    except ValueError:
        CTkAlert(parent, "Digite um numero flutuante válido")
        return False


def parse_int_alert(value, parent) -> int | bool:
    try:
        return int(value)
    except ValueError:
        CTkAlert(parent, "Digite um numero inteiro válido para as medidas das caixas")
        return False


def float_to_string(value) -> str | bool:
    if isinstance(value, float):
        return str(value)
    else:
        return False


def parse_int(value: Any) -> int:
    try:
        return int(value)
    except:
        raise ValueError("Não Foi Possível converter para int")


__all__ = ["parse_float",
           "parse_float_alert",
           "parse_int_alert",
           "float_to_string",
           "parse_int"]