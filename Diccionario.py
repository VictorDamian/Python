#almacenar lo que sea
#no se modifica con indices
#las claves deben ser inmutables
dicc = {'a':44, 'b':True, 4:"hola", (1,2):False}
print(dicc)

dicc = {'a':44, 'a':False ,'b':True, 4:"hola", (1,2):False}
print(dicc)

#crea
dicc['c'] = "AshenOne"
print(dicc)

#actualiza
dicc['a'] = 45
print(dicc)

#obtener datos
valor = dicc['a']
print(valor)

#devolver al buscar
valor = dicc.get('z', "No hay")
print(valor)

#eliminar
del dicc[4]
print(dicc)

#solo unas
llaves = dicc.keys()
print(llaves)

llaves2 = list(dicc.keys())
print(llaves2)

llaves3 = tuple(dicc.values())
print(llaves3)

#extendder dicc
dicc_2 = {'x':222, 'w':"pepe"}
dicc.update(dicc_2)
print(dicc)








