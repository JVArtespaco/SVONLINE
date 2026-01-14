from src.ui.components.buttons import ButtonAreaBaseButton
from typing import TYPE_CHECKING
from src.core.enums import Font, BootstrapColors, UtilsEnumEn


if TYPE_CHECKING:
    from src.ui.screens.main_screen.butons_area import ButtonsArea


class AddButton(ButtonAreaBaseButton):
    def __init__(self, parent: ButtonsArea, *args, **kwargs):
        super().__init__(parent, *args, *kwargs)
        self.parent: ButtonsArea = parent
        self.configure(text="+",
                       font=(Font.ARIAL.value, 20, Font.BOLD.value),
                       fg_color=BootstrapColors.SECONDARY.value,
                       width=20,
                       border_color=BootstrapColors.WHITE.value,
                       border_width=3,
                       hover_color=BootstrapColors.DARK.value,
                       command=self.add)

    def add(self):
        if self.parent.parent.work_area.current_frame:
            self.parent.parent.work_area.current_frame.show_frame()
            self.parent.parent.work_area.current_frame.type_button = UtilsEnumEn.ADD.value

