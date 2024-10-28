# index.py
from modulo1 import agregar_usuario, eliminar_usuario, listar_usuarios
from modulo2 import importar_datos, exportar_datos, procesar_datos
from modulo3 import generar_reporte_uso, generar_reporte_errores

def mostrar_menu():
    print("1. Agregar Usuario")
    print("2. Eliminar Usuario")
    print("3. Listar Usuarios")
    print("4. Importar Datos")
    print("5. Exportar Datos")
    print("6. Procesar Datos")
    print("7. Generar Reporte de Uso")
    print("8. Generar Reporte de Errores")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            eliminar_usuario()
        elif opcion == '3':
            listar_usuarios()
        elif opcion == '4':
            importar_datos()
        elif opcion == '5':
            exportar_datos()
        elif opcion == '6':
            procesar_datos()
        elif opcion == '7':
            generar_reporte_uso()
        elif opcion == '8':
            generar_reporte_errores()
        elif opcion == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
