from __future__ import annotations
from customtkinter import CTkFrame, CTkButton

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.ui.screens.main_screen.main_screen import MainScreen
    from src.ui.frames import BaseWorkAreaFrame

class WorkArea(CTkFrame):
    def __init__(self, parent: MainScreen, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(corner_radius=0)
        self.parent: MainScreen = parent
        self.close_btn: None | CTkButton = None
        self.current_frame: BaseWorkAreaFrame | None = None

    def clear_main(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()

    def create_close_button(self, callback) -> None:
        self.close_btn = CTkButton(
            self, text="✕", command=lambda: self._close_area(callback), fg_color="red", width=10,
            font=("Arial", 8, "bold"), height=10)

        self.close_btn.place(relx=1.0, x=-3, y=3, anchor="ne")

    def _close_area(self, callback) -> None:
        """
        Limpa a área principal e chama callback, se existir.
        """
        self.clear_main()

        if callable(callback):
            callback()

    def add_frame(self, frame: BaseWorkAreaFrame):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame
        self.current_frame.pack()