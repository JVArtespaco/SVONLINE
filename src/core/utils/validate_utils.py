def validate_select(var) -> bool:
    if var:
        if var.get() == "Selecionar":
            return False
        else:
            return True
    else:
        return True

def verify_fields(values) -> int:
    tot = 0
    for value in list(values.values()):
        if value == "":
            tot += 1
    return tot
