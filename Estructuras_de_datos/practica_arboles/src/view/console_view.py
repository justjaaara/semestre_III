import sys
import re  # Importamos el módulo re para expresiones regulares

sys.path.append("src/")

from model.practica import Arbol

class Consola:
    def __init__(self):
        self.arbol = Arbol()
        self.directorio_actual = self.arbol.raiz  # Inicialmente en la raíz

    def ejecutar_comando(self, comando):
        try:
            args = comando.split()
            if len(args) == 0:  # Comando vacío
                print("Error: No se ha ingresado ningún comando.")
                return

            if args[0] == "ls":
                if len(args) == 2:
                    ruta = args[1]
                    print(self.arbol.listar(ruta))
                else:
                    print(self.arbol.listar(self.obtener_ruta_actual()))

            elif args[0] == "ls-R":
                self.arbol.listar_recursivo(self.directorio_actual)

            elif args[0] == "mkdir":
                if len(args) < 2 or not self.validar_nombre_directorio(args[1]):  # Verifica que haya un argumento válido
                    print("Error: 'mkdir' requiere un nombre de directorio válido y no puede contener solo espacios o caracteres especiales.")
                    return
                nombre_directorio = args[1]
                self.arbol.crear_directorio(self.obtener_ruta_actual(), nombre_directorio)

            elif args[0] == "rm-r":
                if len(args) < 2 or not args[1].strip():  # Verifica que haya un argumento no vacío
                    print("Error: 'rm-r' requiere el nombre del directorio a eliminar.")
                    return

                path = args[1]
                resultado, mensaje = self.arbol.eliminar_directorio(path)

                if not resultado:
                    if "contiene otros archivos o carpetas" in mensaje:
                        confirmacion = input(f"{mensaje}\n¿Estás seguro que deseas eliminarlo? (s/n): ").lower()
                        if confirmacion == 's':
                            resultado, mensaje = self.arbol.eliminar_directorio(path, forzar=True)
                            print(mensaje)
                        else:
                            print("Operación cancelada, opción inválida.")
                    else:
                        print(mensaje)
                else:
                    print(mensaje)

            elif args[0] == "mv":
                if len(args) < 3 or not args[1].strip() or not args[2].strip():  # Verifica dos argumentos no vacíos
                    print("Error: 'mv' requiere el nombre actual y el nuevo nombre.")
                    return
                print(self.arbol.modificar_nombre(args[1], args[2]))

            elif args[0] == "cd":
                if len(args) < 2 or not args[1].strip():  # Verifica que haya un argumento no vacío
                    print("Error: 'cd' requiere un nombre de directorio.")
                    return
                nuevo_directorio = self.arbol.buscar_ruta(args[1])
                if nuevo_directorio and nuevo_directorio.es_directorio:
                    self.directorio_actual = nuevo_directorio
                    print(f"Cambiado a {self.obtener_ruta_actual()}")
                else:
                    print("Directorio no encontrado.")
            
            elif args[0] == "exit":
                sys.exit()

            elif args[0] == "pwd":
                print(self.obtener_ruta_actual())

            else:
                print(f"Error: Comando '{args[0]}' no reconocido.")

        except Exception as e:
            print(f"Error al ejecutar el comando: {e}")

    def obtener_ruta_actual(self):
        return self.arbol.obtener_ruta_nodo(self.directorio_actual)

    def validar_nombre_directorio(self, nombre):
        # Comprobar que el nombre no esté vacío y que no contenga solo espacios o caracteres especiales
        if not nombre or re.fullmatch(r'^\W+$', nombre):
            return False
        return True

