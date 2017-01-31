# -*- coding: utf-8 -*-
print "multiplos de 3"
class entra:
	def inicio(self):
		numero = int(raw_input("cantidad de numeros:"))
		return numero
		
	def mitad(self, numero):
		i = 1
		contador = 0
		for i in range (numero):
			numero2 = int(raw_input("numero:"))
			contador2 = numero2 % 3
			if contador2 == 0:
				print "es multiplo de 3"
				contador = contador + numero2
				#print "la suma de los multiplos de 3 es:", contador
			else:
				print "no es multiplo de 3:", numero2
		contador
		return contador
			
objeto = entra()#intancias de la clases al objeto
numero = objeto.inicio()
contador = objeto.mitad(numero)
print "la suma de los multiplos de 3 es:", contador


