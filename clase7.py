# -*- coding: utf-8 -*-
print "multiplos de 3"

class a:
	def b(self):
		numero = int(raw_input("cantidad de numeros:"))
		return numero
	def c(self, numero):
		i = 0
		contador = 0
		for i in range (numero):
			numero2 = int(raw_input("numero:"))
			contador2 = numero2 % 3
			if contador2 == 0:
				print "es el multiplo de 3"
				contador = contador + numero2
			else:
				print "no es multiplo de 3", numero2
		contador
		return contador

z = a()
numero = z.b()
contador = z.c(numero)
print "suma de numeros de multiplos de 3:", contador