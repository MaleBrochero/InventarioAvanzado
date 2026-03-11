
## Lista inventario 
inventario=[]
#### Entrada de datos 
nombre_producto=input("Por favor agrega el nombre del producto")
inventario.append(nombre_producto)
try:
    precio= float(input("Por favor ingrese eel precio del producto"))
    inventario.append(precio)
    cantidad = int(input("Por favor ingrese cantidad del producto "))
    inventario.append(cantidad)
    #### Operacion Matematica

    costo_total = precio * cantidad
    
    ### Mostrar resultados en consola
    print(f"""Nombre del producto: {nombre_producto} // Precio unitario: {precio} // Cantidad: {cantidad} 
           // Costo total calculado: {costo_total}""")
    
    ####Crea un menú que pregunte al usuario qué acción desea realiza
    menu=input(f""" Por favor seleccione el numero segun la operacion que desea realizar :
                1.Agregar producto
                2.Mostrar inventario
                3.Calcular estadísticas
                4.Salir """)
    while menu == "1" or "2" or "3" :
        
        if menu == "1": #Agrega producto
            nombre_producto=input("Por favor agrega el nombre del producto")
            inventario.append(nombre_producto)
            precio= float(input("Por favor ingrese eel precio del producto"))
            inventario.append(precio)
            cantidad = int(input("Por favor ingrese cantidad del producto "))
            inventario.append(cantidad)
            
            print("")
        elif menu == "2": #Mostrar Investario
            print("")
        elif menu == "3": #Calcular estadistica
            print ("")
        elif menu == "4": #Salir
            print("")
        else :
            print("Caracter equivocado , por favor vuelva a intentar")
            
        menu=input(f""" Por favor seleccione el numero segun la operacion que desea realizar :
        1.Agregar producto
        2.Mostrar inventario
        3.Calcular estadísticas
        4.Salir """)
            
        
except ("Caracter invalido vuelva a intentar")
