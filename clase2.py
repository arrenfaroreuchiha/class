# -*- coding: utf-8 -*-
print "mayor, medio y menor"

class itachi:
    def sasuke(self):
        a = int(raw_input("numero a:"))
        b = int(raw_input("numero b:"))
        c = int(raw_input("numero c:"))
        lista = [a, b, c]
        return lista
    def madara(self, a, b, c):
        if a < b:
            if b < c:
                vector = [b, a, c]
            elif a < c:
                vector = [c, a, b]
            else:
                vector = [a, c, b]
        elif a < c:
            vector = [a, b, c]
        elif c < b:
           vector = [b, c, a] 
        else:
          vector = [c, b, a]
        return vector


naruto = itachi()
lista = naruto.sasuke()
obito = naruto.madara(lista[0], lista[1], lista[2])
print "el medio es %d el menor es %d el mayor es %d" %(obito[0], obito[1], obito[2])
