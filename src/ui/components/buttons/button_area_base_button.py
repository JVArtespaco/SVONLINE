from .base_button import BaseButton
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.ui.screens.main_screen.butons_area import ButtonsArea


class ButtonAreaBaseButton(BaseButton):
    def __init__(self, parent: ButtonsArea, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent: ButtonsArea = parent


