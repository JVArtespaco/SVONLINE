from customtkinter import CTkScrollableFrame
from src.ui.frames.base_frame import BaseFrame


class ProductFrame(BaseFrame, CTkScrollableFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._set_title("Produto")






