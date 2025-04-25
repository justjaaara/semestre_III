class Nodo:
    def __init__(self, nombre, es_directorio=True):
        self.nombre = nombre
        self.es_directorio = es_directorio
        self.hijos = []
        self.padre = None  # Referencia al nodo padre

    def agregar_hijo(self, nodo):
        nodo.padre = self  # Asignamos el padre cuando agregamos un hijo
        self.hijos.append(nodo)

    def buscar_hijo(self, nombre):
        for hijo in self.hijos:
            if hijo.nombre == nombre:
                return hijo
        return None

    def eliminar_hijo(self, nombre):
        self.hijos = [hijo for hijo in self.hijos if hijo.nombre != nombre]

import re

class Arbol:
    def __init__(self):
        self.raiz = Nodo("/")

    def obtener_ruta_nodo(self, nodo):
        ruta = []
        nodo_actual = nodo
        while nodo_actual:
            ruta.insert(0, nodo_actual.nombre)
            nodo_actual = nodo_actual.padre
        return "/".join(ruta).replace("//", "/")
    
    def buscar_ruta(self, path):
        if path == "/":
            return self.raiz
        nodos = path.strip("/").split("/")
        nodo_actual = self.raiz
        for nombre in nodos:
            nodo_actual = nodo_actual.buscar_hijo(nombre)
            if not nodo_actual:
                return None
        return nodo_actual

    def eliminar_directorio(self, path, forzar=False):
        nodos = path.strip("/").split("/")
        nombre_a_eliminar = nodos[-1]
        nodo_padre = self.buscar_ruta("/" + "/".join(nodos[:-1]))

        if nodo_padre:
            nodo_a_eliminar = nodo_padre.buscar_hijo(nombre_a_eliminar)

            if nodo_a_eliminar:
                if nodo_a_eliminar.hijos and not forzar:
                    return (False, f"El directorio '{nombre_a_eliminar}' contiene otros archivos o carpetas.")
                else:
                    nodo_padre.eliminar_hijo(nombre_a_eliminar)
                    return (True, f"El directorio '{nombre_a_eliminar}' ha sido eliminado.")
            else:
                return (False, f"El directorio '{nombre_a_eliminar}' no existe.")
        return (False, "Ruta no encontrada.")

    def listar(self, path):
        nodo_actual = self.buscar_ruta(path)
        if nodo_actual:
            return [hijo.nombre for hijo in nodo_actual.hijos]
        return "El directorio no existe"

    def listar_recursivo(self, nodo=None, prefijo=""):
        if nodo is None:
            nodo = self.raiz
        for hijo in nodo.hijos:
            print(f"{prefijo}/{hijo.nombre}")
            if hijo.es_directorio:
                self.listar_recursivo(hijo, prefijo + "/" + hijo.nombre)

    def modificar_nombre(self, path, nuevo_nombre):
        nodos = path.strip("/").split("/")
        nombre_a_modificar = nodos[-1]
        nodo_padre = self.buscar_ruta("/" + "/".join(nodos[:-1]))
        if nodo_padre:
            hijo = nodo_padre.buscar_hijo(nombre_a_modificar)
            if hijo:
                hijo.nombre = nuevo_nombre
                return (f"Carpeta '{nombre_a_modificar}' renombrada a '{nuevo_nombre}'")
        else:
            return ("Carpeta no encontrada")

    def cambiar_directorio(self, path):
        nodo = self.buscar_ruta(path)
        if nodo and nodo.es_directorio:
            return nodo
        return None

    def validar_nombre(self, nombre):
        if not nombre or " " in nombre or not re.match("^[a-zA-Z0-9_]+$", nombre):
            return False
        return True

    def buscar_ruta(self, path):
        if path == "/":
            return self.raiz
        nodos = path.strip("/").split("/")
        nodo_actual = self.raiz
        for nombre in nodos:
            nodo_actual = nodo_actual.buscar_hijo(nombre)
            if not nodo_actual:
                return None
        return nodo_actual

    def crear_directorio(self, path, nombre):
        nodo_padre = self.buscar_ruta(path)
        if not nodo_padre or not nodo_padre.es_directorio:
            print(f"Error: La ruta '{path}' no existe o no es un directorio.")
            return
        
        partes = nombre.split("/")
        nodo_actual = nodo_padre
        
        for i, parte in enumerate(partes):
            if i == len(partes) - 1:
                if re.search(r"\.\w+$", parte):
                    es_directorio = False
                else:
                    es_directorio = True
                
                if nodo_actual.buscar_hijo(parte) is None:
                    if len(parte) > 100:
                        print("Error: El nombre del directorio no puede exceder los 100 caracteres.")
                        return
                    nuevo_nodo = Nodo(parte, es_directorio=es_directorio)
                    nodo_actual.agregar_hijo(nuevo_nodo)
                    tipo = "archivo" if not es_directorio else "directorio"
                    print(f"{tipo.capitalize()} '{parte}' creado en la ruta '{self.obtener_ruta_nodo(nodo_actual)}'")

                else:
                    print(f"Error: El {tipo} '{parte}' ya existe en '{self.obtener_ruta_nodo(nodo_actual)}'")
            else:
                hijo = nodo_actual.buscar_hijo(parte)
                if not hijo:
                    nuevo_nodo = Nodo(parte)
                    if len(parte) > 100:
                        print("Error: El nombre del directorio no puede exceder los 100 caracteres.")
                        return
                    nodo_actual.agregar_hijo(nuevo_nodo)
                    print(f"Directorio intermedio '{parte}' creado en la ruta '{self.obtener_ruta_nodo(nodo_actual)}'")
                    nodo_actual = nuevo_nodo
                else:
                    nodo_actual = hijo
