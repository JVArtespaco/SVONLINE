from customtkinter import W
from src.ui.components.frames import BaseWorkAreaFrame
from src.ui.components.buttons import BaseButton


class ProductFrame(BaseWorkAreaFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._set_title("Produto")
        self.button = BaseButton(self.frame, text="teste")
        self.button.grid(row=0, column=0, stick=W, pady=10, padx=10)





