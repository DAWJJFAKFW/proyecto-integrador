# Documentación para Exposición

Este documento explica lo que hace cada parte del proyecto `proyectointegrador.py` para que puedas presentarlo fácilmente al profesor.

## 1. Qué hace el proyecto

Es una aplicación de consola en Python que gestiona un inventario de productos. Permite:
- crear productos,
- listar los productos existentes,
- actualizar datos de un producto,
- eliminar productos,
- ajustar el stock por sede.

Se usa una lista de productos donde cada producto es un diccionario con su información y su stock.

## 2. Variables globales

- `CATEGORIAS`: lista con las categorías disponibles (`GPU`, `CPU`, `RAM`, `SSD`, `Periferico`).
- `SEDES`: lista con los lugares donde se guarda el stock (`Tienda`, `Bodega`, `Online`).
- `productos`: lista vacía que guarda todos los productos creados.

Cada producto se guarda así:
```python
{
    "codigo": 1,
    "nombre": "Mouse",
    "categoria": "Periferico",
    "precio": 50.0,
    "stock": {
        "Tienda": 10,
        "Bodega": 5,
        "Online": 2,
    }
}
```

## 3. Funciones auxiliares

Estas funciones apoyan todo el programa y se usan desde otras partes.

### `limpiar_pantalla()`
- Imprime una línea de separación para que el menú y las opciones se vean mejor.

### `leer_entero(mensaje)`
- Pide un valor por teclado.
- Valida que el usuario ingrese un número entero.
- Repite la pregunta hasta que la entrada sea correcta.

### `leer_float(mensaje)`
- Pide un valor por teclado.
- Convierte comas a puntos si el usuario escribe `12,5`.
- Valida que la entrada sea un número decimal.
- Repite hasta que la entrada sea válida.

### `leer_texto_no_vacio(mensaje)`
- Pide una cadena de texto.
- No acepta entradas vacías.
- Repite hasta que el usuario escriba algo.

### `buscar_indice_por_codigo(codigo)`
- Recorre la lista `productos`.
- Busca un producto con el código dado.
- Devuelve la posición del producto en la lista o `-1` si no existe.

### `mostrar_menu()`
- Imprime el menú principal con las opciones disponibles.

## 4. Funciones principales

### `crear_producto()`
- Pide datos básicos del producto: código, nombre, categoría y precio.
- Valida que el código sea único y mayor que 0.
- Valida que el precio no sea negativo.
- Pide el stock inicial por cada sede.
- Guarda todo en la lista `productos`.

### `listar_productos()`
- Muestra todos los productos guardados.
- Imprime el código, nombre, categoría, precio y stock por sede.
- Calcula el stock total sumando los valores de cada sede.

### `actualizar_producto()`
- Pide el código del producto a modificar.
- Busca el producto con `buscar_indice_por_codigo()`.
- Si lo encuentra, pide nuevo nombre, nuevo precio y nueva categoría.
- Cambia los valores guardados en el producto.

### `eliminar_producto()`
- Pide el código del producto a eliminar.
- Busca el producto y lo borra de la lista `productos`.
- Así el producto ya no aparece en el inventario.

### `ajustar_stock()`
- Pide el código del producto.
- Muestra las sedes disponibles.
- Permite elegir si el movimiento es `Entrada` o `Salida`.
- Aumenta o disminuye el stock de esa sede.
- Valida que no se pueda sacar más stock del que hay.

## 5. Flujo principal

### `main()`

- Ejecuta un bucle infinito que muestra el menú.
- Pide al usuario elegir una opción.
- Llama a la función correspondiente según la opción elegida.
- Si elige `6`, termina el programa.

### `if __name__ == "__main__":`
- Esta línea hace que el programa se ejecute solo cuando se corre el archivo directamente.
- Si el archivo se importa desde otro programa, no ejecuta `main()` automáticamente.

## 6. Validaciones importantes

El programa cuida que el usuario no escriba datos errados:
- no permite códigos negativos o repetidos,
- no permite precios negativos,
- no permite stocks negativos,
- no permite nombres vacíos,
- no deja elegir opciones fuera del menú.

## 7. Por qué es útil este proyecto

- Usa funciones para separar tareas.
- Usa listas y diccionarios para guardar datos.
- Tiene control de flujo con `while`, `if` y `for`.
- Es un programa completo de consola, con menú y validaciones.
- Es ideal para mostrar los contenidos del curso: arreglos, funciones, validación y buenas prácticas.
