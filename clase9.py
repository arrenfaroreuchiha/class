# -*- coding: utf-8 -*-
print "promedio de materias y calificaciones"

class eduardo:
	def andres(self):
		materias = int(raw_input("cuantas materias:"))
		return materias

	def john(self, materias):
		i = 0
		promedio = 0
		condicional = 0
		condicional1 = 0
		for i in range (materias):
			notas = int(raw_input("puntaje:"))
			condicional = condicional + notas#suma de notas
			creditos = float(raw_input("creditos:"))
			condicional1 = condicional1 + creditos#suma de creditos
		lista = [condicional, condicional1]
		return lista

	def levi(self, condicional, materias):
		promedio = condicional / materias
		promedio
		return promedio
	


andrea = eduardo()
materias = andrea.andres()
lista = andrea.john(materias)
promedio = andrea.levi(lista[0], materias)
print "suma de notas finales es:", lista[0]#suma de notas
print "suma de creditos finales es:", lista[1]#suma de creditos
print "promedio del semestre es:", promedio


