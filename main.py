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

def buscar_pais(paises, nombre):
    for pais in paises:
        if pais["nombre"].strip().lower() == nombre.strip().lower():
            return pais
    return None

def validar_pais(nombre):
    while True:
        try:    
            if nombre == "":
                print()
                raise ValueError("El nombre no puede estar vacío.")
            
            if not nombre.replace(" ", "").isalpha():
                print()
                raise ValueError("El nombre debe contener solo letras.")
            
            return nombre.strip()
        
        except ValueError as e:
            print("Error:", e)     

def validar_entero(mensaje, minimo=1):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < minimo:
                print(f"Error: El número debe ser mayor o igual a {minimo}.")
            
            return numero
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Error: Por favor, ingrese un número válido.")
            else:
                print(f"Error: {e}")

