# Dada una lista de números enteros
# (guarda la lista en una variable) y un entero k,
# escribir un programa que:
#Cree tres listas listas, una con los menores, otra con los 
#mayores y otra con los iguales a k.
#Crea otra lista lista con aquellos que son múltiplos de k.

listaenteros=[1,2,3,4,5,6,4,6,4,7,8,9,4]
numerok=int(input("Introduce un numero para comprobar: "))
listamenores=[]
listamayores=[]
listaigual=[]
for numeris in listaenteros:
	if numeris <numerok :
		listamenores.append(numeris)
	elif numeris >numerok :
		listamayores.append(numeris)

	else:
		listaigual.append(numeris)
print("numeros iguales: ", listaigual)
print("numeros menores: ", listamenores)
print("numeros mayores: ", listamayores)
