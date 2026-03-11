
## Lista inventario 
inventario=[]
#### Entrada de datos 
try:
    
    ####Crea un menú que pregunte al usuario qué acción desea realiza
    menu=input(f""" Por favor seleccione el numero segun la operacion que desea realizar :
                1.Agregar producto
                2.Mostrar inventario
                3.Calcular estadísticas
                4.Salir """)
    while menu == "1" or "2" or "3" :

        if menu == "1": #Agrega producto
            nombre_producto=input("Por favor agrega el nombre del producto")
            precio= float(input("Por favor ingrese eel precio del producto"))
            
            cantidad = int(input("Por favor ingrese cantidad del producto "))
            costo_total = precio * cantidad

            producto = { "Nombre del producto" : nombre_producto, 
                    "Precio_unitario" : precio, 
                    "Cantidad " : cantidad,
                    "Costo_total_calculado " : costo_total}
            
            inventario.append(producto)

        elif menu == "2": #Mostrar Investario

            for producto in inventario:
                print(producto)
                print(producto["Nombre"])





            print( inventario )
        elif menu == "3": #Calcular estadistica

            valor_total_inventario += costo_total
            cantidad_de_producto_registrado = inventario.count()

            print (f"""Cantidad de productos en el inventario {cantidad_de_producto_registrado}
                        Valor total del inventario {valor_total_inventario} """)

        elif menu == "4": #Salir
            print(" Fin ")

        else :
            print("Caracter equivocado , por favor vuelva a intentar")
            
        menu=input(f""" Por favor seleccione el numero segun la operacion que desea realizar :
        1.Agregar producto
        2.Mostrar inventario
        3.Calcular estadísticas
        4.Salir """)
    print (" Programa finalizado")
except ValueError:
    print("Caracter invalido vuelva a intentar")


