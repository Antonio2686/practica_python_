# Escribe un programa que intente dividir dos números. Si el segundo número es cero,
# captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
# 
# try:
#      bloque código 1
# except excepción:
#      bloque código 2
dato1 = input("Ingresa el numerador: ")
dato2= input("Ingresa el divisor: ")
try:
        numerador = float(dato1)
        divisor = float(dato2)

        resultado = numerador / divisor

        print(f"El resultado de la división es: {resultado}")

except ZeroDivisionError:

        print("Error: No se puede dividir entre cero.")