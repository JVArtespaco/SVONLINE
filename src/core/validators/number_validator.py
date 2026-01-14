class NumberValidator:
    def __init__(self, decimal_places: int = 2):
        self.decimal_places = decimal_places
        self.decimal_separator = ","

    def _just_number_and_separator(self, value: str) -> bool:
        return all(
            char.isdigit() or char == self.decimal_separator
            for char in value
        )

    def _basic_valid_format(self, value: str) -> bool:
        if value == "":
            return True

        # Não pode iniciar com vírgula
        if value[0] == self.decimal_separator:
            return False

        # Não pode ter mais de uma vírgula
        if value.count(self.decimal_separator) > 1:
            return False

        return True

    def _format_decimal_places(self, value: str) -> str:
        if value == "":
            return ""

        sep = self.decimal_separator

        if sep not in value:
            # Nenhuma parte decimal -> adiciona ",00" (ou ",000", etc)
            return value + sep + ("0" * self.decimal_places)

        integer, decimal = value.split(sep, 1)

        # Completa à direita com zeros e corta se exceder
        decimal = (decimal + "0" * self.decimal_places)[:self.decimal_places]

        return integer + sep + decimal

    def validate(self, value: str) -> tuple[bool, str]:
        if not self._just_number_and_separator(value):
            return False, value

        if not self._basic_valid_format(value):
            return False, value

        return True, self._format_decimal_places(value)

    def validate_digits(self, new_value: str) -> bool:
        valid, _ = self.validate(new_value)
        return valid
