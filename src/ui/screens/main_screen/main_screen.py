from src.ui.screens.main_screen.top_bar import TopBar
from src.ui.screens.main_screen.butons_area import ButtonsArea
from src.ui.screens.main_screen.work_area import WorkArea
from customtkinter import CTkFrame, TOP, BOTH, X
from src.core.enums import Colors


class MainScreen(CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self._create_layout()

    def _create_layout(self) -> None:
        self.button_area = ButtonsArea(self, height=50, fg_color=Colors.DARK_BLUE.value, corner_radius=0)
        self.button_area.pack(side=TOP, fill=X)

        self.top_bar = TopBar(self, height=50, fg_color=Colors.DARK_BLUE.value, corner_radius=0)
        self.top_bar.pack(side=TOP, fill=X)

        self.work_area = WorkArea(self)
        self.work_area.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=0)
