# Libreria para manejar archivos CSV
import csv


def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Sonda el inventario actual y lo guarda en un archivo CSV estableciendo
    el formato estricto: nombre, precio, cantidad.
    
    Parámetros:
    - inventario (list): La lista de diccionarios con el inventario a respaldar.
    - ruta (str): Ubicación y nombre del archivo CSV.
    - incluir_header (bool): Verdadero por defecto. Agrega la primera línea de títulos técnicos.
    
    Retorno:
    - None
    """
    if len(inventario) == 0:
        print("El inventario esta vacio. No hay nada que guardar.")
        return

    try:
        archivo = open(ruta, mode="w", newline="", encoding="utf-8")
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio", "cantidad"])

        if incluir_header:
            escritor.writeheader()

        for producto in inventario:
            escritor.writerow(producto)

        archivo.close()
        print("Inventario guardado en: " + ruta)

    except PermissionError:
        print("Sin permisos para escribir en " + ruta + ". Elige otra ubicacion.")
    except:
        print("Error al guardar el archivo " + ruta)


def cargar_csv(ruta):
    """
    Lee y valida un archivo CSV para extraer una lista de productos. 
    Aplica controles para descartar filas con menos de 3 columnas o tipos numéricos incorrectos/negativos.
    
    Parámetros:
    - ruta (str): Ubicación del archivo a leer.
    
    Retorno:
    - list: Una nueva lista de diccionarios {"nombre", "precio", "cantidad"} validada.
    """
    productos_validos = []
    filas_invalidas = 0

    try:
        archivo = open(ruta, mode="r", newline="", encoding="utf-8")
        lector = csv.reader(archivo)

        # Lee y valida el encabezado
        encabezado = next(lector)
        encabezado_limpio = []
        for col in encabezado:
            encabezado_limpio.append(col.strip().lower())

        if encabezado_limpio != ["nombre", "precio", "cantidad"]:
            print("El encabezado del archivo no es valido. Se esperaba: nombre,precio,cantidad")
            archivo.close()
            return []

        # Recorre cada fila y valida sus datos
        numero_fila = 2
        for fila in lector:

            if len(fila) != 3:
                print("Fila " + str(numero_fila) + ": se esperaban exactamente 3 columnas. Omitida.")
                filas_invalidas = filas_invalidas + 1
                numero_fila = numero_fila + 1
                continue

            nombre = fila[0].strip()
            precio_str = fila[1].strip()
            cantidad_str = fila[2].strip()

            if nombre == "":
                print("Fila " + str(numero_fila) + ": nombre vacio. Omitida.")
                filas_invalidas = filas_invalidas + 1
                numero_fila = numero_fila + 1
                continue

            # Valida precio con try except
            try:
                precio = float(precio_str)
                if precio < 0:
                    print("Fila " + str(numero_fila) + ": precio negativo. Omitida.")
                    filas_invalidas = filas_invalidas + 1
                    numero_fila = numero_fila + 1
                    continue
            except:
                print("Fila " + str(numero_fila) + ": precio invalido '" + precio_str + "'. Omitida.")
                filas_invalidas = filas_invalidas + 1
                numero_fila = numero_fila + 1
                continue

            # Valida cantidad con try except
            try:
                cantidad = int(cantidad_str)
                if cantidad < 0:
                    print("Fila " + str(numero_fila) + ": cantidad negativa. Omitida.")
                    filas_invalidas = filas_invalidas + 1
                    numero_fila = numero_fila + 1
                    continue
            except:
                print("Fila " + str(numero_fila) + ": cantidad invalida '" + cantidad_str + "'. Omitida.")
                filas_invalidas = filas_invalidas + 1
                numero_fila = numero_fila + 1
                continue

            # Fila valida, se arma el diccionario y se agrega a la lista
            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            productos_validos.append(producto)
            numero_fila = numero_fila + 1

        archivo.close()

    except FileNotFoundError:
        print("Archivo no encontrado: " + ruta)
        return []
    except UnicodeDecodeError:
        print("Error de codificacion en " + ruta + ". Guardalo en UTF-8.")
        return []
    except:
        print("Error inesperado al leer el archivo " + ruta)
        return []

    if filas_invalidas > 0:
        print(str(filas_invalidas) + " fila(s) invalida(s) omitida(s).")

    print(str(len(productos_validos)) + " producto(s) leido(s) desde " + ruta)
    return productos_validos


def integrar_csv(inventario, ruta):
    """
    Carga un archivo CSV externo y permite al usuario definir una política para integrarlo a su inventario actual.
    Si se elige Sobrescribir (S), el archivo reemplazará por completo el inventario en memoria.
    Si se elige Fusionar (N), los productos de coincidencia de nombre alteran sus cantidades y el precio se actualiza.
    
    Parámetros:
    - inventario (list): La lista de diccionarios en la memoria principal.
    - ruta (str): Ubicación del archivo CSV a integrar.
    
    Retorno:
    - None
    """
    # Politica de fusion:
    # Si el nombre ya existe: suma la cantidad y actualiza el precio al nuevo.
    # Si el nombre no existe: se agrega directamente.

    productos_cargados = cargar_csv(ruta)

    if len(productos_cargados) == 0:
        print("No se cargaron productos. El inventario no cambia.")
        return

    print("Opciones:")
    print("  S - Sobrescribir el inventario actual.")
    print("  N - Fusionar con el inventario actual.")

    opcion = ""
    while opcion != "S" and opcion != "N":
        opcion = input("Sobrescribir inventario actual? (S/N): ").strip().upper()
        if opcion != "S" and opcion != "N":
            print("Opcion invalida. Escribe S o N.")

    nuevos = 0
    fusiones = 0
    accion = ""

    if opcion == "S":
        # Limpia la lista y agrega los productos cargados
        inventario.clear()
        for producto in productos_cargados:
            inventario.append(producto)
        accion = "reemplazo total"

    else:
        accion = "fusion"
        for p_nuevo in productos_cargados:
            encontrado = False

            # Recorre el inventario para ver si el producto ya existe
            for p_existente in inventario:
                if p_existente["nombre"] == p_nuevo["nombre"]:
                    encontrado = True

                    if p_existente["precio"] != p_nuevo["precio"]:
                        print(p_existente["nombre"] + ": precio " + str(p_existente["precio"]) + " -> " + str(p_nuevo["precio"]))
                        p_existente["precio"] = p_nuevo["precio"]

                    p_existente["cantidad"] = p_existente["cantidad"] + p_nuevo["cantidad"]
                    print(p_existente["nombre"] + ": cantidad actualizada a " + str(p_existente["cantidad"]) + " uds.")
                    fusiones = fusiones + 1
                    break

            if encontrado == False:
                inventario.append(p_nuevo)
                nuevos = nuevos + 1

    print("=" * 40)
    print("RESUMEN DE CARGA")
    print("=" * 40)
    print("Accion realizada: " + accion)
    print("Productos cargados: " + str(len(productos_cargados)))
    if opcion == "N":
        print("Productos nuevos: " + str(nuevos))
        print("Productos fusionados: " + str(fusiones))
    print("Total en inventario: " + str(len(inventario)))
    print("=" * 40)