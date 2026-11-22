
"""
Proyecto: Software FJ
Archivo: main.py
Descripción: Pruebas de integración del sistema Software FJ.
"""

from sistema import SistemaGestion
from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from excepciones import SoftwareFJError

print("=" * 55)
print("          SISTEMA INTEGRAL SOFTWARE FJ")
print("              PRUEBAS DE GESTIÓN")
print("=" * 55)

# Creamos el sistema.
sistema = SistemaGestion()

# --------------------------------------------------
# OPERACIÓN 1: Registrar un cliente válido.
# --------------------------------------------------

print("\nOPERACIÓN 1: Registrar cliente")

cliente1 = Cliente(
    "Juan Carlos Pérez",
    "1234567890",
    "juancarlos@gmail.com",
    "3001234567"
)

try:
    print(sistema.registrar_cliente(cliente1))
except SoftwareFJError as error:
    print("Error:", error)


# --------------------------------------------------
# OPERACIÓN 2: Intentar registrar un cliente duplicado.
# --------------------------------------------------

print("\nOPERACIÓN 2: Cliente duplicado")

cliente_duplicado = Cliente(
    "María Fernanda",
    "1234567890",
    "maria@gmail.com",
    "3109876543"
)

try:
    sistema.registrar_cliente(cliente_duplicado)
except SoftwareFJError as error:
    print("Error controlado:", error)


# --------------------------------------------------
# OPERACIÓN 3: Registrar una sala.
# --------------------------------------------------

print("\nOPERACIÓN 3: Registrar sala")

sala = ReservaSala("Sala principal", 50000, 20)

try:
    print(sistema.registrar_servicio(sala))
except SoftwareFJError as error:
    print("Error:", error)


# --------------------------------------------------
# OPERACIÓN 4: Registrar equipos.
# --------------------------------------------------

print("\nOPERACIÓN 4: Registrar equipos")

equipos = AlquilerEquipo("Proyectores", 30000, 10)

try:
    print(sistema.registrar_servicio(equipos))
except SoftwareFJError as error:
    print("Error:", error)


# --------------------------------------------------
# OPERACIÓN 5: Registrar asesoría.
# --------------------------------------------------

print("\nOPERACIÓN 5: Registrar asesoría")

asesoria = AsesoriaEspecializada(
    "Asesoría tecnológica",
    80000,
    "Desarrollo de software"
)

try:
    print(sistema.registrar_servicio(asesoria))
except SoftwareFJError as error:
    print("Error:", error)


# --------------------------------------------------
# OPERACIÓN 6: Intentar registrar un servicio duplicado.
# --------------------------------------------------

print("\nOPERACIÓN 6: Servicio duplicado")

servicio_duplicado = ReservaSala("SALA PRINCIPAL", 60000, 15)

try:
    sistema.registrar_servicio(servicio_duplicado)
except SoftwareFJError as error:
    print("Error controlado:", error)


# --------------------------------------------------
# OPERACIÓN 7: Crear una reserva válida.
# --------------------------------------------------

print("\nOPERACIÓN 7: Crear reserva")

try:
    reserva1 = sistema.crear_reserva(
        cliente1,
        sala,
        2,
        asistentes=10
    )

    print("Reserva creada:", reserva1.id)

except SoftwareFJError as error:
    print("Error:", error)


# --------------------------------------------------
# OPERACIÓN 8: Confirmar la reserva.
# --------------------------------------------------

print("\nOPERACIÓN 8: Confirmar reserva")

try:
    print(sistema.confirmar_reserva(reserva1.id))
except SoftwareFJError as error:
    print("Error:", error)


# --------------------------------------------------
# OPERACIÓN 9: Procesar la reserva.
# --------------------------------------------------

print("\nOPERACIÓN 9: Procesar reserva")

try:
    costo = sistema.procesar_reserva(
        reserva1.id,
        impuesto=19,
        descuento=0
    )

    print("Costo final:", costo)

except SoftwareFJError as error:
    print("Error:", error)


# --------------------------------------------------
# OPERACIÓN 10: Intentar cancelar una reserva procesada.
# --------------------------------------------------

print("\nOPERACIÓN 10: Cancelar reserva procesada")

try:
    sistema.cancelar_reserva(reserva1.id)

except SoftwareFJError as error:
    print("Error controlado:", error)


# --------------------------------------------------
# OPERACIÓN 11: Crear reserva con duración inválida.
# --------------------------------------------------

print("\nOPERACIÓN 11: Duración incorrecta")

try:
    sistema.crear_reserva(
        cliente1,
        equipos,
        -5,
        unidades=2
    )

except SoftwareFJError as error:
    print("Error controlado:", error)


# --------------------------------------------------
# OPERACIÓN 12: Consultar resumen del sistema.
# --------------------------------------------------

print("\nOPERACIÓN 12: Resumen general")

try:
    print(sistema.mostrar_resumen())

except Exception as error:
    print("Error inesperado:", error)

print("\n" + "=" * 55)
print("FINALIZARON LAS PRUEBAS DEL SISTEMA")
print("SOFTWARE FJ CONTINÚA FUNCIONANDO")
print("=" * 55)
