from customtkinter import CTkFrame
from src.ui.utils import (apply_recursive,
                          ACTIONS,
                          change_edges_color,
                          )
from src.core.utils import validate_select, verify_fields
from abc import abstractmethod, ABC
from src.ui.components.top_level import CTkAlert
from src.core.validators import FormValidator
from src.core.exceptions import ValidateError
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customtkinter import StringVar


class FormArea(CTkFrame, ABC):
    def __init__(self, parent: CTkFrame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._font12_A = ("Arial", 13)
        self.all_select_vars: list[StringVar] = []
        self._var: StringVar | None = None

    def clear_fields(self) -> None:
        apply_recursive(self, ACTIONS)

    def change_edges(self) -> None:
        for widget in self.winfo_children():
            change_edges_color(widget)

    @abstractmethod
    def return_fields_values(self) -> dict[str, str]:
        pass

    def validate_all_select(self) -> bool:
        if self.all_select_vars:
            for c in self.all_select_vars:
                if not FormValidator.validate_select(c.get()):
                    return False
            return True
        return False

    def validate_and_change_border_colors(self) -> bool:
        try:
            if not FormValidator(self.return_fields_values()).validate_fields(self.validate_all_select):
                self.change_edges()
                return True
            else:
                raise
        except ValidateError:
            CTkAlert(self, str(ValidateError))
            return False