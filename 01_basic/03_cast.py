###
# 03 - casting of types
# Transformar un tipo de dato a otro
###

# Convertir un tipo de dato a otro es muy útil en Python.
# Para realizar diferentes ejercicios y operaciones que a veces se requieren.
# En Python no puedes hacer conversiones de tipos de datos de forma automática.
# Por ejemplo, si tienes un número y quieres convertirlo a cadena de texto,
# debes hacerlo de forma explícita.


print("Conversión de tipos de datos: ")
# Para explicar porque no se puede hacer de forma automática 
#print(2 + "3")
#print("3" + 3)
# Manda un TypeError porque el error esta en el tipo de dato
# No se deben mezclar los tipos de datos

# Para convertir un tipo de dato a otro, se utilizan las funciones de conversión
# int(), float(), str(), etc.

print(2 + int("3"))  # Convierte "3" a entero
print("3" + str(3))  # Convierte 3 a cadena de texto

# El + es para concatenar cadenas de texto o para hacer una suma de enteros
# No suma las cadenas de texto, las "junta" en una sola cadena, a eso se le puede
# llamar concatenación de cadenas de texto

# Para verificar que el tipo de dato se cambio correctamente simplemente se pone 
# la función type() para ver el tipo de dato

print(type(float("3.1416"))) 
print(type(int("5")))
print(type(str(5)))

# Se puede transformar un float a decimal, pero se pierde la parte decimal

print(type(int(344.23)))
print("Dato float: ", 4123.523, " - transformado a entero: ", int(4123.523))

# Sencilla la tranformación de tipo de dato bool

print(bool(12))
print(bool(0))
print(bool(-23))
# El unico valor que Python considera como false es "0" o "0.0" o "None"

"""
ya no ponde tanto texto xd, se hace dificil de leer xd
"""
# Las cadenas de texto, lo miso
# aquí solo se puede hacer la transformación de un tipo de dato bool a cadena de texto y viceversa
print("Hola")
print(bool("Hola"))
print(bool(""))
print(bool(" "))
# Solo las cadenas vacias, osea sin espacio ni nada, se consideran false
print(type(str(True)))  # Convierte True a cadena de texto
print(type(str(False)))  # Convierte False a cadena de texto

# Obvio no puedes hacer transformaciones de tipos de datos que no tengan sentido
# Por ejemplo, no puedes convertir una cadena de texto a un entero directamente y así con lo demás
# Da un ValueError si intentas convertir algo que no se puede convertir directamente




# Nota rapidita:
# Al convertir un tipo de dato float como 2.5 devuelve un entero 2, porque se redondea al par más cercano
# Explicacçión? Simplemente es una forma matematica para optimizar el espacio de almacenamiento
# pero si ya es 2.51 ahí si es 3

#print(int(2.5))
print(int(2.51))



# Que se vio? 
# entero a cadena de texto
# cadena de texto a entero
# entero a float
# float a entero
# cadena de texto a float
# float a cadena de texto
# cadena de texto a booleano
# booleano a cadena de texto
# booleano a entero
# entero a booleano)