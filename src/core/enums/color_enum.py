from enum import Enum


class Colors(Enum):
    WHITE = "white"
    BLACK = "black"
    GREEN = "green"
    DARK_BLUE = "darkblue"
    YELLOW = "yellow"
    RED = "red"
    BLUE = "blue"
    LIGHT_GRAY = "#d6d6d6"
    VERY_LIGHT_GRAY = "#ebebeb"


class BootstrapColors(Enum):
    PRIMARY = "#0d6efd"
    SECONDARY = "#6c757d"
    SUCCESS = "#198754"
    DANGER = "#dc3545"
    WARNING = "#ffc107"
    INFO = "#0dcaf0"
    LIGHT = "#f8f9fa"
    DARK = "#212529"
    BODY = "#212529"
    WHITE = "#ffffff"
    MUTED = "#6c757d"
    BORDER = "#dee2e6"


class BootstrapExtendedColors(Enum):
    # PRIMARY
    PRIMARY_100 = "#cfe2ff"
    PRIMARY_200 = "#9ec5fe"
    PRIMARY_300 = "#6ea8fe"
    PRIMARY_400 = "#3d8bfd"
    PRIMARY_500 = "#0d6efd"  # original
    PRIMARY_600 = "#0a58ca"
    PRIMARY_700 = "#084298"
    PRIMARY_800 = "#052c65"
    PRIMARY_900 = "#031633"

    # SECONDARY
    SECONDARY_100 = "#e2e3e5"
    SECONDARY_200 = "#c5c6c8"
    SECONDARY_300 = "#a8a9ac"
    SECONDARY_400 = "#8b8c8f"
    SECONDARY_500 = "#6c757d"  # original
    SECONDARY_600 = "#565e64"
    SECONDARY_700 = "#41464b"
    SECONDARY_800 = "#2d3238"
    SECONDARY_900 = "#1a1d20"

    # SUCCESS
    SUCCESS_100 = "#d1e7dd"
    SUCCESS_200 = "#a3cfbb"
    SUCCESS_300 = "#75b798"
    SUCCESS_400 = "#479f76"
    SUCCESS_500 = "#198754"  # original
    SUCCESS_600 = "#146c43"
    SUCCESS_700 = "#0f5132"
    SUCCESS_800 = "#0a3622"
    SUCCESS_900 = "#051b11"

    # DANGER
    DANGER_100 = "#f8d7da"
    DANGER_200 = "#f1aeb5"
    DANGER_300 = "#ea868f"
    DANGER_400 = "#e35d6a"
    DANGER_500 = "#dc3545"  # original
    DANGER_600 = "#b02a37"
    DANGER_700 = "#842029"
    DANGER_800 = "#58151c"
    DANGER_900 = "#2c0b0e"

    # WARNING
    WARNING_100 = "#fff3cd"
    WARNING_200 = "#ffe69c"
    WARNING_300 = "#ffda6a"
    WARNING_400 = "#ffcd39"
    WARNING_500 = "#ffc107"  # original
    WARNING_600 = "#cc9a06"
    WARNING_700 = "#997404"
    WARNING_800 = "#664d03"
    WARNING_900 = "#332701"

    # INFO
    INFO_100 = "#cff4fc"
    INFO_200 = "#9eeaf9"
    INFO_300 = "#6edff6"
    INFO_400 = "#3dd5f3"
    INFO_500 = "#0dcaf0"  # original
    INFO_600 = "#0aa2c0"
    INFO_700 = "#087990"
    INFO_800 = "#055160"
    INFO_900 = "#032830"

    # LIGHT
    LIGHT_100 = "#fefefe"
    LIGHT_200 = "#fdfdfe"
    LIGHT_300 = "#fcfcfd"
    LIGHT_400 = "#fafafb"
    LIGHT_500 = "#f8f9fa"
    LIGHT_600 = "#c7c8ca"
    LIGHT_700 = "#959698"
    LIGHT_800 = "#646566"
    LIGHT_900 = "#323233"

    # DARK
    DARK_100 = "#d3d3d4"
    DARK_200 = "#a6a7a8"
    DARK_300 = "#7a7b7d"
    DARK_400 = "#4d4f51"
    DARK_500 = "#212529"  # original
    DARK_600 = "#1a1e21"
    DARK_700 = "#141619"
    DARK_800 = "#0d0f10"
    DARK_900 = "#060708"
