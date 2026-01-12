from src.ui.components.buttons import ButtonAreaBaseButton
from typing import TYPE_CHECKING
from src.core.enums import Font

if TYPE_CHECKING:
    from src.ui.screens.main_screen.butons_area import ButtonsArea


class AddButton(ButtonAreaBaseButton):
    def __init__(self, parent: ButtonsArea, *args, **kwargs):
        super().__init__(parent, *args, *kwargs)
        self.parent: ButtonsArea = parent
        self.configure(text="+", font=(Font.ARIAL.value, 20, Font.BOLD.value))

    def add(self):
        if self.parent.parent.main_frame.current_frame:
            self.parent.parent.main_frame.current_frame.show_frame()

