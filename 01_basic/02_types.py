###
# 02 - types()
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
# Aquí en los números enteros grandes, en otros lenguajes como JavaScript, se puede manejar de diferente forma...
# Al poner "3129074012647109320" + 1 te dará un resultado diferente al que es común porque los bits se manejarían de diferente forma
# Aquí en Python, no hay problema con los números enteros grandes, ya que Python maneja enteros de precisión arbitraria.

###
# Expliación:
# Cuando puse la función type() dentro del print, me devuelve el tipo de dato de lo que le pase como argumento, en este caso un número entero.
# Por lo tanto, al imprimir type(4), me devuelve <class 'int'>, que es el tipo de dato entero en Python.
# Esto es útil para verificar el tipo de dato de una variable o valor en Python.
# Nos menciona que es de la clase 'int'
# El tipo de datos 'type' de este valor '(0)' es un entero, por lo que se imprime <class 'int'>.
###

# También un tipo de datos son los flotantes, que son practimannte decimales
print("float:")
print(type(4.0))
print(type(0.0)) # Aquí aunque en realidad tenga como valor solo un 0, sigue siendo un número decimal, por lo que es de tipo float
print(type(-4.0))
print(type(1000.0)) # → <class 'float'>
print(type(1e3)) # Aquí estoy usando notación científica, que es una forma de representar números muy grandes o muy pequeños, en este caso 1e3 es igual a 1000.0

# Otro tipo de dato sería los complejos, que son números que tienen una parte real y una parte imaginaria
print("complex:")
print(type(4 + 5j)) # # Aquí la parte real es el 4 y la parte imaginaria es el 5j, que es la forma de representar los números complejos en Python
# Esto se usa más para cosas matemáticas avanzadas, como en ingeniería o física o en programación científica → <class 'complex'>

# Otro tipo de dato que es importante a mi parecer es el string, las cadenas de texto
print("str:")
print(type("Comillas dobles"))
print(type('Comillas simples')) 
print(type("""
Comillas triples, que permiten
escribir varias líneas de texto
es una multi linea
""")) # → <class 'str'>

# Otro que es bastante importante es el booleano, que son los valores True y False
print("bool:")
print(type(True))  # Verdadero
print(type(False)) # Falso
# Aquí un detalle es que tambien puede devolver un tipo booleano cuando se hace una comparación logica
print(type(4 > 2))  # True, porque 4 es mayor que 2
print(type(4 < 2))  # False, porque 4 no es menor que 2 → <class 'bool'>

# Hay otro tipo de dato que es NoneType, que representa la ausencia de valor o un valor nulo
print("NoneType:")
print(type(None))  # None es un objeto especial en Python que representa la ausencia de valor → <class 'NoneType'>

