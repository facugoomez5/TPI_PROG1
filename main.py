import csv

def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                paises.append(pais)
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'paises.csv'")
    except ValueError as e:
        print(f"Error al convertir datos: {e}")
    return paises

def mostrar_paises(paises):
    for pais in paises:
        print(
            f"Nombre: {pais['nombre']} | "
            f"Población: {pais['poblacion']} | "
            f"Superficie: {pais['superficie']} km² | "
            f"Continente: {pais['continente']}"
        )

paises = cargar_paises("paises.csv")
mostrar_paises(paises)