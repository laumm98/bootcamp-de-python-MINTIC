#El primer dato compuesto que veremos sera la lista 

lista = ["Laura Montaña", "tecnotutoriales Jheyson Galvis", True, 1.68]
print(lista)
print(lista[1])

#modificar lista 

lista[3]= "Jan"
print(lista[3])

#La tupla es una lista que no se puede modificar 

tupla =("Laura Montaña", "tecnotutoriales Jheyson Galvis", True, 1.68)
print(tupla[1])

# tupla(1) = "tips TIC al paso" ----> esto no se puede hacer 
#Creando un conjunto o set
#un conjunto no admite elementos duplicados

conjunto = {"Laura Montaña", "tecnotutoriales Jheyson Galvis", True, 1.68, 1.68}
print(conjunto)

#creando un diccionario 

diccionario ={
    "nombre": "Laura",
    "apellido": "Montaña",
    "estatura": 1.68,
    "esta feliz": True
}

print (diccionario ["esta feliz"])
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["estatura"])