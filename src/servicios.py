inventario = []
valor_total_inventario = 0
cantidad_total_inventario = 0


def agregar_producto(A, B, C):

    producto = {"Nombre_del_producto": A,  # Diccionario
                "Precio_unitario": B,
                "Cantidad ": C,
                "Costo_total_calculado ": calcular_estadistica(B, C)}
    inventario.append(producto)


def calcular_estadistica(B, C):
    costo_total = B * C  # Operacion
    valor_total_inventario += costo_total  # Acumulador

            print (f"""Cantidad de productos en el inventario {cantidad_total_inventario}
Valor total del inventario {valor_total_inventario} """)
    
#     unidades_totales = suma de cantidad
# valor_total = suma de precio * cantidad
# producto_mas_caro (nombre y precio)
# producto_mayor_stock (nombre y cantidad)


def mostrar_producto():
    for producto in inventario:
        print(producto)


def buscar(A):
    for i in inventario:
        if i == A:
            print(A)
        else:
            print("Este producto no existe")


def actualizar_producto():

    producto_actualizar = int(input(f""" Marque :
                                        1.Actualizar precio
                                        2.Actualizar cantidad """))
    if producto_actualizar == 1:
        nombre_producto_ac = input(" Por favor ingrese el nombre del producto ha actualizar")
        nuevo_precio = float(input(" por favor ingrese nuevo precio"))
        
        for i in inventario:
            if i == nombre_producto_ac:
                for x in inventario[i]:
                    if x == inventario[i]["Precio_unitario"]:
                        x.insert(nuevo_precio) 
                

    elif producto_actualizar == 2:
        nombre_producto_ac = input(
            " Por favor ingrese el nombre del producto ha actualizar")
        nueva_cantidad = float(input(" por favor ingrese cantidad total"))

        for i in inventario:
            if i == nombre_producto_ac:
                for x in inventario[i]:
                    if x == inventario[i]["Cantidad"]:
                        x.insert(nueva_cantidad) 
                        
                        
    else:
        print ("""Opcion invalida  """)

def eliminar_producto (A):
    
    for i in inventario:
        if i == A:
            for x in inventario[i]:
                if x == inventario[i]:
                    x.pop() 
                 
                else :
                    print ("""Opcion invalida  """)
                    
            
    
    
