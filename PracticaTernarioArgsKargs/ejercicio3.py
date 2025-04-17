# Determinar si un número es par o impar
dato =input("Ingresa un número: ")
num = int(dato)

print(f"El número Par" if num % 2 == 0 else "El número Impar")