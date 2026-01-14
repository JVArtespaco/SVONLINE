from enum import Enum


class ProductEnumPTBR(Enum):
    NAME = "Nome"
    COST_PRICE = "Preço de custo"
    WEIGHT = "Peso"
    BRAND = "Marca"
    PACKAGE = "Embalagem"


class ProductEnumEn(Enum):
    NAME = "name"
    COST_PRICE = "cost_price"
    WEIGHT = "weight"
    BRAND = "brand"
    PACKAGE = 'package'