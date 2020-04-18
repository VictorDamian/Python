#objs iterables; tuplas, string, dicc, listas
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13] 

for valor in lista:
	pass

for valor in range(0, 10, 2):
	pass

#indice=0
for indice, valor in enumerate (lista):
	#print(valor, " tiene el indice: ", indice)
	#indice +=1
	pass

#print(len(lista))

for valor in range(11, len(lista)):
	#print(valor)
	pass

for valor in 'Hola a todo el mundo':
	#print(valor)
	pass

dicc = {'a':10, 'b':300, 'c':1}
for llave, valor in dicc.items():
	print("la llave:", llave, "tiene el valor de: ", valor)