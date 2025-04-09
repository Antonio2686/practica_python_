#Escribe un programa que intente sumar un número y una cadena. Si se produce un error
# de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario

dato1 = input("Por favor, ingrese un numero: ")
dato2 = input("Por favor, ingrese una palabra: ")


try:
    numero = int(dato1) # Un número cualquiera
    cadena = dato2  # Una cadena cualquiera
    resultado = numero + cadena  # Intento de suma
    print(f"El resultado de la suma es: {resultado}")
except TypeError:
    print("Error: No se puede sumar un número y una cadena.")

