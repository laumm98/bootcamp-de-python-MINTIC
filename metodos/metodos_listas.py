lista = list(["hola", "Laura ", 1997])
#nos devuelve la longitud de la lista (cantidad de caracteres)

cadena = "hola"

resultado = len(cadena)

print(resultado)

#agregamos un elemento a la lista

lista.append("Janeth")

print(lista)

#agregamos un elemento a la lista con una posicion determinada 

lista.insert(0, "Adios")

print(lista)

#ahora eliminamos un elemento de la lista

lista.pop(1)

print(lista)

#con el -1 se eleimina el ultimo elemento de la lista y con -2 el antepenultimo 

lista.pop(-1)

print(lista)

#con short ordenamos una lisra de forma descendente mientras los elementos sean numero o booleanos 

listanum = list([1, 5, 2, 7, 9])
listanum.sort()

listanum.sort(reverse=True)

print(listanum)

#con reverse revierte los elementos de una lista

lista.reverse()

print(lista)

#verificando si un elemento se encuentra en la lista 

elemento_encontrado = listanum.index(9)
print(elemento_encontrado)