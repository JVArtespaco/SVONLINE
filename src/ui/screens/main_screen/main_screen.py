from src.ui.screens.main_screen.top_bar import TopBar
from src.ui.screens.main_screen.butons_area import ButtonsArea
from src.ui.screens.main_screen.work_area import WorkArea
from customtkinter import CTkFrame


class MainScreen(CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self._create_layout()

    def _create_layout(self) -> None:
        self.button_area = ButtonsArea(self, height=50, fg_color="darkblue", corner_radius=0)
        self.button_area.pack(side="top", fill="x")

        self.top_bar = TopBar(self, height=50, fg_color="darkblue", corner_radius=0)
        self.top_bar.pack(side="top", fill="x")

        self.main_frame = WorkArea(self)
        self.main_frame.pack(side="top", fill="both", expand=True, padx=0, pady=0)
