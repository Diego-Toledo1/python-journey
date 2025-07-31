###
# 05 - input()
# La función input() sirve para pedir informacíon al usuario a través de la consola
###

# Lo que hemos visto hasta ahora se podría decir como un mostrar información
# Ahora toca ofrecer la informacíon

print("Hola, ¿Cuál es tu nombre?")
nombre = input()


print(f"Hola, {nombre} un gusto en saludarte") 

age = (input("¿Cuántos años tienes?\n")) # Aquí necestia un salto de linea. porque el input se pondrá directamente despues del string osea de "tienes?..."
#print(f"Vas a tener dentro de 20 años {age + 20}") # Esto esta mal porque la función input() guarda el valor en tipo string
# solo tienes que hacer una conversión "int()"
print(f"Vas a tener dentro de 20 años {int(age) + 20} años")


# Ahora toca ver como obtener multiples valores con .split()
print("Obtener múltiples valores a la vez")
country, city = input("¿En que pais y cuidad vives?\n").split() #Aquí hay que poner una separación a la hora de introducir los datos en la consola
print(f"Vives en la cuidad de {city} y eres de {country}")


