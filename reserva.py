
"""
Proyecto: Software FJ
Archivo: reserva.py
Descripción: Gestiona las reservas realizadas por los clientes
para los diferentes servicios de Software FJ.
"""

# Importamos las clases necesarias.
from entidad import Entidad
from cliente import Cliente
from servicio import Servicio
from decimal import Decimal, InvalidOperation

# Importamos las excepciones personalizadas.
from excepciones import (
    ValidacionError,
    DisponibilidadError,
    ReservaError,
    EstadoReservaError
)


class Reserva(Entidad):
    """
    Representa una reserva realizada por un cliente
    para utilizar un servicio de Software FJ.
    """

    def __init__(self, cliente, servicio, duracion, **parametros):
        """Inicializa una reserva pendiente de confirmación."""

        super().__init__()

        # Validamos que exista un cliente válido.
        if not isinstance(cliente, Cliente):
            raise ValidacionError("Debe proporcionar un cliente válido.")

        # Validamos que exista un servicio válido.
        if not isinstance(servicio, Servicio):
            raise ValidacionError("Debe proporcionar un servicio válido.")

        # Comprobamos que el cliente esté activo.
        if not cliente.activo:
            raise ValidacionError("El cliente se encuentra inactivo.")

        # Comprobamos que el servicio esté disponible.
        if not servicio.disponible:
            raise DisponibilidadError("El servicio no está disponible.")

        # Validamos la duración.
        try:
            duracion = Decimal(str(duracion))
        except (InvalidOperation, ValueError, TypeError) as error:
            raise ValidacionError("La duración debe ser numérica.") from error

        if not duracion.is_finite() or duracion <= 0:
            raise ValidacionError("La duración debe ser mayor que cero.")

        # Validamos los parámetros específicos del servicio.
        try:
            servicio.validar_parametros(duracion, **parametros)
        except ValueError as error:
            raise ValidacionError(
                "No se pudieron validar los parámetros de la reserva."
            ) from error

        # Almacenamos los datos de la reserva.
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__parametros = parametros.copy()

        # Toda reserva comienza en estado pendiente.
        self.__estado = "Pendiente"

        # Almacenamos el costo una vez procesada.
        self.__costo = None

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.__estado != "Pendiente":
            raise EstadoReservaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        if not self.__cliente.activo:
            raise ValidacionError("El cliente está inactivo.")

        if not self.__servicio.disponible:
            raise DisponibilidadError("El servicio ya no está disponible.")

        # Volvemos a validar los parámetros antes de confirmar.
        try:
            self.__servicio.validar_parametros(
                self.__duracion,
                **self.__parametros
            )
        except ValueError as error:
            raise ReservaError(
                "No se pudo confirmar la reserva."
            ) from error

        self.__estado = "Confirmada"

        return "Reserva confirmada correctamente."

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.__estado not in ("Pendiente", "Confirmada"):
            raise EstadoReservaError(
                "No se puede cancelar una reserva procesada o cancelada."
            )

        self.__estado = "Cancelada"

        return "Reserva cancelada correctamente."

    def procesar(self, impuesto=0, descuento=0):
        """
        Procesa una reserva confirmada y calcula su costo.
        """

        if self.__estado != "Confirmada":
            raise EstadoReservaError(
                "La reserva debe estar confirmada para procesarse."
            )

        if not self.__cliente.activo:
            raise ValidacionError("El cliente está inactivo.")

        if not self.__servicio.disponible:
            raise DisponibilidadError("El servicio no está disponible.")

        try:
            costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto=impuesto,
                descuento=descuento,
                **self.__parametros
            )

            if not costo.is_finite() or costo < 0:
                raise ReservaError("El cálculo del costo no es válido.")

            self.__costo = costo
            self.__estado = "Procesada"

            return costo

        except ReservaError:
            raise

        except (ValueError, TypeError, ArithmeticError) as error:
            raise ReservaError(
                "Ocurrió un error durante el procesamiento de la reserva."
            ) from error

    def describir(self):
        """Devuelve la información general de la reserva."""

        return (
            f"Reserva ID: {self.id}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion} horas\n"
            f"Estado: {self.__estado}\n"
            f"Costo: {self.__costo if self.__costo is not None else 'Pendiente'}"
        )
