numpalabras=int(input("Introduzca el numero de la palabras:"))
lista1=[]

for i in range (numpalabras):
	palabra=input("Introduce una palabra:")
	lista1.append(palabra)
	


buscar1=input("Introduce la primera palabra a sustituir:")
buscar2=input("Introduce la segunda palabra para sustituir:")

lista1[lista1.index(buscar2)] = buscar1
print(lista1)