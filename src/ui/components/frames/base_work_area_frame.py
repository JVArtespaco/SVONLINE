from __future__ import annotations
from .base_frame import BaseFrame
from typing import TYPE_CHECKING
from customtkinter import BOTH, TOP
from src.core.enums import Colors

if TYPE_CHECKING:
    from src.ui.screens.main_screen.work_area import WorkArea


class BaseWorkAreaFrame(BaseFrame):
    def __init__(self, parent: WorkArea, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent: WorkArea = parent
        self.frame: BaseFrame = BaseFrame(self,
                                          fg_color=Colors.WHITE.value,
                                          corner_radius=0)
        self.configure(fg_color=Colors.WHITE.value)

    def show_frame(self):
        if not self.frame.winfo_manager():
            self.frame.pack(side=TOP, fill=BOTH, expand=True)
            self.hidden_buttons()

    def hidden_frame(self):
        self.frame.pack_forget()

    def hidden_buttons(self):
        self.parent.parent.button_area.diable_all_children()
