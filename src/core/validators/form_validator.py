from typing import Callable
from src.core.exceptions import ValidateError


class FormValidator:
    def __init__(self, fields_values: dict):
        self._fields_values: dict = fields_values

    @staticmethod
    def validate_select(value: str) -> bool:
        if value:
            if value == "Selecionar":
                return False
            else:
                return True
        else:
            return True

    def _verify_fields(self) -> int:
        tot = 0
        for value in list(self._fields_values.values()):
            if value == "":
                tot += 1
        return tot

    def validate_fields(self, callback: Callable) -> bool:
        if self._verify_fields() > 0 or not callback:
            raise ValidateError("Preencha todos os Campos")
        else:
            return True