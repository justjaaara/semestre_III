from src.view.console_view import Consola

def main():
    consola = Consola()
    while True:
        comando = input(f">>{consola.obtener_ruta_actual()} ")
        consola.ejecutar_comando(comando)

if __name__ == "__main__":
    main()
