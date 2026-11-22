
"""
Proyecto: Software FJ
Archivo: main.py
Descripción: Pruebas iniciales del módulo de reservas.
"""

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo
from reserva import Reserva
from excepciones import SoftwareFJError

print("======================================")
print("       SISTEMA SOFTWARE FJ")
print("       PRUEBAS DE RESERVAS")
print("======================================")

# Creamos un cliente.
cliente1 = Cliente(
    "Juan Carlos Pérez",
    "1234567890",
    "juancarlos@gmail.com",
    "3001234567"
)

# Creamos dos servicios.
sala = ReservaSala("Sala principal", 50000, 20)
equipos = AlquilerEquipo("Proyectores", 30000, 5)


# PRUEBA 1: Crear una reserva.
print("\nPRUEBA 1: Crear reserva")

try:
    reserva1 = Reserva(cliente1, sala, 2, asistentes=10)
    print("Reserva creada correctamente.")
    print(reserva1.describir())

except SoftwareFJError as error:
    print("Error:", error)


# PRUEBA 2: Confirmar la reserva.
print("\nPRUEBA 2: Confirmar reserva")

try:
    print(reserva1.confirmar())
    print("Estado:", reserva1.estado)

except SoftwareFJError as error:
    print("Error:", error)


# PRUEBA 3: Procesar la reserva.
print("\nPRUEBA 3: Procesar reserva")

try:
    costo = reserva1.procesar(impuesto=19)
    print("Costo final:", costo)
    print("Estado:", reserva1.estado)

except SoftwareFJError as error:
    print("Error:", error)


# PRUEBA 4: Intentar cancelar una reserva procesada.
print("\nPRUEBA 4: Cancelar reserva procesada")

try:
    reserva1.cancelar()

except SoftwareFJError as error:
    print("Error controlado:", error)


# PRUEBA 5: Intentar crear una reserva con duración inválida.
print("\nPRUEBA 5: Duración incorrecta")

try:
    reserva2 = Reserva(cliente1, equipos, -3, unidades=2)

except SoftwareFJError as error:
    print("Error controlado:", error)


# PRUEBA 6: Crear y cancelar una reserva pendiente.
print("\nPRUEBA 6: Cancelar reserva pendiente")

try:
    reserva3 = Reserva(cliente1, equipos, 2, unidades=2)

    print(reserva3.cancelar())
    print("Estado:", reserva3.estado)

except SoftwareFJError as error:
    print("Error:", error)


print("\n======================================")
print("FINALIZARON LAS PRUEBAS DE RESERVAS")
print("EL SISTEMA CONTINÚA FUNCIONANDO")
print("======================================")

