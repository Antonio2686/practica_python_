# un mensaje de error al usuario.
# Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
# FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
# embargo, también intenta crear el archivo si no existe

prueba = "prueba.txt"

try:
    # "r" lee el archivo
    with open(prueba, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:", contenido)
except FileNotFoundError:
    print(f"Error: El archivo '{prueba}' no existe.")
    print("se creara el archivo...")
    try:
        # "W"escribe y crea el archivo si no existe
        with open(prueba, "w") as archivo:
            archivo.write("se escribe el archivo.\n")
        print("El archivo se creo.")
    except Exception as e:
        print("Ha ocurrido un error al crear el archivo:", e)