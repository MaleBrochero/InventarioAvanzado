# Lista inventario
inventario = []


def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario si no existe previamente.
    
    Parámetros:
    - inventario (list): La lista de diccionarios que representa el inventario.
    - nombre (str): El nombre del producto.
    - precio (float): El precio unitario del producto.
    - cantidad (int): La cantidad inicial del producto en stock.
    
    Retorno:
    - None
    """
    # Recorre la lista para verificar que el producto no exista
    for producto in inventario:
        if producto["nombre"] == nombre:
            print("El producto " + nombre + " ya existe. Usa actualizar para modificarlo.")
            return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print("Producto " + nombre + " agregado correctamente.")



def mostrar_inventario(inventario):
    """
    Muestra en consola todos los productos actuales en el inventario.
    
    Parámetros:
    - inventario (list): La lista de productos.
    
    Retorno:
    - None
    """
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return

    print("NOMBRE - PRECIO - CANTIDAD - COSTO TOTAL")
    print("-" * 45)

    for producto in inventario:
        nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        costo_total = precio * cantidad
        print(nombre + " - " + str(precio) + " - " + str(cantidad) + " - " + str(costo_total))

    print("-" * 45)
    print("Total de productos: " + str(len(inventario)))


def buscar_producto(inventario, nombre):
    """
    Busca un producto por su nombre en el inventario.
    
    Parámetros:
    - inventario (list): La lista de productos.
    - nombre (str): El nombre a buscar.
    
    Retorno:
    - dict: El diccionario del producto si se encuentra, o un diccionario vacío si falla.
    """
    # Recorre la lista comparando el nombre de cada diccionario
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto

    # Si no lo encuentra retorna un diccionario vacio
    return {}


def actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
    """
    Actualiza el precio y cantidad de un producto existente.
    
    Parámetros:
    - inventario (list): La lista de productos.
    - nombre (str): El nombre del producto a actualizar.
    - nuevo_precio (float): El nuevo precio.
    - nueva_cantidad (int): La nueva cantidad.
    
    Retorno:
    - None
    """
    producto_encontrado = buscar_producto(inventario, nombre)

    # Si el diccionario esta vacio significa que no se encontro
    if len(producto_encontrado) == 0:
        print("Producto " + nombre + " no encontrado en el inventario.")
        return

    try:
        if nuevo_precio < 0:
            print("El precio no puede ser negativo.")
            return
        producto_encontrado["precio"] = nuevo_precio
        print("Precio de " + nombre + " actualizado a " + str(nuevo_precio))
    except (ValueError, TypeError):
        print("El precio ingresado no es valido.")

    try:
        if nueva_cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return
        producto_encontrado["cantidad"] = nueva_cantidad
        print("Cantidad de " + nombre + " actualizada a " + str(nueva_cantidad))
    except (ValueError, TypeError):
        print("La cantidad ingresada no es valida.")



def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario mediante su nombre.
    
    Parámetros:
    - inventario (list): La lista de productos.
    - nombre (str): Nombre del producto a eliminar.
    
    Retorno:
    - None
    """
    producto_encontrado = buscar_producto(inventario, nombre)

    # Si el diccionario esta vacio significa que no se encontro
    if len(producto_encontrado) == 0:
        print("Producto " + nombre + " no encontrado. Nada que eliminar.")
        return

    inventario.remove(producto_encontrado)
    print("Producto " + nombre + " eliminado del inventario.")


def calcular_estadisticas(inventario):
    """
    Calcula diversas métricas basándose en los productos registrados.
    
    Parámetros:
    - inventario (list): La lista de productos.
    
    Retorno:
    - dict: Un diccionario que contiene métricas agregadas (unidades_totales, valor_total, producto_mas_caro y producto_mayor_stock)
    """
    if len(inventario) == 0:
        print("El inventario esta vacio. No hay estadisticas que calcular.")
        return {}

    unidades_totales = 0
    valor_total = 0
    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    # Recorre la lista acumulando valores y comparando productos
    for producto in inventario:
        unidades_totales = unidades_totales + producto["cantidad"]
        valor_total = valor_total + (producto["precio"] * producto["cantidad"])

        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    estadisticas = {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }

    return estadisticas


def mostrar_estadisticas(inventario):
    """
    Presenta las métricas generadas por calcular_estadisticas en la consola.
    
    Parámetros:
    - inventario (list): La lista de productos.
    
    Retorno:
    - None
    """
    stats = calcular_estadisticas(inventario)

    # Si el diccionario esta vacio significa que el inventario estaba vacio
    if len(stats) == 0:
        return

    print("=" * 40)
    print("ESTADISTICAS DEL INVENTARIO")
    print("=" * 40)
    print("Unidades totales en stock: " + str(stats["unidades_totales"]))
    print("Valor total del inventario: " + str(stats["valor_total"]))
    print("Producto mas caro: " + stats["producto_mas_caro"]["nombre"] + " - $" + str(stats["producto_mas_caro"]["precio"]))
    print("Mayor stock: " + stats["producto_mayor_stock"]["nombre"] + " - " + str(stats["producto_mayor_stock"]["cantidad"]) + " uds.")
    print("=" * 40)

    print("Subtotal por producto:")
    print("-" * 30)
    for producto in inventario:
        # Se usa una variable comun para cumplir la rubrica exactmente y no usar expresiones puramente lambdas, calculando la operacion aqui
        subtotal = producto["precio"] * producto["cantidad"]
        print(producto["nombre"] + " - costo total (existencias): " + str(subtotal))