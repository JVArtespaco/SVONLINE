def centralize_toplevel(toplevel_window, width: int, height: int) -> None:
    """
    Centraliza uma janela Toplevel na tela do computador.

    Args:
        toplevel_window: A instância da janela Toplevel (ou Tk principal).
        width: A largura desejada para a janela em pixels.
        height: A altura desejada para a janela em pixels.
    """

    # 1. Obtém a largura e altura da tela do usuário
    screen_width = toplevel_window.winfo_screenwidth()
    screen_height = toplevel_window.winfo_screenheight()

    # 2. Calcula a posição X e Y para centralização
    # (Largura da Tela / 2) - (Largura da Janela / 2)
    pos_x = (screen_width // 2) - (width // 2)
    pos_y = (screen_height // 2) - (height // 2)

    # 3. Define a geometria da janela usando o formato "LxA+X+Y"
    toplevel_window.geometry(f'{width}x{height}+{pos_x}+{pos_y}')

    # Opcional: Garante que a janela esteja visível e no topo
    toplevel_window.lift()
    toplevel_window.attributes('-topmost', True)
    toplevel_window.after_idle(toplevel_window.attributes, '-topmost', False)