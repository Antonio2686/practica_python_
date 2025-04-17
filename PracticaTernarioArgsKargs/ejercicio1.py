# Calcular el mayor de dos números ingresados por teclado usando un operador
# ternario

# Solicitar los números al usuario
dato1 = input("Ingresa el primer numero: ")
dato2 = input("Ingresa el segundo numero: ")
num1 = int(dato1)
num2 = int(dato2)

# Usar operador ternario para determinar el mayor
print("El mayor primer numero" if num1 > num2 else "el mayor es el segundo" if num2 > num1 else "son iguales")