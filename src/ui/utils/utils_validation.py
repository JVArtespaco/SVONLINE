import customtkinter as ctk
from src.core.protocols import HasChildren

def _verify_entry(widget: ctk.CTkEntry) -> None:
    if widget.get().strip() == "":
        widget.configure(border_color="red")
    else:
        widget.configure(border_color="#198754")

def _verify_combobox(widget: ctk.CTkComboBox) -> None:
    if widget.get().strip() in ("", "selecionar", "Selecionar"):
        widget.configure(border_color="red")
    else:
        widget.configure(border_color="#198754")

def change_edges_color(widget: HasChildren) -> None:
    if isinstance(widget, ctk.CTkEntry):
        _verify_entry(widget)

    elif isinstance(widget, ctk.CTkComboBox):
        _verify_combobox(widget)

    for child in widget.winfo_children():
        change_edges_color(child)
