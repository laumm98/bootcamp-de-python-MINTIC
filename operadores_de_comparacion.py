es_igual_que = 5 == 5
print(es_igual_que)

es_diferente_que = 5 != 6
print(es_diferente_que)

es_mayor_que = 5 > 6
print(es_mayor_que)

es_mayor_o_igual_que = 5 >= 6 
print(es_mayor_o_igual_que)

es_menor_que = 5 < 6
print(es_menor_que)

es_menor_o_igual_que = 5 <= 6
print(es_menor_o_igual_que)

#calculos combinados 

a = 5
b = 10
c = 20

comparacion = a + b == c
print(comparacion)

edad_hija_mayor = 3
edad_hija_menor = 1 
edad_mama = 27

comparacion_edad = edad_hija_mayor + edad_hija_menor != edad_mama
print(comparacion_edad)

#compara usuarios 

contraseña_almacenada = "123456"
contraseña_escrita = "123456"
print(contraseña_almacenada == contraseña_escrita)

contraseña_almacenada = "123456"
contraseña_escrita = '123456'
print(contraseña_almacenada == contraseña_escrita)

contraseña_almacenada = "123456"
contraseña_escrita = '''123456'''
print(contraseña_almacenada == contraseña_escrita)