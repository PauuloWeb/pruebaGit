# Ejercicio 2: Supermercado
#       Un supermercado maneja el catálogo de los productos que vende. 
#       De cada producto se conoce su nombre, precio, y si el mismo es parte del programa Precios Cuidados o no.
#       Por defecto, el producto no es parte del programa, a
#       menos que se especifique lo contrario.
#       Para ayudar a los clientes, el supermercado quiere realizar descuentos en
#       productos de Primera Necesidad. Es por eso que al calcular el precio de un
#       producto de Primera Necesidad, se aplica un descuento del 10%. 

#       Es decir:
#           precioProductoPrimeraNecesidad = precioBaseDelProducto * 0.9

# El supermercado, del cual se conoce el nombre y la dirección, desea conocer la
# cantidad total de productos que comercializa y la suma total de los precios de los
# mismos.
# ---
# Suponga ahora que el descuento a aplicar en cada producto de primera
# necesidad puede ser distinto y se debe poder definir al momento de crear el
# mismo. Por ejemplo, el arroz puede ser un producto de primera necesidad con un
# descuento del 8%, mientras que leche podría ser otro producto de primera
# necesidad con un decuento del 11%. Esto es sólo un ejemplo. El descuento a
# aplicar en cada producto de primera necesidad debe ser configurable al
# momento de crearlo.
# Implementar un nuevo programa basado en el anterior que incorpore este
# nuevo requerimiento.


class Producto:
    def __init__(self, nombre, precio, es_precio_cuidados=False, descuento=1):
        self.nombre = nombre
        self.precio = precio
        self.es_precio_cuidados = es_precio_cuidados
        self.descuento = descuento
    
    def calcular_precio(self, desc):
        if self.es_precio_cuidados:
            return self.precio * desc
        else:
            return self.precio
        
    

# El supermercado, del cual se conoce el nombre y la dirección, desea conocer la
# cantidad total de productos que comercializa y la suma total de los precios de los
# mismos.

class Supermercado:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def cantidad_productos(self):
        return len(self.productos)
    
    def suma_total_precios(self):
        total = 0
        for prod in self.productos:
            total += prod.calcular_precio(prod.descuento)
            print(f"total:{total}")
        return total
    
supermercado = Supermercado("El Chino de la esquina", "Sarmiento123")

# Crear mis productos
# el arroz puede ser un producto de primera necesidad con un
# descuento del 8%, mientras que leche podría ser otro producto de primera
# necesidad con un decuento del 11%.
producto1 = Producto('Arroz', 200, True, 0.92)
producto2 = Producto('Leche', 80, True, 0.89)

# Agregar los productos a mi supermercado

supermercado.agregar_producto(producto1)
supermercado.agregar_producto(producto2)

cantidad_productos = supermercado.cantidad_productos()
precio_total = supermercado.suma_total_precios()

print(f"Estas comprando {cantidad_productos} productos :)!")
print(f"por un total de ARS${precio_total}")