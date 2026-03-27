import servicios
import archivos

#### Entrada de datos
try:

    #### Crea un menu que pregunte al usuario que accion desea realizar
    menu = input(""" Por favor seleccione el numero segun la operacion que desea realizar :
                1.Agregar producto
                2.Mostrar inventario
                3.Buscar
                4.Actualizar
                5.Eliminar
                6.Calcular estadisticas
                7.Guardar CSV
                8.Cargar CSV
                9.Salir\n """)

    while menu == "1" or menu == "2" or menu == "3" or menu == "4" or menu == "5" or menu == "6" or menu == "7" or menu == "8" or menu == "9":

        if menu == "1":  # Agrega producto
            nombre_producto = input("Por favor agrega el nombre del producto: ")
            precio = float(input("Por favor ingrese el precio del producto: "))
            cantidad = int(input("Por favor ingrese cantidad del producto: "))

            servicios.agregar_producto(servicios.inventario, nombre_producto, precio, cantidad)

        elif menu == "2":  # Mostrar inventario

            servicios.mostrar_inventario(servicios.inventario)

        elif menu == "3":  # Buscar

            nombre_producto_inventario = input("Por favor ingrese el producto a consultar: ")

            resultado = servicios.buscar_producto(servicios.inventario, nombre_producto_inventario)

            if len(resultado) == 0:
                print("El producto " + nombre_producto_inventario + " no existe en el inventario.")
            else:
                print("Producto encontrado:")
                print("Nombre: " + resultado["nombre"])
                print("Precio: " + str(resultado["precio"]))
                print("Cantidad: " + str(resultado["cantidad"]))

        elif menu == "4":  # Actualizar

            nombre_producto = input("Por favor ingrese el nombre del producto a actualizar: ")
            nuevo_precio = float(input("Por favor ingrese el nuevo precio: "))
            nueva_cantidad = int(input("Por favor ingrese la nueva cantidad: "))

            servicios.actualizar_producto(servicios.inventario, nombre_producto, nuevo_precio, nueva_cantidad)

        elif menu == "5":  # Eliminar

            elimina_producto = input("Escriba el nombre del producto que desea eliminar: ")

            servicios.eliminar_producto(servicios.inventario, elimina_producto)

        elif menu == "6":  # Calcular estadisticas

            servicios.mostrar_estadisticas(servicios.inventario)

        elif menu == "7":  # Guardar CSV

            ruta = input("Ingrese el nombre del archivo donde desea guardar (ejemplo: inventario.csv): ")

            archivos.guardar_csv(servicios.inventario, ruta)

        elif menu == "8":  # Cargar CSV

            ruta = input("Ingrese el nombre del archivo CSV que desea cargar: ")

            archivos.integrar_csv(servicios.inventario, ruta)

        elif menu == "9":  # Salir
            print("Fin")
            break

        else:
            print("Caracter equivocado, por favor vuelva a intentar.")

        menu = input(""" Por favor seleccione el numero segun la operacion que desea realizar :
                1.Agregar producto
                2.Mostrar inventario
                3.Buscar
                4.Actualizar
                5.Eliminar
                6.Calcular estadisticas
                7.Guardar CSV
                8.Cargar CSV
                9.Salir\n """)

    print("Programa finalizado")

except ValueError:
    print("Caracter invalido vuelva a intentar")