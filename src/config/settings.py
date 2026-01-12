# config/settings.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

APPEARANCE_MODE = "light"
APP_NAME = "Sistema Vendas Online"
DEBUG = True

DEFAULT_WINDOW_SIZE = (1250, 720)

DATE_FORMAT = "%d/%m/%Y"
CURRENCY_SYMBOL = "R$"
