from src.ui.components.frames import BaseWorkAreaFrame
from .product_frame_components import ProductFormFrame
from src.core.enums import Colors, Font
from src.ui.components.buttons import BaseButton
from src.core.enums import UtilsEnumPTBR


class ProductFrame(BaseWorkAreaFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._set_title("Produto")

        self.form_frame = ProductFormFrame(self.frame, fg_color=Colors.WHITE.value)
        self.form_frame.pack()

        self.save_button: BaseButton = BaseButton(self.frame,
                                                  text=UtilsEnumPTBR.SAVE.value,
                                                  command=self.save_items,
                                                  font=(Font.ARIAL.value, 14))
        self.save_button.pack()

    def save_items(self):
        pass






