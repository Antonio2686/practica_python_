# Escribe un programa que intente dividir dos números. Si el segundo número es cero,
# captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
# captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

# Se solicita el primer número 
numero1 = input("Ingrese el numero: ")
# Se solicita el segundo número
numero2= input("Ingrese otro numero ")

try:
    
    num1 = float(numero1)
    num2 = float(numero2)
    
    # división
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)

# Capturamos el error , se intenta dividir entre cero
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

# Capturamos el error, el dato ingresado en no es numero
except ValueError:
    print("Error: El primer número ingresado no es válido.")