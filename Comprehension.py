#crea listas de manera sencilla
"""
lista = []
for valor in range(0, 101):
	lista.append(valor)
print(lista)
"""
lista = [ valor for valor in range(0, 101) if valor %2==0] #valor, #ciclo
#print(lista)

tupla = tuple(( valor for valor in range(0, 101) if valor %2 != 0))
#print(tupla)

dicc = { indice:valor for indice,valor in enumerate(lista) if indice <10}
print(dicc)