###
# 04 - variables
# TLas varibles sirven para guardar datos en memoria
# Python es un lengauje de tipado dinámico y tipado fuerte
###

# AHORA SI VIENE LO BUENO

# Para asginar variables es con lo siguiente:
my_name = "Diego"
print(my_name)


# Tambien las varibles pueden cambiar su valor dependiendo en que orden las declare 

age = 2434
print(age) 

age = 25 # misma varible, diferente valor
print(age)

# Tipo dinámico: el tipo de dato se determina en tiempo de ejecución
# que no tienes que declararlo explícitamente

name = "Diego"
print(name)

name = 98 
print(name)
# Aquí se cambio el tipo de dato de string a int conforme se fue ejecutando el código

# El tipado fuerte significa que no va realizar conversiones automáticas entre tipos de datos
#print(3 + "bb") # TypeError
varibale_1 = "Bienvenido "
varibale_2 = 56
#print(varibale_1 + varibale_2) # TypeError
print(varibale_1 + str(varibale_2))

# Algo que me encanta es el f-string
print(f"Hola {my_name}, tienes {age} años")  # f-string
# Tambien se pueden hacer operaciones dentro del f-string
print(f"Hola {my_name}, tienes {age + 5} años")  # f-string con operación

# Convenciones de nombres de variables
# snake_case: se usa para variables tipicomente

mi_variable_esl_la_mas_perrona = "ok" #snake_case
papa = "ok" # una vaiable corta y normal
mi_variable_esl_la_mas_perrona_1233 = "ok" # una variable larga y con numeros, puede ser corta tambien, pero algo consfusa.

# Algon tambien a mencionar son las constantes
MY_CONSTANT = "Soy una constante"  # Convención de mayúsculas para constantes
print(MY_CONSTANT) # UPPPER_CASE
# LAS CONSTANTES NO DEBERÍAN CAMBIAR SU VALOR, PERO EN PYTHON NO HAY UNA FORMA DE HACERLO REALMENTE, SE PUEDE HACER CON OTRAS COSAS
# USUALMENTE PARA IDENTIFICAR QUE ES CONSTANTE SE ESCRIBE EN MAYÚSCULAS

# NO SE PUEDE USAR NÚMERO PRIMERO EN UNA VARIABLE
#43141_variable = "ko"
#mi-variable = "ko"
#mi variable = "ko"
# NINGUNA DE LAS ANTERIORES SE PUEDE USAR COMO NOMBRE DE VARIABLE

# LAS PALARBAS RESERVADAS NO SE PUEDEN USAR COMO NOMBRE DE VARIABLE
# como por ejemplo: 
# [False, None, True, and, as, assert, break, class, continue, def, del, 
# elif, else, except, finally, for, from, global, if, import, in, is, lambda, 
# nonlocal, not, or, pass, raise, return, try, while with]

# Ahora un apartado importante 
# la anotaciones de tipos

user_logged: bool = True 
print(user_logged)
# Aquí lo que pasa es una notoación sirve para documentar
# o darle una buena estructura a tu archivo de de Python
# si intentamos poner otra vez esa varible como otro tipo de dato marcaría un error inivicible le digo yo xd

#user_logged = 23123 # este visualización de error se activa en las configuración de VScode en el apartado "typecheck"
print(user_logged) # No hay errorr en la terminal porque simplemente es una forma de que el editor te avisa que esa varible es de otro tipo
# el tipo que le asigne yo antes
# puedes asignar esa anotación antes o despues de haber creado la variable