import servicios 
# Lista inventario 
inventario=[]
## Acumulador iniciado
valor_total_inventario = 0
cantidad_total_inventario = 0
#### Entrada de datos 
try:
    
    ####Crea un menú que pregunte al usuario qué acción desea realiza
    menu=input(f""" Por favor seleccione el numero segun la operacion que desea realizar :
                1.Agregar producto
                2.Mostrar inventario
                3.Buscar
                4.Actualizar
                5.Eliminar
                6.Calcular estadísticas
                7.Guardar CSV
                8.Cargar CSV
                9.Salir\n """)
    
    while menu == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" :

        if menu == "1": #Agrega producto
            nombre_producto=input("Por favor agrega el nombre del producto ")
            precio= float(input("Por favor ingrese el precio del producto "))
            cantidad = int(input("Por favor ingrese cantidad del producto "))
            
            servicios.agregar_producto(nombre_producto, precio,cantidad)

        elif menu == "2": #Mostrar Investario

            servicios.mostrar_producto()
            
        elif menu == "3" : ### Buscar
                
                nombre_producto_inventario = input ("Por favor ingrese el producto a consultar")
                print (nombre_producto_inventario)
                
                servicios.buscar (nombre_producto_inventario)
                
        elif menu == "4" : ### Actualizar o reescribir
            
            servicios.actualizar_producto()
                                    
        elif menu == "5" : ### Eliminar
            
            elimina_producto = input( "Escriba el nombre del producto que desea elimminar")
            
            servicios.eliminar_producto (elimina_producto)
                
        elif menu == "6": #Calcular estadistica
            
            def calcular_estadistica ()

        
        elif menu == "7" : ### Guardar CSV
            pass
        
        elif menu == "8" : ### Cargar CSV
            
            
            
        elif menu == "9": #Salir
            print(" Fin ")
            break
        else :
            print("Caracter equivocado , por favor vuelva a intentar")
            
        menu=input(f""" Por favor seleccione el numero segun la operacion que desea realizar :
                1.Agregar producto
                2.Mostrar inventario
                3.Buscar
                4.Actualizar
                5.Eliminar
                6.Calcular estadísticas
                7.Guardar CSV
                8.Cargar CSV
                9.Salir\n """)
        
    print (" Programa finalizado")

except ValueError:
    print("Caracter invalido vuelva a intentar")

