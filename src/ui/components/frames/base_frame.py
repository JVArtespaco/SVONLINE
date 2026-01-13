from __future__ import annotations
from customtkinter import CTkFrame, CTkLabel
from typing import TYPE_CHECKING
from src.core.exceptions import EmptyValueError, NoneError
from src.ui.utils import apply_recursive, ACTIONS
from src.core.enums import Font, Colors


if TYPE_CHECKING:
    from src.core.protocols.ctk_widgets import CTkBase


class BaseFrame(CTkFrame):
    def __init__(self, parent: CTkBase, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent: CTkBase = parent
        self._old_pack_info: dict | None = None
        self._old_grid_info: dict | None = None

    def _set_title(self, value: str) -> None:
        if not value:
            raise EmptyValueError("O título nao pode ser uma string vazia")
        else:
            self._title: CTkLabel = CTkLabel(self, text=value, fg_color=Colors.WHITE.value,
                                             font=(Font.ARIAL.value, 20, Font.BOLD.value))
            self._title.pack(padx=10)
            self._title.lift()

    def pack(self, **kwargs) -> None:
        """Intercepta o .pack() do CTk e guarda os argumentos."""
        self._old_pack_info = kwargs.copy()  # salva só kwargs
        return super().pack(**kwargs)

    def get_old_pack_info(self) -> dict | None:
        return self._old_pack_info

    def restore_pack(self) -> None:
        """Recoloca o widget exatamente como estava antes."""
        if self._old_pack_info is None:
            raise NoneError("O restore_pack só pode ser usado depois de o pack ter sido chamado.")

        super().pack(**self._old_pack_info)

    def grid(self, **kwargs) -> None:
        """Intercepta e salva o último grid usado."""
        self._old_grid_info = kwargs.copy()
        return super().grid(**kwargs)

    def get_old_grid_info(self) -> dict | None:
        return self._old_grid_info

    def restore_grid(self) -> None:
        if self._old_grid_info is None:
            raise NoneError("O restore_grid so pode ser usado depois de o pack ter sido chamado")

        super().grid(**self._old_grid_info)

    def reset(self) -> None:
        apply_recursive(self, ACTIONS)