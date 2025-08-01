###
# 02 - Booleans
# Valores lógicos: True (verdadero) y False (Falso)
# Fundamentales para el control de flujo y la logica en programacion
###

print("\nValores Booleanos basicos:")
print(True)
print(False)

print("\nOperadores de comparacion: ")
print("5 > 3:", 5 > 3)      #True
print("5 < 3:", 5 < 3)      #False
print("5 == 5:", 5 == 5)    #True (igualdad)
print("5 != 3:", 5 != 3)    #True (diferencia)
print("5 >= 3:", 5 >= 3)    #True (Mayor o igual que)
print("5 <= 3:", 5 <= 3)    #False (Menor o igual que) 

print("Comparacion de cadenas")
print("'manzana' < 'pera':", "manzana" < "pera") #True
#En la comparacion los compara por letra hace ver que letra o palabra es 'mayor' 

# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)   # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)             # False
print("not False:", not False)            # True

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)





