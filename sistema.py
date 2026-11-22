
"""
Proyecto: Software FJ
Archivo: sistema.py
Descripción: Administra los clientes, servicios y reservas
mediante listas internas y registra eventos y errores.
"""

# Importamos las herramientas necesarias.
import logging
from pathlib import Path

# Importamos las clases del proyecto.
from cliente import Cliente
from servicio import Servicio
from reserva import Reserva

# Importamos las excepciones personalizadas.
from excepciones import (
    SoftwareFJError,
    ValidacionError,
    ReservaError
)


class SistemaGestion:
    """
    Clase principal que centraliza las operaciones
    del sistema Software FJ.
    """

    def __init__(self):
        """Inicializa las listas y el sistema de registros."""

        # Listas privadas para almacenar los objetos.
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

        # Creamos la carpeta de registros si no existe.
        carpeta_logs = Path(__file__).parent / "logs"
        carpeta_logs.mkdir(exist_ok=True)

        # Configuramos el archivo de eventos y errores.
        self.__logger = logging.getLogger("SoftwareFJ")
        self.__logger.setLevel(logging.INFO)
        self.__logger.propagate = False

        # Evitamos crear varios manejadores del mismo archivo.
        if not self.__logger.handlers:
            archivo_log = carpeta_logs / "sistema.log"

            manejador = logging.FileHandler(
                archivo_log,
                encoding="utf-8"
            )

            formato = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            manejador.setFormatter(formato)
            self.__logger.addHandler(manejador)

        self.__logger.info("Sistema Software FJ iniciado.")

    # ==================================================
    # REGISTRO DE CLIENTES
    # ==================================================

    def registrar_cliente(self, cliente):
        """Registra un cliente después de validar su información."""

        try:
            if not isinstance(cliente, Cliente):
                raise ValidacionError("El objeto proporcionado no es un cliente.")

            # Evitamos documentos duplicados.
            for existente in self.__clientes:
                if existente.documento == cliente.documento:
                    raise ValidacionError(
                        "Ya existe un cliente con ese documento."
                    )

            self.__clientes.append(cliente)

            self.__logger.info(
                "Cliente registrado: %s",
                cliente.documento
            )

            return "Cliente registrado correctamente."

        except SoftwareFJError as error:
            self.__logger.exception("Error al registrar cliente.")
            raise

        except Exception as error:
            self.__logger.exception("Error inesperado al registrar cliente.")
            raise SoftwareFJError(
                "No fue posible registrar el cliente."
            ) from error

    # ==================================================
    # REGISTRO DE SERVICIOS
    # ==================================================

    def registrar_servicio(self, servicio):
        """Registra un servicio en el sistema."""

        try:
            if not isinstance(servicio, Servicio):
                raise ValidacionError("El objeto proporcionado no es un servicio.")

            for existente in self.__servicios:
                if existente.nombre.casefold() == servicio.nombre.casefold():
                    raise ValidacionError(
                        "Ya existe un servicio con ese nombre."
                    )

            self.__servicios.append(servicio)

            self.__logger.info(
                "Servicio registrado: %s",
                servicio.nombre
            )

            return "Servicio registrado correctamente."

        except SoftwareFJError:
            self.__logger.exception("Error al registrar servicio.")
            raise

        except Exception as error:
            self.__logger.exception("Error inesperado al registrar servicio.")
            raise SoftwareFJError(
                "No fue posible registrar el servicio."
            ) from error

    # ==================================================
    # CREACIÓN DE RESERVAS
    # ==================================================

    def crear_reserva(self, cliente, servicio, duracion, **parametros):
        """Crea y almacena una nueva reserva."""

        try:
            # Verificamos que el cliente esté registrado.
            if cliente not in self.__clientes:
                raise ValidacionError(
                    "El cliente no está registrado en el sistema."
                )

            # Verificamos que el servicio esté registrado.
            if servicio not in self.__servicios:
                raise ValidacionError(
                    "El servicio no está registrado en el sistema."
                )

            # Creamos el objeto reserva.
            nueva_reserva = Reserva(
                cliente,
                servicio,
                duracion,
                **parametros
            )

            self.__reservas.append(nueva_reserva)

            self.__logger.info(
                "Reserva creada: %s",
                nueva_reserva.id
            )

            return nueva_reserva

        except SoftwareFJError:
            self.__logger.exception("Error al crear reserva.")
            raise

        except Exception as error:
            self.__logger.exception("Error inesperado al crear reserva.")
            raise ReservaError(
                "No fue posible crear la reserva."
            ) from error

    # ==================================================
    # CONFIRMAR RESERVAS
    # ==================================================

    def confirmar_reserva(self, identificador):
        """Confirma una reserva mediante su identificador."""

        try:
            reserva = self.__buscar_reserva(identificador)

            resultado = reserva.confirmar()

            self.__logger.info(
                "Reserva confirmada: %s",
                identificador
            )

            return resultado

        except SoftwareFJError:
            self.__logger.exception("Error al confirmar reserva.")
            raise

        except Exception as error:
            self.__logger.exception("Error inesperado al confirmar reserva.")
            raise ReservaError(
                "No fue posible confirmar la reserva."
            ) from error

    # ==================================================
    # CANCELAR RESERVAS
    # ==================================================

    def cancelar_reserva(self, identificador):
        """Cancela una reserva existente."""

        try:
            reserva = self.__buscar_reserva(identificador)

            resultado = reserva.cancelar()

            self.__logger.info(
                "Reserva cancelada: %s",
                identificador
            )

            return resultado

        except SoftwareFJError:
            self.__logger.exception("Error al cancelar reserva.")
            raise

        except Exception as error:
            self.__logger.exception("Error inesperado al cancelar reserva.")
            raise ReservaError(
                "No fue posible cancelar la reserva."
            ) from error

    # ==================================================
    # PROCESAR RESERVAS
    # ==================================================

    def procesar_reserva(self, identificador, impuesto=0, descuento=0):
        """Procesa una reserva y calcula su costo."""

        try:
            reserva = self.__buscar_reserva(identificador)

            costo = reserva.procesar(
                impuesto=impuesto,
                descuento=descuento
            )

            self.__logger.info(
                "Reserva procesada: %s | Costo: %s",
                identificador,
                costo
            )

            return costo

        except SoftwareFJError:
            self.__logger.exception("Error al procesar reserva.")
            raise

        except Exception as error:
            self.__logger.exception("Error inesperado al procesar reserva.")
            raise ReservaError(
                "No fue posible procesar la reserva."
            ) from error

    # ==================================================
    # BÚSQUEDA DE RESERVAS
    # ==================================================

    def __buscar_reserva(self, identificador):
        """Busca una reserva mediante su identificador."""

        if not isinstance(identificador, str) or not identificador.strip():
            raise ValidacionError("El identificador de reserva es obligatorio.")

        for reserva in self.__reservas:
            if reserva.id == identificador:
                return reserva

        raise ReservaError("No se encontró la reserva solicitada.")

    # ==================================================
    # CONSULTAS DEL SISTEMA
    # ==================================================

    def listar_clientes(self):
        """Devuelve una copia de la lista de clientes."""
        return tuple(self.__clientes)

    def listar_servicios(self):
        """Devuelve una copia de la lista de servicios."""
        return tuple(self.__servicios)

    def listar_reservas(self):
        """Devuelve una copia de la lista de reservas."""
        return tuple(self.__reservas)

    def mostrar_resumen(self):
        """Muestra las cantidades de registros del sistema."""

        resumen = (
            f"CLIENTES REGISTRADOS: {len(self.__clientes)}\n"
            f"SERVICIOS REGISTRADOS: {len(self.__servicios)}\n"
            f"RESERVAS REGISTRADAS: {len(self.__reservas)}"
        )

        self.__logger.info("Consulta del resumen general.")

        return resumen

    