numbers = {1: "uno", 2:"dos", 3: "tres"} #creando un diccionario

print(numbers)
print(numbers[1]) #imprime el valor de la llave 1
print(numbers[2]) #imprime el valor de la llave 2

information = { "nombre": "Laura",
               "apellido": "Montaña",
               "estatura": 1.68,
               "esta_feliz": True

}

print(information)

del information["apellido"]
print(information)

claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)

