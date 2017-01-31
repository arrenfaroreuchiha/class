# -*- coding: utf-8 -*-
import math
print "ecuacion cuadratica"

class a:
	def b(self):
		a = int(raw_input("numero 1:"))
		b = int(raw_input("numero 2:"))
		c = int(raw_input("numero 3:"))
		x = b ^ 2 - 4 * a * c
		lista = [a, b, c, x]
		return lista
		

	def c(self, a, b, c, x):
		if a == 0:
			print "no se puede dividir"
		else:
			x = (-b) + math.sqrt (b) * (-4 * a * c) / 2 * a  
			x = (-b) - math.sqrt (b) * (-4 * a * c) / 2 * a
			if x > 0:
				print "es pocitiva"
			else:
				print "es negativa"
		return

m = a()
lista = m.b()
eduardo = m.c(lista[0], lista[1], lista[2], lista[3])
