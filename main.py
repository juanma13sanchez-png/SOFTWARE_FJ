
"""
Proyecto: Software FJ
Archivo: main.py
Descripción: Pruebas de los servicios especializados.
"""

from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

print("======================================")
print("       SISTEMA SOFTWARE FJ")
print("       PRUEBAS DE SERVICIOS")
print("======================================")

# PRUEBA 1: Crear una reserva de sala.
print("\nPRUEBA 1: Reserva de sala")

try:
    sala = ReservaSala("Sala de reuniones", 50000, 20)

    print(sala.describir())

    costo = sala.calcular_costo(2)
    print("Costo por 2 horas:", costo)

except ValueError as error:
    print("Error:", error)


# PRUEBA 2: Crear un alquiler de equipos.
print("\nPRUEBA 2: Alquiler de equipos")

try:
    equipo = AlquilerEquipo("Proyectores", 30000, 10)

    print(equipo.describir())

    costo = equipo.calcular_costo(3, unidades=2)
    print("Costo por 3 horas y 2 equipos:", costo)

except ValueError as error:
    print("Error:", error)


# PRUEBA 3: Crear una asesoría especializada.
print("\nPRUEBA 3: Asesoría especializada")

try:
    asesoria = AsesoriaEspecializada(
        "Asesoría tecnológica",
        80000,
        "Desarrollo de software"
    )

    print(asesoria.describir())

    costo = asesoria.calcular_costo(
        2,
        impuesto=19,
        descuento=10,
        modalidad="virtual"
    )

    print("Costo con impuesto y descuento:", costo)

except ValueError as error:
    print("Error:", error)


# PRUEBA 4: Intentar reservar una sala con demasiados asistentes.
print("\nPRUEBA 4: Validación de capacidad")

try:
    sala.calcular_costo(2, asistentes=30)

except ValueError as error:
    print("Error controlado:", error)


# PRUEBA 5: Intentar alquilar más equipos de los disponibles.
print("\nPRUEBA 5: Validación de disponibilidad")

try:
    equipo.calcular_costo(2, unidades=15)

except ValueError as error:
    print("Error controlado:", error)


print("\n======================================")
print("FINALIZARON LAS PRUEBAS DE SERVICIOS")
print("El programa continúa funcionando.")
print("======================================")

