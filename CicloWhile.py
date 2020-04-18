contador = 0
con = True

while con:
	print(contador)
	contador+=1

	if contador == 5:
		print("este es cinco")
		continue
	elif contador == 6:
		con = False
else:
	print("Termino")

