from src.ui.components.frames import FormArea
from customtkinter import CTkEntry, CTkLabel
from src.core.enums import Colors, ProductEnumPTBR, ProductEnumEn
from src.ui.components.entrys import FloatEntry
from src.ui.components.combobox import PackageComboBox


class ProductFormFrame(FormArea):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        (CTkLabel(self, text=ProductEnumPTBR.NAME.value, fg_color=Colors.WHITE.value)
         .grid(column=0, row=0, padx=5, pady=5))
        self.product_name_entry: CTkEntry = CTkEntry(self, width=250)
        self.product_name_entry.grid(column=1, row=0, padx=5, pady=5)

        (CTkLabel(self, text=ProductEnumPTBR.BRAND.value, fg_color=Colors.WHITE.value).
         grid(column=2, row=0, padx=5, pady=5))
        self.product_brand_entry: CTkEntry = CTkEntry(self, width=150)
        self.product_brand_entry.grid(column=3, row=0)

        (CTkLabel(self, text=ProductEnumPTBR.WEIGHT.value, fg_color=Colors.WHITE.value)
         .grid(column=4, row=0, padx=5, pady=5))
        self.product_weight_entry: FloatEntry = FloatEntry(3, self, width=50)
        self.product_weight_entry.grid(column=5, row=0, padx=5, pady=5)

        (CTkLabel(self, text=ProductEnumPTBR.COST_PRICE.value, fg_color=Colors.WHITE.value)
         .grid(column=6, row=0, padx=5, pady=5))
        self.product_cost_price_entry: FloatEntry = FloatEntry(2, self, width=50)
        self.product_cost_price_entry.grid(column=7, row=0, padx=5, pady=5)

        (CTkLabel(self, text=ProductEnumPTBR.PACKAGE.value, fg_color=Colors.WHITE.value)
         .grid(column=8, row=0, padx=5, pady=5))
        self.product_package_combobox: PackageComboBox = PackageComboBox(self)
        self.product_package_combobox.grid(column=9, row=0, padx=5, pady=5)
        self.all_select_vars.append(self.product_package_combobox.var)

    def return_fields_values(self) -> dict[str, str]:
        return {ProductEnumEn.NAME.value: self.product_name_entry.get(),
                ProductEnumEn.BRAND.value: self.product_brand_entry.get(),
                ProductEnumEn.WEIGHT.value: self.product_weight_entry.get(),
                ProductEnumEn.COST_PRICE.value: self.product_cost_price_entry.get(),
                ProductEnumEn.PACKAGE.value: str(self.product_package_combobox.get_id())}

