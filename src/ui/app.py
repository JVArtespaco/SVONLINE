from customtkinter import CTk
from src.ui.screens.main_screen.main_screen import MainScreen
from src.config.settings import APP_NAME


class App(CTk):

    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self._configure_window()
        self._load_main_screen()

    def _configure_window(self):
        self.after(10, lambda: self.state("zoomed"))

    def _load_main_screen(self):
        MainScreen(self).pack(fill="both", expand=True)

    def run(self):
        self.mainloop()
