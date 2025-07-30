###
# 01 - print()
# Esto es un módulo de Python que imprime un mensaje en la consola.
# La función print() es una de las funciones más utilizadas en Python, ya que nos permite mostrar información en la consola.
# En este archivo estoy viendo cómo usar la función print() de manera básica y algunos de sus argumentos
###

print("Hello, World!") #Simple un solo "Hello, World!" en la consola
print('Se pueden usar comillas simples o dobles') #Al impirmir perfectamente se pueden usar comillas simples o dobles, depende como te acomodes
print("El", "anime", "es", "algo", "increible") #Aqui le estamos pasando varios argumentos a la función print, los cuales serán separados por un espacio en blanco por defecto
# En la linea de arriba se muestra como se pueden pasar varios argumentos a la función print, los cuales serán separados por un espacio en blanco por defecto.

# Puede a ver mas separadores en el print, como por ejemplo:

print("Ah", "Que", sep="-") #El argumento sep nos permite cambiar cambiar el separador por defecto que tiene la funcion print, aqui voy a experimentar un poco con el arguemnto
print("Separacion", "por", "punto", sep=".") # Aquí hice uso del argumento sep para cambiar el separador por un punto
print("Separacion", "por", "asterisco", sep="*") # Aquí hice uso del argumento sep para cambiar el separador por un asterisco

# Pero obviamente como se ve sigue junto, ¿hay separación?, si, pero no es visible, en el argumento sep tenemos que poner manualmente la separación
print("Separación", "por", "espacio", sep=" ") # Aquí hice uso del argumento sep para cambiar el separador por un espacio, que es el predeterminado cuanod solo pones las ","

###

# También podemos cambiar el final de la impresión con el argumento end, que por defecto es un salto de línea

print("Hey", "que pasa", end="") # Aquí use el end para hacer que no se agregue un salto de línea al final de la impresión, el salto de linea se nota cuando se imprime el siguiente print
print("¿Todo bien?") 

# Se puede poner adentro del end cualquier cosa, como por ejemplo un espacio, un salto de línea, un asterisco, un punto, una guion o lo que sea porque es un texto al final de cuentas
#Ejemplos:

print("Cuando", "usas", "la", "vandal", end=" ")
print("en", "valorant", "mataras", "mas", "facil")

print("Cuando", "usas", "la", "vandal", end=".")
print("en", "valorant", "mataras", "mas", "facil")

print("Cuando", "usas", "la", "vandal", end="*")
print("en", "valorant", "mataras", "mas", "facil")

print("Cuando", "usas", "la", "vandal", end="HOLA")
print("en", "valorant", "mataras", "mas", "facil")

print("Cuando", "usas", "la", "vandal", end=":-:")
print("en", "valorant", "mataras", "mas", "facil")

print("Cuando", "usas", "la", "vandal", end="\n") # Aquí use el end y un salto de linea "\n" para que al final de la impresión se agregue un salto de línea, así es como se representa el salto de linea tambien 
print("en", "valorant", "mataras", "mas", "facil")

# El end por defecto renderiza un salto de línea, pero podemos cambiarlo a lo que yo quiera jojojo

###

# Tambien se pueden usar los arguemntos en un solo print, como por ejemplo:
print("Hola", "mundo", sep=" ", end="!!!") # Aquí estoy usando los argumentos sep y end en un solo print, el sep es para separar las palabras por un espacio y el end es para que al final de la impresión se agregue "!!!"
print("apoco si pa")

###

###

# Aquí podemos imprimir tambien numeros, booleanos, listas, tuplas, diccionarios, etc.
# Pero eso más adelante que todavia no llego al tema xd
# imprimir un número

print(12)
print(12, 13, 15, 15)
print(12, 13, 15, 15, sep="-")
print(56584,323,323,23) # Aqui que descubri, simplemente es estetica el espacio que hay entre la "," y el numero, no afecta en nada al print, es solo estetica
print(423, 234,5, 62, sep="*", end=" ")
print(555555555)

# Aquí se imprime más cosas boolean 
print(True) # Imprime True
print(False) # Imprime False
print(True, False) # Imprime True y False separados por un espacio
print(True, False, sep="-") # Imprime True y False separados por un guion
print(True, False, sep="*", end=" ") # Imprime True y False separados por un asterisco y al final un espacio
print(121212, "Texto", sep="****")

# Lo demas lo vere más adelante. 
