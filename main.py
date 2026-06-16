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

def validar_texto(mensaje):
    while True:
        nombre = input(mensaje).strip().title()
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

def validar_continente():
    continentes_validos = ["Africa", "America", "Asia", "Europa", "Oceania"]
    while True:
        continente = input("Ingrese el continente del país: ").strip().capitalize()
        try:
            if continente not in continentes_validos:
                print()
                raise ValueError(f"El continente debe ser uno de los siguientes: {', '.join(continentes_validos)}.")
            return continente
        except ValueError as e:
            print("Error:", e)

def validar_entero(mensaje, minimo=1):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < minimo:
                raise ValueError(f"Error: El número debe ser mayor o igual a {minimo}.")
            
            return numero
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Error: Por favor, ingrese un número válido.")
            else:
                print(f"Error: {e}")


def agregar_pais(paises):
    print("\n---- Agregar un nuevo país ----")
    nombre = validar_texto("Ingrese el nombre del país: ")
    if buscar_pais(paises, nombre):
        print("Error: El país ya existe en la lista.")
        return
    poblacion = validar_entero("Ingrese la población del país: ",1)
    superficie = validar_entero("Ingrese la superficie del país (en km²): ",1)
    continente = validar_continente()

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(pais)
    print("País agregado exitosamente.")

def actualizar_pais(paises):
    print("\n---- Actualizar población y superficie de un país existente ----")
    nombre = validar_texto("Ingrese el nombre del país a actualizar: ")
    pais = buscar_pais(paises, nombre)
    if pais is None:
        print("Error: El país no se encuentra en la lista.")
        return
    
    mostrar_paises([pais])
    
    poblacion = validar_entero("Ingrese la nueva población del país: ",1)
    superficie = validar_entero("Ingrese la nueva superficie del país (en km²): ",1)
    
    pais["poblacion"] = poblacion
    pais["superficie"] = superficie
    
    print("País actualizado exitosamente.")


def buscar_pais_por_nombre(paises):
    print("\n---- Buscar un país por nombre ----")
    nombre = validar_texto("Ingrese el nombre del país a buscar: ")
    
    encontrados = []
    
    for pais in paises:
        if nombre in pais["nombre"].strip().title():
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print("No se encontraron países que coincidan con la búsqueda.")
    else:
        print(f"Se encontraron {len(encontrados)} país(es) que coinciden con la búsqueda:")
        for pais in encontrados:
            mostrar_paises([pais])

def filtrar_paises(paises):
    print("\n--- FILTROS ---")
    print("1. Filtrar por continente")
    print("2. Filtrar por población")
    print("3. Filtrar por superficie")
    
    opcion = input("Seleccione una opción de filtro (1-3): ").strip()
    while opcion not in ["1", "2", "3"]:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 3.")
        opcion = input("Seleccione una opción de filtro (1-3): ").strip()
        
    if opcion == "1":
        filtrar_por_continente(paises)
    elif opcion == "2":
        filtrar_por_poblacion(paises)
    elif opcion == "3":
        filtrar_por_superficie(paises)
        
def filtrar_por_continente(paises):
    continente = validar_continente()
    paises_filtrados = [pais for pais in paises if pais["continente"] == continente]
    
    if len(paises_filtrados) == 0:
        print(f"No se encontraron países en el continente {continente}.")
    else:
        print(f"Países en el continente {continente}:")
        mostrar_paises(paises_filtrados)

def filtrar_por_poblacion(paises):
    poblacion_minima = validar_entero("Ingrese la población mínima: ",1)
    poblacion_maxima = validar_entero("Ingrese la población máxima: ",1)
    
    while poblacion_minima > poblacion_maxima:
        print("Error: La población mínima no puede ser mayor que la población máxima.")
        poblacion_minima = validar_entero("Ingrese la población mínima: ",1)
        poblacion_maxima = validar_entero("Ingrese la población máxima: ",1)
    
    encontrados = []
    for pais in paises:
        if poblacion_minima <= pais["poblacion"] <= poblacion_maxima:
            encontrados.append(pais)
    
    
    if len(encontrados) == 0:
        print("No se encontraron países dentro del rango de población especificado.")
    else:
        print(f"Se encontraron {len(encontrados)} país(es) dentro del rango de población especificado:")
        mostrar_paises(encontrados)
    

