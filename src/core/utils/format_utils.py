def order_int_on_string(n1, n2, n3) -> str:
    lista = [int(n1), int(n2), int(n3)]
    lista = sorted(lista, reverse=True)
    return f"{lista[0]}cm x {lista[1]}cm x {lista[2]}cm"


__all__ = ["order_int_on_string"]