
"""
Proyecto: Software FJ
Archivo: excepciones.py
Descripción: Define las excepciones personalizadas
para controlar los errores del sistema.
"""


class SoftwareFJError(Exception):
    """Excepción general del sistema Software FJ."""
    pass


class ValidacionError(SoftwareFJError):
    """Se produce cuando un dato no cumple las validaciones."""
    pass


class DisponibilidadError(SoftwareFJError):
    """Se produce cuando un servicio no está disponible."""
    pass


class ReservaError(SoftwareFJError):
    """Se produce cuando ocurre un problema con una reserva."""
    pass


class EstadoReservaError(ReservaError):
    """Se produce cuando una operación no está permitida
    debido al estado actual de la reserva."""
    pass
