from __future__ import annotations
from src.ui.components.menus.base_menu import Menu
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.ui.screens.main_screen.top_bar import TopBar


class ProductMenu(Menu):
    def __init__(self,
                 parent: TopBar,
                 *args,
                 **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent: TopBar = parent
        self._placeholder = "Produto"
        self._menu_options = ["Produto Base",
                              "Produto KIt,"
                              "Varição,"]

        self._pre_select_var.set(self._placeholder)

        self.configure(width=self.calculate_width(),
                       variable=self._pre_select_var,
                       values=self._menu_options,
                       command=self._security_callback)

    def select_option(self, choice) -> None:
        self.parent.parent.main_frame.clear_main()

        if choice == "Produto Base":
            #ProductBase(self.parent.parent.main_frame)
            pass
        self.parent.parent.main_frame.create_close_button(callback=self.reset_dropdown)


__all__ = ["ProductMenu"]