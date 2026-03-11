
#### Entrada de datos 
nombre_producto=input("Por favor agrega el nombre del producto")
try:
    precio= float(input("Por favor ingrese eel precio del producto"))
    cantidad = int(input("Por favor ingrese cantidad del producto "))
    
#### Operacion Matematica

    costo_total = precio * cantidad
    
### Mostrar resultados en consola
    print(f"""Nombre del producto: {nombre_producto} // Precio unitario: {precio} // Cantidad: {cantidad} 
           // Costo total calculado: {costo_total}""")
except("Caracter invalido vuelva a intentar")