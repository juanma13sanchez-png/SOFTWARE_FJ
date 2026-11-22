
"""
Proyecto: Software FJ
Archivo: pruebas_excepciones.py
Descripción: Demuestra el manejo avanzado de excepciones
utilizado en el sistema Software FJ.
"""

import logging
from pathlib import Path

from cliente import Cliente
from excepciones import ValidacionError

# Configuramos el registro de errores.
carpeta_logs = Path(__file__).parent / "logs"
carpeta_logs.mkdir(exist_ok=True)

logging.basicConfig(
    filename=carpeta_logs / "sistema.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8",
    force=True
)

logger = logging.getLogger("PruebasExcepciones")


print("=" * 55)
print("       PRUEBAS DE EXCEPCIONES SOFTWARE FJ")
print("=" * 55)


# PRUEBA 1: TRY / EXCEPT
print("\nPRUEBA 1: TRY / EXCEPT")

try:
    cliente = Cliente(
        "Juan Pérez",
        "ABC123",
        "juan@gmail.com",
        "3001234567"
    )

except ValueError as error:
    print("Error controlado:", error)
    logger.exception("Error detectado en prueba 1.")

print("El sistema continúa funcionando.")


# PRUEBA 2: TRY / EXCEPT / ELSE
print("\nPRUEBA 2: TRY / EXCEPT / ELSE")

try:
    cliente = Cliente(
        "María Fernanda",
        "1234567890",
        "maria@gmail.com",
        "3109876543"
    )

except ValueError as error:
    print("Error al registrar:", error)
    logger.exception("Error detectado en prueba 2.")

else:
    print("Cliente creado correctamente.")
    print(cliente.describir())
    logger.info("Cliente creado en prueba 2.")


# PRUEBA 3: TRY / EXCEPT / FINALLY
print("\nPRUEBA 3: TRY / EXCEPT / FINALLY")

try:
    resultado = 10 / 0
    print("Resultado:", resultado)

except ZeroDivisionError as error:
    print("Error controlado: no se puede dividir entre cero.")
    logger.exception("Error detectado en prueba 3.")

finally:
    print("Bloque FINALLY ejecutado.")
    print("Finalización de la operación.")


# PRUEBA 4: ENCADENAMIENTO DE EXCEPCIONES
print("\nPRUEBA 4: ENCADENAMIENTO DE EXCEPCIONES")

try:
    try:
        numero = int("Software FJ")

    except ValueError as error:
        raise ValidacionError(
            "No fue posible convertir el dato a número."
        ) from error

except ValidacionError as error:
    print("Excepción personalizada:", error)
    print("Causa original:", error.__cause__)
    logger.exception("Error detectado en prueba 4.")


print("\n" + "=" * 55)
print("FINALIZARON LAS PRUEBAS DE EXCEPCIONES")
print("EL SISTEMA CONTINÚA FUNCIONANDO")
print("=" * 55)
