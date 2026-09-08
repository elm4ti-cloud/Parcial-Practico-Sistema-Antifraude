# Parcial — Detector de Transmisiones Sospechosas

Nombre:  Matias Villero

## 1. ¿Qué debe hacer el programa?

el programa debe registrar y analizar transacciones para determinar si son sospechosas, cada transacción tendrá un puntaje para clasificarla

---

## 2. Clase `Transmision`

La clase tendrá los siguientes atributos:

- `id`: identificador de las transacciones
- `origen`: persona, usuario o lugar desde donde se envia la transaccion
- `mensaje`: contenido que se va a analizar
- `puntaje`: valor del mensaje
- `clasificacion`: categoria asignada a la transacción

Escriba brevemente qué representa cada uno.

---

## 3. Métodos

### `analizar()`

Responsabilidad: analiza el contenido del mensaje, aplica las reglas y calcula el puntaje de riesgo

### `clasificar()`

Responsabilidad: analiza y retorna la clasificacion de la transacción

### `to_dict()`

Responsabilidad: convierte el objeto Transaccion a diccionario para alamcenarlo en un JSON

### `from_dict()`
 
Responsabilidad: recibe el diccionario del JSON y convertirlo nuevamente en un objeto

---

## 4. Algoritmo de análisis

Complete el siguiente pseudocódigo:

```text
puntaje = 0

SI el mensaje contiene un dispositivo desconocido
    sumar 30 puntos

SI el mensaje contiene un pais distinto a Colombia
    sumar 25 puntos

SI el mensaje contiene un hora entre 0 y 5
    sumar 20 puntos

SI el mensaje contiene un valor mayor a 2000000
    sumar 30 puntos
```

---

## 5. Persistencia

Explique brevemente qué ocurre al iniciar el programa:
se lee el JSON
los datos se convierten en diccionarios y luego cada diccionario se convierte en un objeto

```text
JSON
 ↓
____________________
 ↓
____________________
```

Explique qué ocurre al guardar:
los objetos se convierten en diccionarios por to_dict() y posteriormente se guardan en el JSON

```text
Objetos
 ↓
____________________
 ↓
JSON
```

---

## 6. Menú

Indique qué debe hacer cada opción:

### Opción 1 — Registrar transmisión

1.  solicitar los datos de la transacción al usuario
2.  crea el objeto transacción y analiza el mensaje
3.  agrega la transacción a la lista y guarda la información en el JSON

### Opción 2 — Listar transmisiones

1.  mostrar todas las transacciones
2.  mostrar: id, origen, mensaje, puntaje y clasificación

### Opción 3 — Salir

Acción: finaliza el programa

---

## Nota

Este archivo debe completarse durante los primeros 15 minutos del parcial, antes de comenzar la implementación.