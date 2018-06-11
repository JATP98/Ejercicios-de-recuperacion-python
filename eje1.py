#1.Lee por teclado números y guardalo en una lista, 
# el proceso finaliza cuando metamos un número negativo.
 #Muestra el máximo de los números guardado en la lista, 
 #muestra los números pares.
lista=[]
listapares=[]
numeros=int(input("Dime numeros a introducir: ")
while numeros >0:
	lista.append(numeros)
print(max(lista))
for numero in lista:
	if numero %2 == 0:
		numero.append(listapares)
print (listapares)