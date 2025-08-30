def format_cents(value: int) -> str:
    "transforms all received values ​​into a string with R$ at the beginning and cents"
    f_value: float = value / 100
    return "R$ {:,.2f}".format(f_value).replace(',', '_').replace('.', ',').replace('_', '.')