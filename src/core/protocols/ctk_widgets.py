from __future__ import annotations
from typing import Protocol, Iterable, runtime_checkable, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from classes.register import Register
    from classes import form_area


@runtime_checkable
class HasChildren(Protocol):
    def winfo_children(self) -> Iterable["HasChildren"]: ...


@runtime_checkable
class CTkBase(HasChildren, Protocol):
    def winfo_width(self) -> int: ...

    def winfo_height(self) -> int: ...


@runtime_checkable
class RegisterFrame(CTkBase, Protocol):
    register_item: Register | None
    form_area: FormBase


@runtime_checkable
class FormBase(CTkBase, Protocol):
    def clear_fields(self) -> None: ...

    def change_edges(self) -> None: ...

    def return_fields_values(self) -> dict[str, str]: ...

    def validate_fields(self) -> int: ...