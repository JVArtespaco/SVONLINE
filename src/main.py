# src/main.py
import sys
import customtkinter as ctk
from src.config.settings import APPEARANCE_MODE
from src.database.migrations.runner import run_migrations
from src.ui.app import App


def bootstrap():
    # Aparência
    ctk.set_appearance_mode(APPEARANCE_MODE)

    # Testa banco
    try:
        #test_connection()
        run_migrations()
    except Exception as e:
        print("Erro ao conectar no banco:", e)
        sys.exit(1)

    # Inicia aplicação
    app = App()
    app.run()


if __name__ == "__main__":
    bootstrap()

