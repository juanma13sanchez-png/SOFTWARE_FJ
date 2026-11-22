
"""
Proyecto: Software FJ
Archivo: entidad.py
Descripción: Define la clase abstracta Entidad,
base para las demás clases del sistema.
"""

# Importamos ABC y abstractmethod para trabajar con abstracción.
from abc import ABC, abstractmethod

# Importamos datetime para registrar la fecha de creación.
from datetime import datetime

# Importamos uuid para generar identificadores únicos.
import uuid


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del sistema Software FJ.
    """

    def __init__(self):
        """Inicializa los atributos generales de una entidad."""

        # Atributos privados para aplicar encapsulación.
        self.__id = str(uuid.uuid4())
        self.__fecha_creacion = datetime.now()
        self.__activo = True

    @property
    def id(self):
        """Permite consultar el identificador de la entidad."""
        return self.__id

    @property
    def fecha_creacion(self):
        """Permite consultar la fecha de creación."""
        return self.__fecha_creacion

    @property
    def activo(self):
        """Permite consultar si la entidad está activa."""
        return self.__activo

    def desactivar(self):
        """Desactiva una entidad del sistema."""

        if not self.__activo:
            raise ValueError("La entidad ya se encuentra desactivada.")

        self.__activo = False

    def activar(self):
        """Activa nuevamente una entidad."""

        if self.__activo:
            raise ValueError("La entidad ya se encuentra activa.")

        self.__activo = True

    @abstractmethod
    def describir(self):
        """
        Método abstracto que deberán implementar
        todas las clases que hereden de Entidad.
        """
        pass
