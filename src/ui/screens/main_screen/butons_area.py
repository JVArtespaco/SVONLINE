from customtkinter import CTkFrame
from typing import TYPE_CHECKING
from src.core.enums import State
from .buttons_area_buttons import *

if TYPE_CHECKING:
    from src.ui.screens.main_screen.main_screen import MainScreen


class ButtonsArea(CTkFrame):
    def __init__(self, parent: MainScreen, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent: MainScreen = parent
        self.add_button = AddButton(self)
        self.add_button.grid(row=0, column=0, padx=(10, 5), pady=10)

    def enable_all_buttons(self):
        children: list = self.winfo_children()
        for child in children:
            child.state = State.ENABLE

    def diable_all_children(self):
        children: list = self.winfo_children()
        for child in children:
            child.state = State.DISABLE

