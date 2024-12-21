def limpar_campo(campo):
    """
    Limpa o campo de entrada.
    :param campo: QLineEdit.
    """
    campo.clear()


def validar_decimal(valor):
    """
    Valida se o valor pode ser convertido para decimal.
    :param valor: string.
    :return: True se válido, False caso contrário.
    """
    try:
        float(valor)
        return True
    except ValueError:
        return False
