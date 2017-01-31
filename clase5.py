# -*- coding: utf-8 -*-
print "suma de numeros pares"

class obito:
    def kakachi(self):
        numero = int(raw_input("cantidad de numeros:"))
        return numero

    def gai(self, numero):
        i = 1
        par = 0
        impares = []
        a = 0
        for i in range (numero):
            numero2 = int(raw_input("cantidad de numeros:"))
            contador = numero2
            contador = numero2 % 2
            if contador == 0:
                par = par + numero2
            else:
                # impares.append([])
                # impares[a].append(numero2)
                impares.insert(a, numero2)
                a += 1

        lista = [par, impares]
        return lista

objeto = obito()

numero = objeto.kakachi()
lista = objeto.gai(numero)
total = lista[0]
print "La suma de los pares es, ", total
# impares = lista[1]
# for i, x in 5(impares):
#     print "El numero impar es: ", x

for x in lista[1]:
    print "El numero impar es: ", x

