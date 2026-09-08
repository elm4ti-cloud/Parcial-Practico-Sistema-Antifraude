class Transaccion:

    def __init__(self, id, titular, valor, hora, pais, dispositivo_conocido):

        # Validaciones
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

        # Datos
        self.id = id
        self.titular = titular
        self.valor = valor
        self.hora = hora
        self.pais = pais
        self.dispositivo_conocido = dispositivo_conocido

        # Cálculo automático
        self.puntaje_riesgo = self.calcular_riesgo()
        self.clasificacion = self.clasificar()

    def calcular_riesgo(self):

        puntaje = 0

        # Valor mayor o igual a $2.000.000
        if self.valor >= 2000000:
            puntaje += 30

        # Hora entre 0 y 5
        if 0 <= self.hora <= 5:
            puntaje += 20

        # País diferente de Colombia
        if self.pais.strip().lower() != "colombia":
            puntaje += 25

        # Dispositivo no conocido
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
            datos["titular"],
            datos["valor"],
            datos["hora"],
            datos["pais"],
            datos["dispositivo_conocido"]
        )