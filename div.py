def div(number1: float, number2: float) -> float:
    if number2 == 0:
        raise ValueError("No se puede dividir por cero.")
    return number1 / number2