CATEGORIAS = ["GPU", "CPU", "RAM", "SSD", "Periferico"]

SEDES = ["Tienda", "Bodega", "Online"]

productos = []


def limpiar_pantalla():
    print("\n" + "=" * 60)


def leer_entero(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            valor = int(texto)
            return valor
        except ValueError:
            print("Dato invalido escribi un numero entero")


def leer_float(mensaje):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(texto)
            return valor
        except ValueError:
            print("Dato invalido escribi un numero")


def leer_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo no pued quedar vacio")


def buscar_indice_por_codigo(codigo):
    for i in range(len(productos)):
        producto = productos[i]
        if producto["codigo"] == codigo:
            return i
    return -1


def crear_producto():
    limpiar_pantalla()
    print("CREAR PRODUCTO")

    codigo = leer_entero("Codigo del producto: ")
    if codigo < 1:
        print("El codigo debe ser mayor o igual a 1")
        return
    if buscar_indice_por_codigo(codigo) != -1:
        print("Ese codigo ya existe intenta con otro")
        return

    nombre = leer_texto_no_vacio("Nombre del producto: ")
    print("Categorias disponibles:")
    for i in range(len(CATEGORIAS)):
        print(f"{i + 1}. {CATEGORIAS[i]}")
    opcion_categoria = leer_entero("Selecciona categoria: ")
    while opcion_categoria < 1 or opcion_categoria > len(CATEGORIAS):
        print("Opcion invalida")
        opcion_categoria = leer_entero("Selecciona categoria: ")
    categoria = CATEGORIAS[opcion_categoria - 1]
    precio = leer_float("Precio unitario: ")
    if precio < 0:
        print("El precio no pued ser negativo")
        return

    productos.append(
        {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stock": {},
        }
    )

    print("Ingresa stock inicial por sede")
    for sede in SEDES:
        cantidad = leer_entero(f"Stock en {sede}: ")
        if cantidad < 0:
            print("No pued ser negativo")
            return
        productos[-1]["stock"][sede] = cantidad

    print("Producto creado con exito")


def listar_productos():
    limpiar_pantalla()
    print("LISTADO DE INVENTARIO")

    if not productos:
        print("Todavia no hay productos registrados")
        return

    encabezado = "Codigo | Nombre | Categoria | Precio"
    for i in range(len(SEDES)):
        encabezado = encabezado + " | " + SEDES[i]
    encabezado = encabezado + " | Stock total"
    print(encabezado)
    print("-" * len(encabezado))

    for i in range(len(productos)):
        producto = productos[i]
        fila = (
            f"{producto['codigo']} | {producto['nombre']} | "
            f"{producto['categoria']} | ${producto['precio']:.2f}"
        )
        total = 0
        for sede in SEDES:
            cantidad = producto["stock"][sede]
            total = total + cantidad
            fila = fila + " | " + str(cantidad)
        fila = fila + " | " + str(total)
        print(fila)


def actualizar_producto():
    limpiar_pantalla()
    print("ACTUALIZAR PRODUCTO")

    if not productos:
        print("No hay productos para actualizar por ahora")
        return

    codigo = leer_entero("Codigo del producto a actualizar: ")
    if codigo < 1:
        print("El codigo debe ser mayor o igual a 1")
        return
    indice = buscar_indice_por_codigo(codigo)

    if indice == -1:
        print("No encontre ningun producto con ese codigo")
        return

    nuevo_nombre = leer_texto_no_vacio("Nuevo nombre del producto: ")
    nuevo_precio = leer_float("Nuevo precio unitario: ")
    if nuevo_precio < 0:
        print("El precio no pued ser negativo")
        return
    print("Categorias disponibles:")
    for i in range(len(CATEGORIAS)):
        print(f"{i + 1}. {CATEGORIAS[i]}")
    opcion_categoria = leer_entero("Nueva categoria: ")
    while opcion_categoria < 1 or opcion_categoria > len(CATEGORIAS):
        print("Opcion invalida")
        opcion_categoria = leer_entero("Nueva categoria: ")

    productos[indice]["nombre"] = nuevo_nombre
    productos[indice]["precio"] = nuevo_precio
    productos[indice]["categoria"] = CATEGORIAS[opcion_categoria - 1]

    print("Datos actualizados correctamente")


def eliminar_producto():
    limpiar_pantalla()
    print("ELIMINAR PRODUCTO")

    if not productos:
        print("No hay productos para eliminar por ahora")
        return

    codigo = leer_entero("Codigo del producto a eliminar: ")
    if codigo < 1:
        print("El codigo debe ser mayor o igual a 1")
        return
    indice = buscar_indice_por_codigo(codigo)

    if indice == -1:
        print("No encontre ningun producto con ese codigo")
        return

    eliminado = productos.pop(indice)
    print(f"Se elimino {eliminado['nombre']} del inventario")


def ajustar_stock():
    limpiar_pantalla()
    print("AJUSTAR STOCK")

    if not productos:
        print("Todavia no hay productos registrados")
        return

    codigo = leer_entero("Codigo del producto: ")
    if codigo < 1:
        print("El codigo debe ser mayor o igual a 1")
        return
    indice = buscar_indice_por_codigo(codigo)

    if indice == -1:
        print("No encontre ningun producto con ese codigo")
        return

    print(f"Producto seleccionado: {productos[indice]['nombre']}")
    print("Sedes disponibles:")
    for i in range(len(SEDES)):
        print(f"{i + 1}. {SEDES[i]}")
    opcion_sede = leer_entero("Selecciona sede: ")
    while opcion_sede < 1 or opcion_sede > len(SEDES):
        print("Opcion invalida")
        opcion_sede = leer_entero("Selecciona sede: ")
    pos_sede = opcion_sede - 1

    print("Tipo de ajuste:")
    print("1. Entrada")
    print("2. Salida")
    tipo = leer_entero("Selecciona opcion: ")
    while tipo != 1 and tipo != 2:
        print("Opcion invalida")
        tipo = leer_entero("Selecciona opcion: ")
    unidades = leer_entero("Cantidad de unidades: ")
    if unidades < 1:
        print("La cantidad debe ser mayor o igual a 1")
        return

    stock_actual = productos[indice]["stock"][SEDES[pos_sede]]
    if tipo == 1:
        productos[indice]["stock"][SEDES[pos_sede]] = stock_actual + unidades
        print("Stock actualizado correctamente")
        return

    if unidades > stock_actual:
        print("No hay suficiente stock para esa salida")
        return

    productos[indice]["stock"][SEDES[pos_sede]] = stock_actual - unidades
    print("Stock actualizado correctamente")


def mostrar_menu():
    print("\nMENU PRINCIPAL")
    print("1. Crear producto")
    print("2. Listar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Ajustar stock")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = leer_entero("Selecciona una opcion (1-6): ")
        while opcion < 1 or opcion > 6:
            print("Opcion invalida")
            opcion = leer_entero("Selecciona una opcion (1-6): ")

        if opcion == 1:
            crear_producto()
        elif opcion == 2:
            listar_productos()
        elif opcion == 3:
            actualizar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            ajustar_stock()
        elif opcion == 6:
            limpiar_pantalla()
            print("Gracias por usar el sistema nos vemos")
            break


if __name__ == "__main__":
    main()
