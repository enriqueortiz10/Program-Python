# Matriz de la videoteca: [Título, Año de Lanzamiento, Calificación, Género]
videoteca = [
    ["Inception", 2010, 8.8, "Ciencia Ficción"],
    ["Avatar", 2009, 7.9, "Acción"],
    ["Interstellar", 2014, 8.6, "Ciencia Ficción"],
    ["Joker", 2019, 8.4, "Drama"],
    ["Parasite", 2019, 8.5, "Suspenso"],
    ["Dune", 2021, 8.1, "Ciencia Ficción"],
    ["Top Gun: Maverick", 2022, 8.3, "Acción"]
]

# Función para contar títulos que cumplen los criterios
def contar_titulos(matriz, calificacion_minima, año_limite):
    contador = 0

    for titulo in matriz:
        año = titulo[1]
        calificacion = titulo[2]

        if calificacion >= calificacion_minima and año >= año_limite:
            contador += 1

    return contador


# Entrada de datos por teclado
calificacion_minima = float(input("Ingrese la calificación mínima: "))
año_limite = int(input("Ingrese el año límite: "))

# Llamado a la función
resultado = contar_titulos(videoteca, calificacion_minima, año_limite)

# Mostrar resultado
print("Cantidad de títulos que cumplen ambos criterios:", resultado)