import tkinter as tk
import customtkinter as ctk
from src.core.validators import NumberValidator


class FloatEntry(ctk.CTkEntry):

    def __init__(self, decimal_places: int, parent, *args, **kwargs):
        self.var = tk.StringVar()

        super().__init__(
            parent,
            textvariable=self.var,
            validate="key",
            *args,
            **kwargs
        )
        self.decimal_places: int = decimal_places
        # validatecommand → só valida durante digitação
        validate_command = (self.register(NumberValidator.validate_digits), "%P")
        self.configure(validatecommand=validate_command)

        # formatar ao perder foco
        self.bind("<FocusOut>", self._on_focus_out)

    # ----------------------------------------------------
    # Quando perde o foco, aplica formatação final
    # ----------------------------------------------------
    def _on_focus_out(self, event=None) -> None:
        self._apply_format()

    # ----------------------------------------------------
    # A ÚNICA função que usa self (como você pediu)
    # ----------------------------------------------------
    def _apply_format(self) -> None:
        valid, formatted = NumberValidator(self.decimal_places).validate(self.var.get())
        if valid:
            self.var.set(formatted)
            self._adjust_cursor(formatted)

    def _adjust_cursor(self, formatted) -> None:
        nova_pos = self._update_position(formatted)
        if nova_pos < 0:
            nova_pos = 0
        if nova_pos > len(formatted):
            nova_pos = len(formatted)
        self.icursor(nova_pos)

    def _update_position(self, formatted) -> int:
        pos_cursor = self.index("insert")
        diff = len(formatted) - len(self.var.get())
        nova_pos = pos_cursor + diff
        return nova_pos