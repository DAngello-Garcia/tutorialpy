# Las listas son conjuntos de elementos ordenados, mutables (que pueden ser modificados) y permiten valores duplicados.
lista = [1, 'Hola', 3.17, True]
print(lista)

listaPro = [2, False, lista]
print(listaPro)

print(lista[2])
lista[1] = 3
lista.remove(3.17)
lista.insert(2,'Péguelo')
print(lista)
# max, min, count
print(lista.reverse())

print(2 in listaPro)