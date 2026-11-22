
# SOFTWARE FJ
## Sistema Integral de Gestión de Clientes, Servicios y Reservas

### 1. Descripción del proyecto

Software FJ es una aplicación desarrollada en Python que permite gestionar clientes, servicios y reservas mediante programación orientada a objetos.

El sistema ofrece tres tipos de servicios:

- Reservas de salas.
- Alquiler de equipos.
- Asesorías especializadas.

La aplicación no utiliza bases de datos. La información se administra mediante objetos y listas internas. Los archivos se utilizan para registrar eventos y errores.

### 2. Objetivo general

Desarrollar un sistema integral, modular y estable que permita administrar clientes, servicios y reservas, aplicando los principios de programación orientada a objetos y el manejo avanzado de excepciones.

### 3. Tecnologías utilizadas

- Lenguaje: Python.
- Editor: Visual Studio Code.
- Control de versiones: Git.
- Repositorio: GitHub.
- Almacenamiento temporal: listas y objetos.
- Registro de eventos: archivos de logs.

### 4. Estructura del proyecto

```text
SOFTWARE_FJ/
│
├── main.py
├── entidad.py
├── cliente.py
├── servicio.py
├── reserva.py
├── excepciones.py
├── sistema.py
├── pruebas_excepciones.py
├── logs/
│   └── sistema.log
├── .gitignore
└── README.md
```

### 5. Descripción de las clases

**Entidad:** clase abstracta que establece las características generales de las entidades.

**Cliente:** permite registrar clientes y validar sus datos personales.

**Servicio:** clase abstracta que define las características generales de los servicios.

**ReservaSala:** administra el servicio de reserva de salas.

**AlquilerEquipo:** administra el alquiler de equipos tecnológicos.

**AsesoriaEspecializada:** administra las asesorías profesionales.

**Reserva:** relaciona un cliente con un servicio y administra el estado de las reservas.

**SistemaGestion:** centraliza el registro y administración de clientes, servicios y reservas mediante listas internas.

### 6. Principios de programación orientada a objetos

El proyecto implementa:

- Abstracción mediante las clases Entidad y Servicio.
- Herencia mediante Cliente y los servicios especializados.
- Polimorfismo mediante los métodos sobrescritos de cada servicio.
- Encapsulación mediante atributos privados y propiedades.
- Parámetros opcionales para calcular costos con impuestos y descuentos.

### 7. Manejo de excepciones

El sistema incorpora excepciones personalizadas:

- SoftwareFJError.
- ValidacionError.
- DisponibilidadError.
- ReservaError.
- EstadoReservaError.

También implementa:

- try/except.
- try/except/else.
- try/except/finally.
- Encadenamiento de excepciones.
- Registro de errores mediante logging.

### 8. Instalación y ejecución

1. Instalar Python.
2. Abrir la carpeta SOFTWARE_FJ en Visual Studio Code.
3. Activar el entorno virtual, si se utiliza.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

Para ejecutar las pruebas de excepciones:

```bash
python pruebas_excepciones.py
```

### 9. Registro de eventos y errores

Los eventos y errores se almacenan en:

`logs/sistema.log`

El sistema utiliza el módulo logging de Python.

### 10. Pruebas realizadas

Se realizaron pruebas de:

- Registro válido e inválido de clientes.
- Detección de clientes duplicados.
- Creación de servicios especializados.
- Detección de servicios duplicados.
- Creación de reservas.
- Confirmación y cancelación de reservas.
- Procesamiento y cálculo de costos.
- Validación de parámetros incorrectos.
- Manejo de excepciones.
- Registro de errores y eventos.

### 11. Restricciones del sistema

El proyecto no utiliza motores de bases de datos. La información se gestiona mediante objetos y listas internas.

Los archivos se utilizan únicamente para el registro de eventos y errores.

### 12. Conclusión

El proyecto Software FJ integra los fundamentos de programación orientada a objetos y manejo avanzado de excepciones en una aplicación modular.

Su estructura permite administrar clientes, servicios y reservas, controlar errores y mantener la continuidad de las operaciones.
