to_do =["Alistar la pelicula", 
        "freir el maizpira",
        "preparar pasabocas"]

print(to_do)

mi_dia =["preparar a mi hija para el colegio",
            "trabajar",
            "ir al gimnasio",
            "comer",
            "trabajar"]

print(mi_dia)

numbers = [1, 2, 3, 4, "cinco"]
print(numbers)
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento: ", mix[0])
print("Segundo elemento: ", mix[1])
print("Tercer elemento: ", mix[2])
print("Cuarto elemento: ", mix[3])
print("Ultimo elemento: ", mix[-1])

print(mix[0:2])
print(mix[:2])

mix.append(False)
print(mix)

mix.append("Laura Montaña")
print(mix)

mix.insert(1,["a", "b"])
print(mix)

print(mix.index(["a", "b"]))
print(mix)

numbers = [1, 2, 100, 90, 45, 3, 4, 5]
print(numbers)
print("mayor: ", max(numbers))
print("menor: ", min(numbers))
del numbers[-1]
print(numbers)
del numbers [:2]
print(numbers)
del (numbers)
#print(numbers)