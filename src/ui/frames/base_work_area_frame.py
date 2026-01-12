from __future__ import annotations
from .base_frame import BaseFrame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.ui.screens.main_screen.work_area import WorkArea


class BaseWorkAreaFrame(BaseFrame):
    def __init__(self, parent: WorkArea, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.frame: BaseFrame = BaseFrame(self)

    def show_frame(self):
        self.frame.pack()

    def hidden_frame(self):
        self.frame.pack_forget()