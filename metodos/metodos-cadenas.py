cadena1 = "HOLA,SOY,LAURA,MONTAÑA"
cadena2 = "Gracias por aprender python con nosotros"
#print(dir(cadena1))

resultado = cadena1.lower() #con upper colocas todas las letras en mayuscula
print(resultado)

primera_letra_mayus =cadena1.capitalize()
print(primera_letra_mayus)

busqueda_find = cadena1.find("Z")
if busqueda_find == -1:
    print("No se encuentra la letra")
else:
    print(busqueda_find)

busqueda_index =cadena1.index("L")
print(busqueda_index)

es_numerico =cadena1.isnumeric()
if es_numerico == True:
    print("Es numerico")
else:
    print("No es numerico")

es_alfa_numerico = cadena1.isalpha()
if es_alfa_numerico == True:
    print("Es alfa numerico")
else:
    print("No es alfa numerico")

contar_coincidencia = cadena1.count("A")
print(contar_coincidencia)

contar_caracteres = len(cadena1)
print(contar_caracteres)

empieza_con = cadena1.startswith("H")
if empieza_con == True:
    print("Si empieza con H")
else:
    print("No empieza con H")

termina_con = cadena1.endswith("A")
if termina_con == True:
    print("Si termina con A")
else:
    print("No termina con A") 

cadena_nueva = cadena1.replace("SOY", "yo me llamo")
print(cadena_nueva)

cadena_separada =cadena1.split(",")
print(cadena_separada)
print(type(cadena_separada))
print(cadena_separada[0])