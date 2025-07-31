###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###
# curso de midudev: https://youtu.be/TkN2i-_4N4g?si=a-B7q920-Hs--z2O
# ejercicios sacados de su github: https://github.com/midudev/curso-python/blob/main/01_basic/exercises.py

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Mi nombre es Diego Eduardo")

print("Mi cuidad es Cuernavaca")


print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print("12345")
print(type("12345"))
print(int("12345"))
print(type(int("12345")))
print(float(12345))
print(type(float(12345)))

print(3.99)
print(type(3.99))
print(int(3.99))
print(type(int(3.99)))
# ¿Qué ocurre? Básicamente ocurre que depués del punto decimal todo se elimina lo ignora completamente. 

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

name = "Diego"
age = 19
height = 1.80


print(f"Hola, me llamo {name}, tengo {age} años y mido {height} metros")


print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1\n")

pi = 3.14159
print(pi)
pi_round = round(pi)
print(pi_round)
print(pi_round // 2)
pi_round_resul = pi_round // 2
print(f"El resultado es: {pi_round_resul}")


# Voy a simplificarlo
print("\n---- Simplificación ----")
pi = 3.14159
print(f"El número PI redondeado es: {round(pi)}")
print(f"Ahora vamos a dividir el número PI redondeado entre 2 - '3.14159 // 2' - : {round(pi) // 2}")

print("--------------")


