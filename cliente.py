
"""
Proyecto: Software FJ
Archivo: cliente.py
Descripción: Define la clase Cliente para registrar,
validar y administrar la información de los clientes.
"""

# Importamos la clase abstracta Entidad.
from entidad import Entidad

# Importamos expresiones regulares para validar los datos.
import re


class Cliente(Entidad):
    """
    Representa a un cliente registrado en Software FJ.
    Hereda los atributos y métodos de Entidad.
    """

    def __init__(self, nombre, documento, correo, telefono):
        """
        Inicializa un cliente después de validar sus datos.
        """

        # Ejecutamos el constructor de la clase padre.
        super().__init__()

        # Validamos los datos antes de almacenarlos.
        self.__nombre = self.__validar_nombre(nombre)
        self.__documento = self.__validar_documento(documento)
        self.__correo = self.__validar_correo(correo)
        self.__telefono = self.__validar_telefono(telefono)

    def __validar_nombre(self, nombre):
        """Comprueba que el nombre sea válido."""

        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser texto.")

        nombre = nombre.strip()

        if len(nombre) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")

        if not re.fullmatch(r"[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s'-]+", nombre):
            raise ValueError("El nombre contiene caracteres no permitidos.")

        return nombre

    def __validar_documento(self, documento):
        """Comprueba que el documento sea válido."""

        documento = str(documento).strip()

        if not documento.isdigit():
            raise ValueError("El documento debe contener solamente números.")

        if not 5 <= len(documento) <= 15:
            raise ValueError("El documento debe tener entre 5 y 15 dígitos.")

        return documento

    def __validar_correo(self, correo):
        """Comprueba que el correo electrónico tenga un formato válido."""

        if not isinstance(correo, str):
            raise ValueError("El correo debe ser texto.")

        correo = correo.strip().lower()

        patron = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"

        if not re.fullmatch(patron, correo):
            raise ValueError("El correo electrónico no tiene un formato válido.")

        return correo

    def __validar_telefono(self, telefono):
        """Comprueba que el teléfono tenga un formato válido."""

        if not isinstance(telefono, str):
            telefono = str(telefono)

        telefono = telefono.strip()

        # Permitimos números, espacios, signo + y guiones.
        if not re.fullmatch(r"\+?[0-9\s-]+", telefono):
            raise ValueError("El teléfono contiene caracteres no permitidos.")

        # Comprobamos que tenga entre 7 y 15 dígitos.
        cantidad_digitos = sum(caracter.isdigit() for caracter in telefono)

        if not 7 <= cantidad_digitos <= 15:
            raise ValueError("El teléfono debe tener entre 7 y 15 dígitos.")

        return telefono

    # Propiedades para consultar los datos encapsulados.

    @property
    def nombre(self):
        """Devuelve el nombre del cliente."""
        return self.__nombre

    @property
    def documento(self):
        """Devuelve el documento del cliente."""
        return self.__documento

    @property
    def correo(self):
        """Devuelve el correo del cliente."""
        return self.__correo

    @property
    def telefono(self):
        """Devuelve el teléfono del cliente."""
        return self.__telefono

    def describir(self):
        """Implementa el método abstracto heredado de Entidad."""

        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono} | "
            f"ID: {self.id}"
        )
