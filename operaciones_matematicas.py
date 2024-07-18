#operaciones matematicas 
a = 10
b = 3
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

print("suma", a + b)
print("resta", a - b)
print("multiplicacion", a * b)
print("division", a / b)

#en python el operador % obtiene el residuo de una division

print("modulo", a % b )

# el siguiente signo es el doble division y el resultado es la parte entera

print("division entera", a // b)

#potencia 

print("potencia", a ** b)

#artificio 

a += 2 
print(a)
a *= 2 
print(a)
a /= 2 
print(a)

operacion1 = 2 + 3 * 4
print(operacion1)
operacion2 = 2 + (3 * 4)
print(operacion2)
operacion3 = (2 + 3) * 4
print(operacion3)
operacion4 = (2 + 3)* (4 ** 2)/ 8 - 1
print(operacion4)