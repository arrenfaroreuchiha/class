# -*- conding: utf-8- -*-
matriz = []
vector = []

class naruto:
	def sasuke(self):
		print "uso del un vector con matriz"
		cantidad = int(raw_input("cuantos numeros:"))
		return cantidad

	def hinata(self, cantidad):
		contador = 0
		for i in range(cantidad):
			numero = int(raw_input("cual es el numero:"))
			#contador += 1
			vector.insert(i, numero)
			vector.sort()
		if cantidad == 9:
			num = 0
			for i in range(0, 3):
				matriz.append([])
				for j in range(0, 3):
					matriz[i].append()
					
		lista = [matriz, cantidad, vector]
		return lista
		
	def sakura(self, lista, cantidad):
		cantidad = lista[1]
		vector = lista[2]
		if cantidad == 9:
			matriz = lista[0]
			cantidad = lista[1]
			print "------------------------------------------------------"
			print "este es su vector en su orden:", vector
			print "este es el numero mayor del vector:", (max(vector))
			print "este es el numero menor del vector:", (min(vector))
			print "esta es la cantidad de numeros que hay en el vector", (len(vector))
			print "esta es su matriz por haber elegido nueve numeros y en su orden:", matriz
			print "este es el numero mayor de la matriz:", (max(max(matriz)))
			print "este es el numero menor de la matriz:", (min(min(matriz)))
			print "------------------------------------------------------"
			for i in range(1):
				for j in range(cantidad):
					print matriz[i][j]
			for i in range(0, 3):
				for x in range(0, 3):
					print matriz(i)				
		else:
			print "------------------------------------------------------"
			print "este es su vector en su orden:", vector
			print "este es el numero mayor del vector:", (max(vector))
			print "este es el numero menor del vector:", (min(vector))
			print "esta es la cantidad de numeros que hay en el vector", (len(vector))

itachi = naruto()
lista = itachi.sasuke()
pein = itachi.hinata(lista)
num = itachi.sakura(pein, lista)

