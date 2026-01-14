import customtkinter as ctk
from src.utils import check_query
from src.ui.components.top_level import CTkAlert


class PackageComboBox(ctk.CTkComboBox):
    def __init__(self, parent: ctk.CTkFrame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.__options = None
        self.__packages_names = ""
        self.load_packaging()
        self.var = ctk.StringVar(value=self.__packages_names[0])
        self.configure(values=self.__packages_names, variable=self.var, width=300,
                       state="readonly")

    def load_packaging(self) -> None:
        try:
            result = check_query()
            if result:
                self.__options = result
                self.__options = sorted(self.__options)
                self.__options.insert(0, (0, "Selecionar"))
                self.__packages_names = [op[1] for op in self.__options]
        except Exception as e:
            CTkAlert(self, f"Erro ao buscar produtos:\n{e}")

    def get_id(self) -> int:
        package_index = self.__packages_names.index(self.var.get())
        selected_id = self.__options[package_index][0]
        return selected_id