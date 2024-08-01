a = [1, 2, 3, 4, 5]
b = a 
print (a)
print (b)
del a[0]
print (a)
print (b)
print(id(a)) #id sirve para mostrar el espacio en memoria que ocupa una variable 
print(id(b))

#METODO SLIDE no sirve para acceder a espacios de memoria diferente cuando queremos copiar una variable

c = a [:]
print(id(a)) 
print(id(b))
print(id(c))

a.append(6)
print (a)
print (b)
print (c)