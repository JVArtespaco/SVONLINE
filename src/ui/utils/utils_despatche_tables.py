import customtkinter as ctk

ACTIONS = {
    ctk.CTkEntry: lambda widget: widget.delete(0, ctk.END),
    ctk.CTkOptionMenu: lambda widget: widget.set(widget.cget("values")[0] if widget.cget("values") else ""),
    ctk.CTkComboBox: lambda widget: widget.set(widget.cget("values")[0] if widget.cget("values") else "")
}
