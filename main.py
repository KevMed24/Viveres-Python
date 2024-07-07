import funciones

def main():
    nombresproduc = [[["" for _ in range(30)] for _ in range(3)] for _ in range(10)]
    precio = [0.0] * 10
    n = [0]

    funciones.leer_datos("Datos.txt", nombresproduc, precio, n)

    opcion1 = 0
    opcion2 = 0
    nombreAbuscar = ""

    while True:
        print("Seleccione una opcion:\n1. Imprimir Inventario\n2. Buscar Productos\n3. Editar Productos\n4. Agregar Producto\n5. Eliminar Producto\n>>", end="")
        opcion1 = int(input())
        if opcion1 == 1:
            funciones.imprimir_inventario(nombresproduc, precio, n[0])
        elif opcion1 == 2:
            print("Ingrese el producto que desea buscar: ", end="")
            nombreAbuscar = input().strip()
            index = funciones.buscar_producto_por_nombre(nombresproduc, nombreAbuscar, n[0])
            funciones.imprimir_producto_por_indice(nombreAbuscar, nombresproduc, precio, index)
        elif opcion1 == 3:
            print("Ingrese el nombre del producto que desea editar: ", end="")
            nombreAbuscar = input().strip()
            funciones.editar_producto(nombreAbuscar, nombresproduc, precio, n[0])
            funciones.guardar_datos("Datos.txt", nombresproduc, precio, n[0])
        elif opcion1 == 4:
            funciones.agregar_producto(nombresproduc, precio, n)
            funciones.guardar_datos("Datos.txt", nombresproduc, precio, n[0])
        elif opcion1 == 5:
            print("Ingrese el nombre del producto que desea eliminar: ", end="")
            nombreAbuscar = input().strip()
            funciones.eliminar_producto(nombresproduc, precio, n, nombreAbuscar)
            funciones.guardar_datos("Datos.txt", nombresproduc, precio, n[0])
        else:
            print("Opción no válida. Intente de nuevo.")

        print("Desea elegir una nueva opcion: 1.Si / 2.No\n>>", end="")
        opcion2 = int(input())
        if opcion2 != 1:
            break

if __name__ == "__main__":
    main()
