# Inventario Avanzado 📦

Un sistema de gestión de inventarios por consola escrito en Python. Permite llevar un control detallado de productos, calcular estadísticas financieras y persistir los datos de manera estructurada a través de archivos CSV.

## 🚀 Características Principales

El programa funciona mediante un menú interactivo con las siguientes opciones:

1. **Agregar producto:** Registra un nuevo producto con su nombre, precio y cantidad.
2. **Mostrar inventario:** Visualiza todos los productos registrados mostrando su precio, existencias y el subtotal calculado en tiempo real.
3. **Buscar:** Encuentra un producto específico por su nombre.
4. **Actualizar:** Modifica el precio y la cantidad de un artículo existente.
5. **Eliminar:** Borra un artículo permanentemente del registro.
6. **Calcular estadísticas:** Obtiene un resumen que incluye el total de unidades en stock, el valor financiero total del inventario, el producto más caro y el artículo con mayores existencias.
7. **Guardar CSV:** Exporta tu inventario actual a un archivo `.csv` (se guarda automáticamente dentro de la carpeta `data/`).
8. **Cargar CSV:** Importa un archivo `.csv` desde la carpeta `data/`. Te permite elegir entre **fusionar** las existencias (suma cantidades y actualiza precios) o **sobrescribir** el inventario actual.
9. **Salir:** Finaliza el programa de forma segura.

## ⚙️ Requisitos

- **Python 3.x** instalado en tu sistema.

No se requieren librerías externas. El proyecto utiliza la librería estándar `csv` y `os` nativas de Python.

## 🏃 ¿Cómo ejecutar el programa?

Abre tu terminal (Símbolo del sistema, PowerShell o la terminal de tu editor de código), asegúrate de estar ubicado en la carpeta principal del proyecto (`InventarioAvanzado`) y ejecuta el siguiente comando:

**En Windows:**
```bash
py src\app.py
```
*(Alternativa si estás en MacOS o Linux: `python3 src/app.py`)*

## 📁 Estructura del Proyecto

El código está modularizado para mantener buenas prácticas de desarrollo:

- `src/app.py`: Archivo principal que arranca el programa, contiene el bucle infinito y gestiona el menú interactivo con validaciones de entrada (`try/except`).
- `src/servicios.py`: Módulo lógico que contiene todas las operaciones de inventario (CRUD, impresión por consola y cálculo de estadísticas).
- `src/estructura_csv.py`: Módulo encargado de la persistencia de datos (guardar, leer y fusionar correctamente los archivos CSV bajo estrictas reglas de formato).
- `data/`: Directorio donde se almacenan automáticamente todos los archivos exportados por el programa.

## 📝 Reglas del formato CSV
Si deseas crear un documento manualmente para cargarlo al programa en la opción 8, tu archivo debe tener terminación `.csv`, estar guardado en la carpeta `data/` y seguir estrictamente tres columnas:

```csv
nombre,precio,cantidad
Manzanas,2.5,100
Zapatos,40.0,3
```
*(Cualquier fila vacía, precio negativo o cantidad errónea será omitida para evitar daños en el inventario)*.
