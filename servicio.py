
"""
Proyecto: Software FJ
Archivo: servicio.py
Descripción: Define la clase abstracta Servicio y sus
tres servicios especializados.
"""

from entidad import Entidad
from abc import abstractmethod
from decimal import Decimal, InvalidOperation


class Servicio(Entidad):
    """
    Clase abstracta que representa un servicio general.
    Todos los servicios deben implementar sus propios
    métodos de cálculo, validación y descripción.
    """

    def __init__(self, nombre, tarifa_base):
        super().__init__()

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        try:
            tarifa = Decimal(str(tarifa_base))
        except (InvalidOperation, ValueError, TypeError) as error:
            raise ValueError("La tarifa debe ser un número válido.") from error

        if not tarifa.is_finite() or tarifa <= 0:
            raise ValueError("La tarifa debe ser mayor que cero.")

        self.__nombre = nombre.strip()
        self.__tarifa_base = tarifa
        self.__disponible = True

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tarifa_base(self):
        return self.__tarifa_base

    @property
    def disponible(self):
        return self.__disponible

    def cambiar_disponibilidad(self, estado):
        """Permite habilitar o deshabilitar un servicio."""

        if not isinstance(estado, bool):
            raise ValueError("La disponibilidad debe ser True o False.")

        self.__disponible = estado

    def _calcular_total(self, subtotal, impuesto=0, descuento=0):
        """
        Calcula el valor final aplicando impuestos y descuentos.
        Los parámetros opcionales permiten distintas variantes
        del cálculo del costo.
        """

        try:
            impuesto = Decimal(str(impuesto))
            descuento = Decimal(str(descuento))
        except (InvalidOperation, ValueError, TypeError) as error:
            raise ValueError("Impuesto o descuento inválido.") from error

        if not impuesto.is_finite() or not descuento.is_finite():
            raise ValueError("Los porcentajes deben ser valores finitos.")

        if not Decimal("0") <= impuesto <= Decimal("100"):
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        if not Decimal("0") <= descuento <= Decimal("100"):
            raise ValueError("El descuento debe estar entre 0 y 100.")

        total_con_descuento = subtotal * (
            Decimal("1") - descuento / Decimal("100")
        )

        total_final = total_con_descuento * (
            Decimal("1") + impuesto / Decimal("100")
        )

        return total_final.quantize(Decimal("0.01"))

    @abstractmethod
    def validar_parametros(self, duracion, **kwargs):
        """Cada servicio debe validar sus propios parámetros."""
        pass

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0, **kwargs):
        """Cada servicio debe implementar su cálculo de costo."""
        pass

    @abstractmethod
    def describir(self):
        """Cada servicio debe proporcionar su descripción."""
        pass


class ReservaSala(Servicio):
    """Servicio especializado en reservas de salas."""

    def __init__(self, nombre, tarifa_hora, capacidad_maxima):
        super().__init__(nombre, tarifa_hora)

        if type(capacidad_maxima) is not int or capacidad_maxima <= 0:
            raise ValueError("La capacidad debe ser un entero positivo.")

        self.__capacidad_maxima = capacidad_maxima

    def validar_parametros(self, duracion, **kwargs):
        asistentes = kwargs.get("asistentes", 1)

        if type(asistentes) is not int or asistentes <= 0:
            raise ValueError("La cantidad de asistentes debe ser positiva.")

        if asistentes > self.__capacidad_maxima:
            raise ValueError("La sala no tiene capacidad suficiente.")

        if not self.disponible:
            raise ValueError("El servicio de sala no está disponible.")

        try:
            horas = Decimal(str(duracion))
        except (InvalidOperation, ValueError, TypeError) as error:
            raise ValueError("La duración debe ser numérica.") from error

        if not horas.is_finite() or horas <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        return horas

    def calcular_costo(self, duracion, impuesto=0, descuento=0, **kwargs):
        horas = self.validar_parametros(duracion, **kwargs)
        subtotal = horas * self.tarifa_base

        return self._calcular_total(subtotal, impuesto, descuento)

    def describir(self):
        return (
            f"Reserva de sala: {self.nombre} | "
            f"Tarifa por hora: ${self.tarifa_base} | "
            f"Capacidad máxima: {self.__capacidad_maxima}"
        )


class AlquilerEquipo(Servicio):
    """Servicio especializado en alquiler de equipos."""

    def __init__(self, nombre, tarifa_hora, unidades_disponibles):
        super().__init__(nombre, tarifa_hora)

        if type(unidades_disponibles) is not int or unidades_disponibles < 0:
            raise ValueError("Las unidades disponibles deben ser un entero no negativo.")

        self.__unidades_disponibles = unidades_disponibles

    def validar_parametros(self, duracion, **kwargs):
        unidades = kwargs.get("unidades", 1)

        if type(unidades) is not int or unidades <= 0:
            raise ValueError("La cantidad de equipos debe ser positiva.")

        if unidades > self.__unidades_disponibles:
            raise ValueError("No hay suficientes equipos disponibles.")

        if not self.disponible:
            raise ValueError("El servicio de alquiler no está disponible.")

        try:
            horas = Decimal(str(duracion))
        except (InvalidOperation, ValueError, TypeError) as error:
            raise ValueError("La duración debe ser numérica.") from error

        if not horas.is_finite() or horas <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        return horas, unidades

    def calcular_costo(self, duracion, impuesto=0, descuento=0, **kwargs):
        horas, unidades = self.validar_parametros(duracion, **kwargs)
        subtotal = horas * self.tarifa_base * unidades

        return self._calcular_total(subtotal, impuesto, descuento)

    def describir(self):
        return (
            f"Alquiler de equipo: {self.nombre} | "
            f"Tarifa por hora: ${self.tarifa_base} | "
            f"Unidades disponibles: {self.__unidades_disponibles}"
        )


class AsesoriaEspecializada(Servicio):
    """Servicio especializado en asesorías profesionales."""

    def __init__(self, nombre, tarifa_hora, especialidad):
        super().__init__(nombre, tarifa_hora)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad es obligatoria.")

        self.__especialidad = especialidad.strip()

    def validar_parametros(self, duracion, **kwargs):
        modalidad = kwargs.get("modalidad", "virtual")

        if modalidad not in ("virtual", "presencial"):
            raise ValueError("La modalidad debe ser virtual o presencial.")

        if not self.disponible:
            raise ValueError("El servicio de asesoría no está disponible.")

        try:
            horas = Decimal(str(duracion))
        except (InvalidOperation, ValueError, TypeError) as error:
            raise ValueError("La duración debe ser numérica.") from error

        if not horas.is_finite() or horas <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        return horas

    def calcular_costo(self, duracion, impuesto=0, descuento=0, **kwargs):
        horas = self.validar_parametros(duracion, **kwargs)
        subtotal = horas * self.tarifa_base

        return self._calcular_total(subtotal, impuesto, descuento)

    def describir(self):
        return (
            f"Asesoría especializada: {self.nombre} | "
            f"Tarifa por hora: ${self.tarifa_base} | "
            f"Especialidad: {self.__especialidad}"
        )
