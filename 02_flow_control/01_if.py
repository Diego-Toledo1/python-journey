###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumple ciertas condiciones.
###
import os 
os.system("clear") #Esto sirve para limpiar la terminal y no sea tan molesto. 
# Vamos a pasar a las sentencias condicionales ahora si viene lo que hace a Python, Python
print("\n Sentencia simple condicional")

age = 16
if age >= 18: # Aqui los dos puntos es como decir un "ENTONCES HAZ ESTO..."
    print('Eres mayor de edad.') #Aqui va el mensaje, Python funciona por tabulaciones
#Si pones aqui el primer print da error
    #Si lo pones aqui no da error
    #Puedes poner mas de un string
    print("Felicidades")

# print("Estoy fuera del condicional if")

#Ojo piojo
#Si pones un print afuera literal del if, como es ponerlo fuera? es sin tabulaciones
#Si hago que el condicional if no se cumpla, no imprimira el 'Eres mayor de edad'
#ni el 'Felicidades'
#pero si el 'Estoy fuera del condicional if' porque esta fuera del condicional


print("\nSentencia condicional else")

age_2 = 20

if age_2 >= 45:
    print("Vas para el quinto piso")
else:
    print("Estas a tiempo de empezar hacer ejercicio")

print("\nSentencia condicioanl elif")

calificacion = 1

if calificacion >= 9: # Siempre tiene que llevar el dos puntos :
    print("Sobresaliente, puedes mejorar crack ;p")
elif calificacion >= 7: # Aqui hay que poner otra condicion para que funcione el elif
    print("Ufff, no estudiaste eh... echale mas ganitas CRACK!")
elif calificacion >= 6: # El elif es como decir, sino haz esto
    print("Aqui si no como ayudarte pa, para mi no pasas.")
else: # Aqui el else es decir, si no se cumple ninguna de las anteriores pues imprime esto
    print("Ni me hables, bobo...")
# O perfectamente no puedes poner el else y simplemente no se ejecutara nada en dado caso
# que nose cumpla ninguna de las condiciones de la parte de arriba. 

# En las condiciones de arriba son condicones que si o si te devolveran un True o False
# PORQUE HAECES LA CONDICIONES SI SE CUMPLE ESTO HAZ ESTO


# Vamos con los operados logicos
print("\nCondiciones multiples")

edad = 17
tengo_licencia = True
# el operador 'and' sirve para hacer una comparacion y solo se cumplira si ambos lados son verdaderos
# LEYES MAS ESTRICTAS
if edad >= 18 and tengo_licencia:
    print("Puedes conducir papu!!")
else:
    print("Prepara la mordida bobo 🥱")

# vamos con el operador 'or' 
# este operador logico, es si una de las dos condiciones es 'True' toda la condicion 'PASA'

# Pais de Colombia, diferentes leyes
if edad >= 18 or tengo_licencia:
    print("\nPUEDES CONDUCIR LIBREMENTE ;D")
else:
    print("No puedes conducir ni pagando... o si?????")

# Ahora vamos con el operador 'not' 

es_fin_de_semana = False
#El operador 'not' es voltear literalmente la condicion
#si la varibale es_fin_de_semana es false, pasa a True y se cumple la condicion
if not es_fin_de_semana:
    print("Orale we que hay que chambear")

if not es_fin_de_semana:
    print("Orale we que hay que chambear")
else:
    print("GOOO DIAMANTE EN LOL")


# Un consejo que me da midudev es siempre simplificar el condicional

# Tambien como se vio en el archivo cast, los numeros actuan como True y False numero > y < a 0 es True y Numero 0 es False

numero = 4
if numero:
    print("entra en la condicion")

numero2 = 0
if numero2:
    print("no entra en la condicion porque es false")
print("Look")

# igual con las cadenas de texto

nombresito = "Manuelas" #True
if nombresito:
    print("La cadena de texto no esta vacia")

nombresito2 = "" #False
if nombresito2:
    print("La cadena si esta vacia por ende no imprime nada")
print("cadena vacia")


print("\n La condicion ternaria")
#Es una forma concisa de un if-else en una linea de codigo
# [codigo si cumple la condicion] if [condicion] else [codigo si no cumple]

edad = 18

mensaje = "Es mayor de edad" if edad >18 else "Es menor de edad"
print(mensaje)