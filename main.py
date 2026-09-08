import json
import os

class Transaccion:

    def __init__(self, id, titular, valor, hora, pais, dispositivo_conocido):

        if not titular or titular.strip() == "":
            raise ValueError("El titular no puede estar vacío.")

        if valor <= 0:
            raise ValueError("El valor debe ser mayor que cero.")

        if hora < 0 or hora > 23:
            raise ValueError("La hora debe estar entre 0 y 23.")

        if not pais or pais.strip() == "":
            raise ValueError("El país no puede estar vacío.")

        if not isinstance(dispositivo_conocido, bool):
            raise ValueError(
                "dispositivo_conocido debe ser True o False."
            )

        self.id = id
        self.titular = titular
        self.valor = valor
        self.hora = hora
        self.pais = pais
        self.dispositivo_conocido = dispositivo_conocido

        self.puntaje_riesgo = self.calcular_riesgo()
        self.clasificacion = self.clasificar()

    def calcular_riesgo(self):
        puntaje = 0

        if self.valor >= 2000000:
            puntaje += 30

        if 0 <= self.hora <= 5:
            puntaje += 20

        if self.pais.strip().lower() != "colombia":
            puntaje += 25

        if self.dispositivo_conocido is False:
            puntaje += 30

        return puntaje

    def clasificar(self):
        if self.puntaje_riesgo <= 29:
            return "NORMAL"
        elif self.puntaje_riesgo <= 59:
            return "SOSPECHOSA"
        else:
            return "ALTO RIESGO"

    def to_dict(self):
        return {
            "id": self.id,
            "titular": self.titular,
            "valor": self.valor,
            "hora": self.hora,
            "pais": self.pais,
            "dispositivo_conocido": self.dispositivo_conocido,
            "puntaje_riesgo": self.puntaje_riesgo,
            "clasificacion": self.clasificacion
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["id"],
            datos["datos"],
            datos["titular"],
            datos["valor"],
            datos["hora"],
            datos["pais"],
            datos["dispositivo_conocido"]
        )


ARCHIVO = "transacciones.json"


def cargar_transacciones():
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            transacciones = []
            for dato in datos:
                transaccion = Transaccion.from_dict(dato)
                transacciones.append(transaccion)
            return transacciones

        except (json.JSONDecodeError, KeyError, ValueError):
            print("El archivo JSON contiene datos inválidos.")
            return []
    return []


def guardar_transacciones(transacciones):
    datos = []
    for transaccion in transacciones:
        datos.append(transaccion.to_dict())

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(
            datos,
            archivo,
            ensure_ascii=False,
            indent=4
        )


def ejecutar_casos_prueba(transacciones):
    print("\n=== EJECUTANDO CASOS DE PRUEBA OBLIGATORIOS ===")
    
    casos = [
        {"id": 1, "titular": "Laura Gómez", "valor": 3500000, "hora": 2, "pais": "Colombia", "dispositivo_conocido": False},
        {"id": 2, "titular": "Carlos Pérez", "valor": 500000, "hora": 14, "pais": "Colombia", "dispositivo_conocido": True},
        {"id": 3, "titular": "Ana Torres", "valor": 2500000, "hora": 10, "pais": "Perú", "dispositivo_conocido": True}
    ]
    
    for datos in casos:
        try:
            t = Transaccion(
                datos["id"],
                datos["titular"],
                datos["valor"],
                datos["hora"],
                datos["pais"],
                datos["dispositivo_conocido"]
            )
            transacciones.append(t)
            
            print("-----------------------------------")
            print("ID:", t.id)
            print("Titular:", t.titular)
            print("Puntaje de riesgo:", t.puntaje_riesgo)
            print("Clasificación:", t.clasificacion)
            
        except ValueError as error:
            print(f"Error al crear caso de prueba {datos['id']}: {error}")
            
    guardar_transacciones(transacciones)
    print("===============================================\n")


def registrar_transaccion(transacciones):
    print("\n--- REGISTRAR TRANSACCIÓN ---")
    try:
        id = int(input("ID: "))
        titular = input("Titular: ")
        valor = float(input("Valor: "))
        hora = int(input("Hora (0-23): "))
        pais = input("País: ")
        dispositivo = input(
            "¿El dispositivo es conocido? (True/False): "
        )

        if dispositivo.lower() == "true":
            dispositivo_conocido = True
        elif dispositivo.lower() == "false":
            dispositivo_conocido = False
        else:
            print("Error: debe escribir True o False.")
            return

        transaccion = Transaccion(
            id,
            titular,
            valor,
            hora,
            pais,
            dispositivo_conocido
        )

        transacciones.append(transaccion)
        guardar_transacciones(transacciones)

        print("\nTransacción registrada correctamente.")
        print("Puntaje:", transaccion.puntaje_riesgo)
        print("Clasificación:", transaccion.clasificacion)

    except ValueError as error:
        print("\nError:", error)


def listar_transacciones(transacciones):
    print("\n--- LISTA DE TRANSACCIONES ---")
    if len(transacciones) == 0:
        print("No hay transacciones registradas.")
        return

    for transaccion in transacciones:
        print("-----------------------------------")
        print("ID:", transaccion.id)
        print("Titular:", transaccion.titular)
        print("Valor:", transaccion.valor)
        print("Hora:", transaccion.hora)
        print("País:", transaccion.pais)
        print(
            "Dispositivo conocido:",
            transaccion.dispositivo_conocido
        )
        print("Puntaje:", transaccion.puntaje_riesgo)
        print("Clasificación:", transaccion.clasificacion)


def menu():
    transacciones = cargar_transacciones()

    if len(transacciones) == 0:
        ejecutar_casos_prueba(transacciones)

    while True:
        print("\n==============================")
        print(" DETECTOR DE TRANSACCIONES")
        print("==============================")
        print("1. Registrar transacción")
        print("2. Listar transacciones")
        print("3. Salir")
        print("==============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_transaccion(transacciones)
        elif opcion == "2":
            listar_transacciones(transacciones)
        elif opcion == "3":
            guardar_transacciones(transacciones)
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
