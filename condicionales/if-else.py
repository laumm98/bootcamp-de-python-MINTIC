#Esta es la estructura de un condicional 
# if condicion: si esto es True 
#accion 
#la accion se ejecuta 
# if false: si esto es falso 
# accion
#la accion no se ejecuta

edad = 17 
if edad >= 18:
    print("Puedes pasar")

else: print("Eres menor de edad, no puedes pasar \n")

contraseña_almacenada = "JheysonGalvis"
contraseña_escrita = "JheysonGalvis"

if contraseña_almacenada == contraseña_escrita:
    print("Hay coincidencia \n")

else: print("No hay coincidencia \n")

ingreso_mensual = 100000

if ingreso_mensual > 1000:
    print("Estas bien economicamente en Latinoamerica \n")

if ingreso_mensual > 10000:
    print("Estas bien en cualquier parte del mundo \n")

else: print("estas en la pobreza \n")

#aprender a utilizar el elif
ingreso_mensual = 12000

if ingreso_mensual > 1000:
    print("Estas bien economicamente en Latinoamerica \n")

elif ingreso_mensual > 10000:
    print("Estas bien en cualquier parte del mundo \n")

else: print("estas en la pobreza \n")

#aprender a utilizar varios elif
ingreso_mensual = 90

if ingreso_mensual > 10000:
    print("Estas bien economicamente en cualquier parte del mundo \n")

elif ingreso_mensual > 1000:
    print("Estas bien en Latinoamerica \n")

elif ingreso_mensual > 500:
    print("Estas bien en Colombia \n")

elif ingreso_mensual > 200:
    print("Estas bien en Peru \n")

else: print("estas en la pobreza \n")

#aprender a utilizar elif anidados
ingreso_mensual = 12000
ahorro_mensual = 6000

if ingreso_mensual > 10000:
    
    if ahorro_mensual < 7000: 
        print("Ahora si estas bien \n")
    else: print("Estas gastando mucho dinero, ahorra mas")


elif ingreso_mensual > 1000:
    print("Estas bien en Latinoamerica \n")

elif ingreso_mensual > 500:
    print("Estas bien en Colombia \n")

elif ingreso_mensual > 200:
    print("Estas bien en Peru \n")

else: print("estas en la pobreza \n")

