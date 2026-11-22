from entidad import Entidad

try:
    entidad = Entidad()

except TypeError as error:
    print("Prueba exitosa: no se puede crear una entidad abstracta.")
    print("Detalle del error:", error)
    