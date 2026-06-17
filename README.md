# 🌎 Gestión de Datos de Países en Python

Trabajo Práctico Integrador (TPI) – Programación I

## 📋 Descripción

Este proyecto consiste en una aplicación de consola desarrollada en Python que permite gestionar información sobre países a partir de un archivo CSV.

El sistema permite realizar consultas, filtros, ordenamientos y estadísticas sobre los países almacenados, aplicando los conceptos vistos en la materia Programación I.

---

## 🎯 Objetivos

- Leer información desde archivos CSV.
- Utilizar listas y diccionarios.
- Aplicar funciones modulares.
- Implementar validaciones de datos.
- Realizar búsquedas, filtros y ordenamientos.
- Generar estadísticas básicas.

---

## 📂 Estructura del Proyecto

```
TPI_PROG1/
│
├── main.py
├── paises.csv
├── README.md
```

---

## 📊 Datos utilizados

Cada país contiene:

- Nombre
- Población
- Superficie (km²)
- Continente

Ejemplo:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
Japon,125800000,377975,Asia
```

---

## ⚙️ Funcionalidades

### 1. Mostrar países

Permite visualizar todos los países cargados.

### 2. Agregar país

Permite registrar un nuevo país validando:

- Nombre no vacío
- Nombre sin números
- País no repetido
- Población válida
- Superficie válida
- Continente válido

### 3. Actualizar país

Modifica:

- Población
- Superficie

de un país existente.

### 4. Buscar país

Permite buscar países por nombre mediante coincidencia parcial o exacta.

### 5. Filtrar países

Filtros disponibles:

- Continente
- Rango de población
- Rango de superficie

### 6. Ordenar países

Ordenamientos disponibles:

- Nombre (A-Z)
- Población ascendente
- Población descendente
- Superficie ascendente
- Superficie descendente

### 7. Estadísticas

Muestra:

- País con mayor población
- País con menor población
- Promedio de población
- Promedio de superficie
- Cantidad de países por continente

### 8. Guardar y salir

Guarda los cambios realizados en el archivo CSV.

---

## ▶️ Ejecución

1. Descargar el repositorio.

2. Verificar que exista el archivo:

```text
paises.csv
```

3. Ejecutar:

```bash
python main.py
```

---

## 🛠️ Tecnologías utilizadas

- Python 3
- CSV
- Listas
- Diccionarios
- Funciones

---

## 📚 Conceptos aplicados

- Archivos CSV
- Modularización
- Validaciones
- Estructuras repetitivas
- Estructuras condicionales
- Ordenamiento de datos
- Estadísticas básicas

---

## 👨‍💻 Integrantes

- Facundo Gomez
- Ricardo Oliva

---
## 🎥 Video demostración

Agregar aquí el enlace al video:

```
https://youtu.be/KFaBrPIKCUg?si=V1q1M5q97HWAbEV7
```

---

## 📄 Documentación

Agregar aquí el enlace al PDF:

```
https://drive.google.com/file/d/1n5_eWjimuRRmUGcn_8MgBsx4TfyP5jND/view?usp=drivesdk
```