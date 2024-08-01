def leer_datos(filename, nombresproduc, precio, n):
    try:
        with open(filename, "r") as file:
            n[0] = 0
            for line in file:
                if n[0] < 10:
                    data = line.strip().split()
                    if len(data) == 4:
                        nombresproduc[n[0]][0] = data[0]
                        nombresproduc[n[0]][1] = data[1]
                        nombresproduc[n[0]][2] = data[2]
                        precio[n[0]] = float(data[3])
                        n[0] += 1
    except FileNotFoundError:
        print("No se pudo abrir el archivo de datos.")

def guardar_datos(filename, nombresproduc, precio, n):
    try:
        with open(filename, "w") as file:
            for i in range(n):
                file.write(f"{nombresproduc[i][0]} {nombresproduc[i][1]} {nombresproduc[i][2]} {precio[i]:.2f}\n")
    except IOError:
        print("Error al abrir el archivo para guardar.")

def imprimir_inventario(nombresproduc, precio, n):
    print("Nombre\t\tCantidad\t\tFecha de Caducidad\t\tPrecio")
    for i in range(n):
        print(f"{nombresproduc[i][0]}\t\t\t{nombresproduc[i][1]}\t\t\t{nombresproduc[i][2]}\t\t{precio[i]:.2f}")

def buscar_producto_por_nombre(nombresproduc, nombre_abuscar, n):
    for i in range(n):
        if nombresproduc[i][0] == nombre_abuscar:
            return i
    return -1

def imprimir_producto_por_indice(nombre_abuscar, nombresproduc, precio, index):
    if index != -1:
        print(f"En el inventario del producto {nombre_abuscar} muestra:")
        print(f"Cantidad: {nombresproduc[index][1]}")
        print(f"Fecha de Caducidad: {nombresproduc[index][2]}")
        print(f"Precio: {precio[index]:.2f}")
    else:
        print(f"No existe el producto {nombre_abuscar} en el registro")

def editar_producto(nombre_abuscar, cantidad, fecha, precio_producto, nombresproduc, precio, n):
    for i in range(n):
        if nombresproduc[i][0] == nombre_abuscar:
            nombresproduc[i][1] = cantidad
            nombresproduc[i][2] = fecha
            precio[i] = precio_producto
            return True
    return False

def agregar_producto(nombre, cantidad, fecha, precio_producto, nombresproduc, precio, n):
    if n[0] >= 10:
        print("No se pueden agregar más productos, el inventario está lleno.")
        return
    nombresproduc[n[0]][0] = nombre
    nombresproduc[n[0]][1] = cantidad
    nombresproduc[n[0]][2] = fecha
    precio[n[0]] = precio_producto
    n[0] += 1

def eliminar_producto(nombre_abuscar, nombresproduc, precio, n):
    index = buscar_producto_por_nombre(nombresproduc, nombre_abuscar, n[0])
    if index != -1:
        for i in range(index, n[0] - 1):
            nombresproduc[i][0] = nombresproduc[i + 1][0]
            nombresproduc[i][1] = nombresproduc[i + 1][1]
            nombresproduc[i][2] = nombresproduc[i + 1][2]
            precio[i] = precio[i + 1]
        n[0] -= 1
        print(f"Producto {nombre_abuscar} ha sido eliminado con éxito.")
    else:
        print(f"No existe el producto {nombre_abuscar} en el inventario.")
