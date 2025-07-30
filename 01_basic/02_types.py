###
# 01 - print()
# En este archivo voy a ver los tipo de datos que existen en Python.
# De acuerdo al curso en el que estoy aprendiendo, existen 6 tipos de datos primitivos:
# int, float, str, bool, list y dict, NoneType, complex, tuple, range, set.....
###

"""
Así se puede usar una cadena de texto en Python, de tipo string
pero si no se le asigna a una variable, no se puede usar como 
un comentario
depende de gustos
"""

# Lo mismo, aplicando lo aprendido, tenemos que aprender a imprimir los tipos de datos, con lo que esta en el archivo 01_basic/01_print.py

# Estos son los tipos de datos enteros:
print("int:")
#print(212)
#print(2)
#print(0)
#print(-312)

# Para que no estorbar se comenta los prints de arriba

print("Vamos a imprimir tipos de", "datos", "enteros: ", sep=" ", end="\n") 
print(type(4))
print(type(0))
print(type(-4))
print(type(1000))
print(type(3129074012647109320))

###
# Expliación:
# Cuando puse la función type() dentro del print, me devuelve el tipo de dato de lo que le pase como argumento, en este caso un número entero.
# Por lo tanto, al imprimir type(4), me devuelve <class 'int'>, que es el tipo de dato entero en Python.
# Esto es útil para verificar el tipo de dato de una variable o valor en Python.
# Nos meciona que es de la clase 'int'
# El tipo de datos 'type' de este valor '(0)' es un entero, por lo que se imprime <class 'int'>.
###
