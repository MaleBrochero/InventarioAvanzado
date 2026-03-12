
#### Entrada de datos 
nombre_producto=input("Por favor agrega el nombre del producto\n")
try:
    precio= float(input("Por favor ingrese eel precio del producto\n"))
    cantidad = int(input("Por favor ingrese cantidad del producto\n "))
    
#### Operacion Matematica

    costo_total = precio * cantidad
    
### Mostrar resultados en consola
    print(f"""Nombre del producto: {nombre_producto} // Precio unitario: {precio} // Cantidad: {cantidad} 
           // Costo total calculado: {costo_total}""")
except ValueError:
                print("Caracter invalido vuelva a intentar")