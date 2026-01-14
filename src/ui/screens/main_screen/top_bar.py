from __future__ import annotations
from customtkinter import CTkFrame, W
from .top_bar_menus import ProductMenu
from typing import TYPE_CHECKING
from src.core.enums import Colors

if TYPE_CHECKING:
    from src.ui.screens.main_screen.main_screen import MainScreen


class TopBar(CTkFrame):
    def __init__(self,
                 parent: MainScreen,
                 *args,
                 **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent: MainScreen = parent

        self.product_menu = ProductMenu(self, fg_color=Colors.WHITE.value,
                                        text_color=Colors.BLACK.value,
                                        button_color=Colors.VERY_LIGHT_GRAY.value,
                                        button_hover_color=Colors.LIGHT_GRAY.value)
        self.product_menu.grid(row=0, column=0, padx=5, pady=(0, 10), stick=W)


