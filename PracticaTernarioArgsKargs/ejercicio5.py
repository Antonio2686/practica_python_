# Imprimir un mensaje de error si no se pasan suficientes argumentos

def validar_argumentos(min_args, **kwargs):
    if len(kwargs) < min_args:
        return f"Error: se requieren al menos {min_args} argumentos, pero solo se pasaron {len(kwargs)}."
    else:
        return f"Argumentos válidos: {kwargs}"

# Ejemplo de uso
print(validar_argumentos(3, nombre="Juan", apellido = "Perez"))  # Error: se requieren al menos 3 argumentos, pero solo se pasaron 2.
print(validar_argumentos(2, nombre="Juan", apellido="Gonzalez", provincia="Buenos aires")) # Argumentos válidos: 


