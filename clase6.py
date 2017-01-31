# -*- coding: utf-8 -*-
print "numero primo o no primo"

class a:
	def b(self):
		numero = int(raw_input("numero:"))
		return numero
	def c(self, numero):
		i = 1
		for i in range(1):
			contador = numero % 2
			if contador == 1:
				print "el numero es primo"
			elif contador > 1:
				contador = numero % i
			elif contador == 0:
				print "el numero no es primo"
		return

d = a()
numero = d.b()
e = d.c(numero)