def filtrar_por_superficie(paises): 
    superficie_minima = validar_entero("Ingrese la superficie mínima (en km²): ",1)
    superficie_maxima = validar_entero("Ingrese la superficie máxima (en km²): ",1)
    
    while superficie_minima > superficie_maxima:
        print("Error: La superficie mínima no puede ser mayor que la superficie máxima.")
        superficie_minima = validar_entero("Ingrese la superficie mínima (en km²): ", 1)
        superficie_maxima = validar_entero("Ingrese la superficie máxima (en km²): ", 1)
    
    
    encontrados = []
    for pais in paises:
        if superficie_minima <= pais["superficie"] <= superficie_maxima:
            encontrados.append(pais)
    
    if len(encontrados) == 0:
        print("No se encontraron países dentro del rango de superficie especificado.")
    else:
        print(f"Se encontraron {len(encontrados)} país(es) dentro del rango de superficie especificado:")
        mostrar_paises(encontrados)

def ordenar_paises(paises):
    print("\n--- ORDENAR PAÍSES ---")
    print("1. Ordenar por nombre (A-Z)")
    print("2. Ordenar por población (menor a mayor)")
    print("3. Ordenar por población (mayor a menor)")
    print("4. Ordenar por superficie (menor a mayor)")
    print("5. Ordenar por superficie (mayor a menor)")
    
    opcion = input("Seleccione una opción de ordenamiento (1-5): ").strip()
    while opcion not in ["1", "2", "3", "4", "5"]:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")
        opcion = input("Seleccione una opción de ordenamiento (1-5): ").strip()
    
    if opcion == "1":
        paises_ordenados = sorted(paises, key=lambda x: x["nombre"])
        print("Países ordenados por nombre (A-Z):")
        mostrar_paises(paises_ordenados)
    
    elif opcion == "2":
        paises_ordenados = sorted(paises, key=lambda x: x["poblacion"])
        print("Países ordenados por población (menor a mayor):")
        mostrar_paises(paises_ordenados)
    
    elif opcion == "3":
        paises_ordenados = sorted(paises, key=lambda x: x["poblacion"], reverse=True)
        print("Países ordenados por población (mayor a menor):")
        mostrar_paises(paises_ordenados)
    
    elif opcion == "4":
        paises_ordenados = sorted(paises, key=lambda x: x["superficie"])
        print("Países ordenados por superficie (menor a mayor):")
        mostrar_paises(paises_ordenados)
    
    elif opcion == "5":
        paises_ordenados = sorted(paises, key=lambda x: x["superficie"], reverse=True)
        print("Países ordenados por superficie (mayor a menor):")
        mostrar_paises(paises_ordenados)
    
def mostrar_estadisticas(paises):
    print("\n--- ESTADÍSTICAS ---")
    
    pais_mas_poblado = max(paises, key=lambda x: x["poblacion"])
    pais_menos_poblado = min(paises, key=lambda x: x["poblacion"])
    promedio_poblacion = sum(pais["poblacion"] for pais in paises) / len(paises)
    promedio_superficie = sum(pais["superficie"] for pais in paises) / len(paises)
    
    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1
    
    print(f"País más poblado: {pais_mas_poblado['nombre']} con {pais_mas_poblado['poblacion']} habitantes.")
    print(f"País menos poblado: {pais_menos_poblado['nombre']} con {pais_menos_poblado['poblacion']} habitantes.")
    print(f"Promedio de población: {promedio_poblacion:.2f} habitantes.")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km².")
    print("Número de países por continente:")
    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad} país(es)")
        

def guardar_paises(nombre_archivo, paises):
    try:
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
        print("Datos guardados exitosamente en 'paises.csv'.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
        
def menu():
    while True:
        try:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Mostrar todos los países")
            print("2. Agregar un nuevo país")
            print("3. Actualizar población y superficie de un país existente")
            print("4. Buscar un país por nombre")
            print("5. Filtrar países")
            print("6. Ordenar países")
            print("7. Mostrar estadísticas")
            print("8. Guardar y salir")
            
            opcion = input("Seleccione una opción (1-8): \n").strip()
            if opcion not in [str(i) for i in range(1, 9)]:
                raise ValueError("Opción no válida. Por favor, seleccione una opción entre 1 y 8.")
            return opcion
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Error: Debe ingresar un número.")
            else:
                print("Error:", e)
    
def main():
    paises = cargar_paises("paises.csv")
    while True:
        opcion = menu()
        if opcion == "1":
            mostrar_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais_por_nombre(paises)
        elif opcion == "5":
            filtrar_paises(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
        elif opcion == "8":
            guardar_paises("paises.csv", paises)
            print("Datos guardados exitosamente. Saliendo del programa.")
            break
            
if __name__ == "__main__":
    main()