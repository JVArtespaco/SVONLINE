from __future__ import annotations
from customtkinter import CTkFrame
from .top_bar_menus import ProductMenu
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.ui.screens.main_screen.main_screen import MainScreen


class TopBar(CTkFrame):
    def __init__(self,
                 parent: MainScreen,
                 *args,
                 **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent: MainScreen = parent

        self.product_menu = ProductMenu(self, fg_color="white", text_color="black",
                                        button_color="#ebebeb", button_hover_color="#d6d6d6")
        self.product_menu.grid(row=0, column=0, padx=5, pady=2, stick="w")


