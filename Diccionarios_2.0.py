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



#TALLER COLABORATIVO

contacts = { "nombre": "Laura Montaña",
                    "edad": 27,
                    "telefono": 3157849494,
                    "signo zodiacal": "LEO",
                    "Pelicula fav": "no tengo",
                    "cancion fav": "Be Yourself - Audioslave",
                    "comida fav": "Pasta a la carbonara",
                    "¿Cuál es tu lugar soñado para unas vacaciones?": "Bali",
                    "¿Qué habilidad secreta te gustaría tener?": "Telequinesis",
                    "¿Tienes algún talento oculto o pasatiempo inusual?": "Reposteria",
                    "¿Quién es tu héroe o persona que admiras más y por qué?": "ninguno en especial",
                    "¿Cuál es el libro que más te ha impactado y por qué?": "El TUNEL - Ernesto Sabato",
                    "¿Si pudieras cenar con cualquier persona, viva o muerta, quién sería y qué le preguntarías?": "Cenaria con mmmm Elon Musk y le preguntaria cual es la clave del exito",
                    "¿Qué logro personal te enorgullece más hasta ahora?": "mi titulo profesional"

}

resultado = contacts.values()
print(resultado)



