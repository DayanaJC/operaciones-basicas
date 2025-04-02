"""
Módulo para realizar operaciones básicas y calcular el promedio de una lista de números.

Dayana Jessica Javier Curi
"""


class OperacionesBasicas:
    """Clase para realizar operaciones matemáticas básicas."""

    def __init__(self):
        """Inicializa el resultado en cero."""
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado."""
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado."""
        self.resultado = a - b

    def obtener_resultado(self):
        """Retorna el resultado de la última operación realizada."""
        return self.resultado


class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores):
        """Inicializa la lista de valores."""
        self.valores = valores

    def calcular_promedio(self):
        """Calcula y retorna el promedio de los valores."""
        if not self.valores:
            return 0  # Evita la división por cero
        return sum(self.valores) / len(self.valores)

    def obtener_cantidad_valores(self):
        """Retorna la cantidad de valores en la lista."""
        return len(self.valores)


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20


# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora = CalculadoraPromedio(NUMEROS)
    promedio_numeros = calculadora.calcular_promedio()
    print(f"El promedio de los números es: {promedio_numeros}")
