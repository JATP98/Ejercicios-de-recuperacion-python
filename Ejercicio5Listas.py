lista1=[]
numeropalabras=int(input("Introduce el numero de palabras:"))

for i in range(numeropalabras):
	palabra=input("Introduzca una palabra:")
	lista1.append(palabra)


buscar=input("Introduce la palabra a buscar en la lista:")
veces=lista1.count(buscar)
print("Aparece en la lista:",veces)