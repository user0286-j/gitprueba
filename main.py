# Crear una tabla de multiplicación
from add import add
from div import div
from mul import mul
from res import res

"""
Tiene los siguientes módulos:

- mul(number1, number2) Jhoel
- add(number1, number2) Amilcar
- diff(number1, number2) Jhon
- div(number1, number2) César

Quiero que implementen cada uno de los módulos
y en el main añadir una pequeña interfaz
"""

if __name__ == "__main__":
    print("Mini-calculadora")
    number1: float = float(input("Dame el primer número: "))
    number2: float = float(input("Dame el segundo número: "))
    print("\nQué operación quisieras hacer?")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. División")
    opcion: int = int(input("----->"))
    if 1 <= opcion <= 4: # Dentro de los parámetros
        if opcion == 1:
            print(f"El resultado es {add(number1, number2)}")
        elif opcion == 2:
            print(f"El resultado es {res(number1, number2)}")
        elif opcion == 3:
            print(f"El resultado es {mul(number1, number2)}")
        elif opcion == 4:
            print(f"El resultado es {div(number1, number2)}")
