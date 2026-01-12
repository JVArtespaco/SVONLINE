from customtkinter import CTkOptionMenu, StringVar
from abc import abstractmethod, ABC


class Menu(CTkOptionMenu, ABC):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._menu_options: list[str] = []
        self._pre_select_var: StringVar = StringVar()
        self.configure(width=self.calculate_width())
        self._placeholder: str = ""

    def _security_callback(self, choice) -> None:
        """
        CustomTkinter chama o callback até quando não deveria.
        Este método impede que valores inválidos disparem a lógica.
        """
        self._pre_select_var.set(self._placeholder)
        if choice not in self._menu_options:
            return  # Ignora valores inválidos

        self.select_option(choice)

    def reset_dropdown(self) -> None:
        """
        Quando o botão X for clicado,
        o OptionMenu é automaticamente resetado para o placeholder.
        """
        self._pre_select_var.set(self._placeholder)

    def calculate_width(self) -> int:
        return self._font.measure(self._pre_select_var.get()) + 40

    def reset(self) -> None:
        self.configure(variable=self._pre_select_var)

    @abstractmethod
    def select_option(self, choice) -> None:
        pass
