# -*- coding: utf-8 -*-
print "medio de tres numeros"

class itachi:
	def sasuke(self):
		a = int(raw_input("numero 1:"))
		b = int(raw_input("numero 2:"))
		c = int(raw_input("numero 3:"))
		lista = [a, b, c]
		return lista
	def naruto(self, a, b, c):
		if a < b:
			if b < c:
				vector = [b]
			elif a < c:
				vector = [c]
			else:
				vector = [a]
		elif a < c:
			vector = [a]
		elif c < b:
			vector = [b]
		else:
			vector = [c]
		return vector



shisui = itachi()
lista = shisui.sasuke()
obito = shisui.naruto(lista[0], lista[1], lista[2])
print "el medio es %d" % (obito[0])

