import customtkinter as ctk
from src.ui.utils import centralize_toplevel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.protocols.ctk_widgets import CTkBase


class CTkAlert(ctk.CTkToplevel):
    def __init__(self, parent: CTkBase, message: str, title: str = "Aviso"):
        super().__init__(parent)
        self.title(title)
        self.resizable(False, False)
        self.grab_set()  # Modal (trava interação na janela principal)

        self.protocol("WM_DELETE_WINDOW", self._close)  # Intercepta o 'X'

        centralize_toplevel(self, 320, 140)

        # Animação Fade-In
        self.attributes("-alpha", 0.0)
        self._fade_in()

        # Conteúdo
        frame = ctk.CTkFrame(self, corner_radius=10)
        frame.pack(expand=True, fill="both", padx=10, pady=10)
        if title == "Aviso":
            ctk.CTkLabel(frame, text="⚠️", font=("Arial", 32)).pack(pady=(10, 0))
        ctk.CTkLabel(frame, text=message, wraplength=260, font=("Arial", 14)).pack(pady=(5, 15))

        ctk.CTkButton(frame, text="OK", width=80, command=self._close).pack()

    def _fade_in(self) -> None:
        alpha = self.attributes("-alpha")
        if alpha < 1:
            alpha += 0.08
            self.attributes("-alpha", alpha)
            self.after(15, self._fade_in)

    def _close(self) -> None:
        # Inicia a animação de fade out
        self._fade_out(1.0)

    def _fade_out(self, opacity) -> None:
        if opacity > 0:
            # Reduz a opacidade em passos (ex: 0.1)
            opacity -= 0.1
            if opacity < 0:
                opacity = 0
            # Define a opacidade da janela
            self.attributes("-alpha", opacity)
            # Agenda a próxima redução de opacidade após um curto intervalo (ex: 20 ms)
            self.after(20, self._fade_out, opacity)
        else:
            # Quando a opacidade chega a 0, destrói a janela
            self.destroy()