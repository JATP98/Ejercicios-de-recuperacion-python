#Escribe un programa que permita crear una
 #lista de palabras. Para ello, el programa 
 #tiene que pedir un número y luego solicitar 
 #ese número de palabras para crear la lista. 
 #Por último, el programa tiene que escribir la lista
lista=[]
prueba=int(input("Dime cuantas palabras quieres meter: "))
contador=0
while contador != prueba:
	palabra=input("Introduce una palabra: ")
	contador=contador+1
	lista.append(palabra)
print(lista)