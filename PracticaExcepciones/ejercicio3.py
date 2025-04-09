# Escribe un programa que intente acceder a una clave que no existe en un
# diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

# Creamos un diccionario persona
persona = {"nombre": "antonio", "apellido": "Lugo" }

# Intentamos acceder a la edad de la persona , pero no existe en el diccionario
try:
    edad = persona["edad"]
    print("La edad de la persona es:", edad)
except KeyError:
    print("Error: no existe en el diccionario.")
