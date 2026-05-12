# Proyecto Integrador: Sistema de Inventario

## Descripción
Este proyecto es una aplicación de consola en Python para gestionar un inventario de productos tecnológicos. Permite crear, listar, actualizar, eliminar productos y ajustar el stock en diferentes sedes.

## Requisitos
- Python 3.x / el codigo usa python 3.14

## Instalacion
No se requieren dependencias adicionales. Solo Python estándar.

## Ejecuciok
Ejecuta el archivo `proyectointegrador.py` con Python:

```bash
python proyectointegrador.py
```

## Uso
El programa presenta un menú con las siguientes opciones:
1. Crear producto
2. Listar productos
3. Actualizar producto
4. Eliminar producto
5. Ajustar stock
6. Salir

Sigue las instrucciones en pantalla para interactuar con el sistema.

## Funcionalidades
- **Crear producto**: Ingresa código, nombre, categoría, precio y stock inicial por sede.
- **Listar productos**: Muestra una tabla con todos los productos y su stock total.
- **Actualizar producto**: Modifica nombre, precio y categoría de un producto existente.
- **Eliminar producto**: Remueve un producto del inventario.
- **Ajustar stock**: Aumenta o disminuye el stock en una sede específica.

## Validaciones
- Códigos únicos y positivos.
- Precios no negativos.
- Stocks no negativos.
- Entradas de texto no vacías.
- Opciones de menú válidas.

## Casos de Prueba
1. Crear un producto con código 1, nombre "Mouse", categoría 1 (GPU), precio 50.0, stock 10 en cada sede.
2. Listar productos para verificar la creación.
3. Actualizar el producto con código 1 a precio 60.0.
4. Ajustar stock: entrada de 5 unidades en Tienda.
5. Eliminar el producto.
6. Intentar listar productos vacíos.

## Estructura del Cdigo
- productos: Lista de diccionarios con información de productos.
- matriz_stock: Lista de listas para stock por sede.
- Funciones de validación de entrada.
- Funciones CRUD para productos.
- Función para ajustar stock.

## Autor
didier y santiago