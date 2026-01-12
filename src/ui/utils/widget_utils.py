from src.core.protocols.ctk_widgets import HasChildren


def apply_recursive(container: HasChildren, action_map) -> None:
    for widget in container.winfo_children():
        for widget_type, action in action_map.items():
            if isinstance(widget, widget_type):
                action(widget)
                break

        if widget.winfo_children():  # Se tiver filhos, chama recursivo
            apply_recursive(widget, action_map)