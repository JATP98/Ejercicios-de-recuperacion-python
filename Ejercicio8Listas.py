numpalabras1=int(input("Introduzca el numero de la palabras para la lista1:"))
numpalabras2=int(input("Introduzca el numero de la palabras para la lista2:"))
lista1=[]
lista2=[]

for i in range (numpalabras1):
	palabra=input("Introduce una palabra para la lista1:")
	lista1.append(palabra)

for i in range (numpalabras2):
	palabra=input("Introduce una palabra para la lista2:")
	lista2.append(palabra)

	if palabra in lista1:
		lista1.remove(palabra)

print("Palabras de la lista 1",lista1)
print("Palabras de la lista 2",lista2)
