numpalabras=int(input("Introduzca el numero de la palabras:"))
lista1=[]

for i in range (numpalabras):
	palabra=input("Introduce una palabra:")
	lista1.append(palabra)

rmpalabra=input("Que palabra quieres borrar?")
lista1.remove(rmpalabra)
print(lista1)