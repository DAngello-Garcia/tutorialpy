def evenNumbers(lim):
    n = 1
    lista = []
    while n<lim:
        lista.append(n*2)   #función
        n+=1
    return lista

print(evenNumbers(3))
print('Fin')

def evenNumbers(lim):
    n = 1
    while n<lim:
        yield n*2       #generador
        n+=1

resultado = evenNumbers(11)
print(next(resultado))
print('Fin')
print(next(resultado))
print('Fin2')
for i in resultado:
    print(i)

def retCities(*ciudades):   #el * antes del parámetro, significa número indeterminado de argumentos y en forma de tupla
    for elemento in ciudades:
        # for sub in elemento:
            # yield sub
            yield from elemento

cities = retCities('Bogotá', 'Medellín', 'Cali')
print(next(cities))
print(next(cities))
