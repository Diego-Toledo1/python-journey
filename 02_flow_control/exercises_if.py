###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
"""
numero_1 = input("Introduce el primero numero: ")
numero_2 = input("Introduce el segundo numero: ")

if numero_1 > numero_2:
    print(f"\nEl numero {numero_1} es mayor que {numero_2}\n")
else:
    print(f"El numero {numero_2} es mayor que {numero_1}")
"""

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
"""
print(" /// Calculadora simple ///\n")
print(" /// Para realizar la operacion tienes que ingresar dos numeros ///\n")
print(" /// Tambien tienes que elejir la operacion que deseas hacer: (+, -, *, /)")

numero_1 = input(" /// Ingresa el primero numero: ")
numero_2 = input(" /// Ingresa el segundo numero: ")

operacion = input(" /// Ingresa la operacion: ")
print(f"Numeros que elejiste // numero 1: {numero_1}, numero 2: {numero_2} \n")
print(f"La operacion que elejiste fue: {operacion}\n")

if operacion == "+":
    print(f"El resultado de la suma es: {int(numero_1) + int(numero_2)}")
elif operacion == "-":
    print(f"El resultado de la resta es: {int(numero_1) - int(numero_2)} ")
elif operacion == "*":
    print(f"El resultado de la multiplicacion es: {int(numero_1) * int(numero_2)} ")
elif operacion == "/":
    print(f"El resultado de la division es: {int(numero_1) / int(numero_2)} ")
else:
    print("Numero invalido")
"""

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
"""
anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
"""

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Introduce una edad: \n"))

if edad <= 2 and edad >= 0:
    print("Eres un bebo!!!")
elif edad >= 3 and edad <= 12:
    print("Niño robloxini!!") 
elif edad >= 13 and edad <= 17:
    print("PELOOOOOS")
elif edad >= 18 and edad <= 64:
    print("A CHAMBEARRR!!!")
elif edad > 65:
    print("A HUELE A POLVO AQUI")
else: 
    print("EDAD NO VALIDA")
