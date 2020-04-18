miString1 = "Hola"
miString2 = "a todo el mundo"

stringR ='{a} {b}'.format(a = miString1, b = miString2)

""" FUENTES 
stringR=stringR.lower()
stringR=stringR.upper()
stringR=stringR.title() 
print(stringR) """

""" BUSQUEDA """
pos = stringR.find('todo')
print(pos)
print(stringR[7])

count = stringR.count('o')
print(count)

new_string = stringR.replace('a','x')
print(new_string)

new_string = stringR.split(' ')
print(new_string)
