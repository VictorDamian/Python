fruta = "kiwi"
fruta = "manzana"

if fruta == "2" : 
	print("si es kiwi")
elif fruta == "manzana" :
	print("es otra manzana")
elif fruta == "manzana" :
	pass
else :
	print("no es l")


msj = "bien" if fruta == 'kiwi' else "no es"
print(msj)

#si no tiene valor, es falso
valor = None
valor_2 = 20

if valor or valor_2 > 20:
	print("es verdad")
else:
	print("no es verdad")