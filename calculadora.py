# practica de calculadora en python

valor1 = int(input("Ingresa el valor 1 "))
valor2 = int(input("Ingresa el valor 2 "))

operacion = input(
    "Ingresa el tipo de operacion que desea realizar ya sea \"+\", \"-\", \"*\", \"/\": ")

if operacion == '+':
    suma = valor1 + valor2
    print(f"El resultado de su suma es de: {suma}")
elif operacion == "-":
    resta = valor1 - valor2
    print(f"El resultado de su resta es de: {resta}")
elif operacion == "*":
    mult = valor1 * valor2
    print(f"El resultado de su multiplicacion es de: {mult}")
elif operacion == "/":
    div = valor1 / valor2
    print(f"El resultado de su division es de: {div}")
else:
    print("Su operación no está permitida. Intente de nuevo.")

# fin de la practica
