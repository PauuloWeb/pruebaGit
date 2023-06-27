def calcular_precio(inmueble):
    zona = inmueble['zona']
    antiguedad = 2023 - inmueble['año']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2
    
    return precio

def agregar_inmueble(lista_inmuebles, inmueble):
    if inmueble['zona'] in ['A', 'B', 'C'] and inmueble['estado'] in ['Disponible', 'Reservado', 'Vendido']:
        if inmueble['año'] >= 2000 and inmueble['metros'] >= 60 and inmueble['habitaciones'] >= 2:
            lista_inmuebles.append(inmueble)
            print('Inmueble agregado con éxito.')
        else:
            print('El inmueble no cumple con las reglas de validación.')
    else:
        print('El inmueble no cumple con las reglas de validación.')

def editar_inmueble(lista_inmuebles, index, nuevo_inmueble):
    if index >= 0 and index < len(lista_inmuebles):
        inmueble_actual = lista_inmuebles[index]
        inmueble_actual.update(nuevo_inmueble)
        print('Inmueble editado con éxito.')
    else:
        print('Índice inválido.')

def eliminar_inmueble(lista_inmuebles, index):
    if index >= 0 and index < len(lista_inmuebles):
        inmueble = lista_inmuebles.pop(index)
        print('Inmueble eliminado con éxito.')
        return inmueble
    else:
        print('Índice inválido.')

def cambiar_estado(lista_inmuebles, index, nuevo_estado):
    if index >= 0 and index < len(lista_inmuebles):
        inmueble = lista_inmuebles[index]
        inmueble['estado'] = nuevo_estado
        print('Estado del inmueble cambiado con éxito.')
    else:
        print('Índice inválido.')

def buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista_inmuebles:
        if (inmueble['estado'] in ['Disponible', 'Reservado'] and
            calcular_precio(inmueble) <= presupuesto):
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = calcular_precio(inmueble)
            inmuebles_encontrados.append(inmueble_con_precio)
    
    return inmuebles_encontrados

# Ejemplo de uso
lista_inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]

# Agregar un nuevo inmueble
nuevo_inmueble = {'año': 2020, 'metros': 120, 'habitaciones': 3, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}
agregar_inmueble(lista_inmuebles, nuevo_inmueble)

# Editar un inmueble existente
editar_inmueble(lista_inmuebles, 1, {'metros': 90, 'habitaciones': 2})

# Eliminar un inmueble existente
eliminar_inmueble(lista_inmuebles, 3)

# Cambiar el estado de un inmueble existente
cambiar_estado(lista_inmuebles, 2, 'Reservado') 

# Buscar inmuebles por presupuesto
presupuesto = 15000
inmuebles_encontrados = buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto)
for inmueble in inmuebles_encontrados:
    print(inmueble)
