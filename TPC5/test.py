from TPC5_functions import *
import random

#teste
'''texto = 'sadsadss'
texto_centrado = texto.center(100)+ '|'

print(texto)
print(texto_centrado + texto_centrado)'''



#cinema
a = [['a',100, [random.randint(0, 100) for i in range(10)]],['b', 200,[random.randint(0, 100) for j in range(10)]],['c', 300,[]]]
#print(a)

b = ordenaLugares(a)
#print(b)


#testes
guardarCinema('lista_de_cinemas_teste.txt', b)


CINEMA = lerCinema('lista_de_cinemas_teste.txt')
#print(CINEMA)
showCinema(CINEMA)

showMovies(CINEMA)

print(filmeExiste(CINEMA, 'a'))

guardarCinema('lista_de_cinemas_teste.txt', CINEMA)