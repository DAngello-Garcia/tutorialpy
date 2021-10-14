areaTriangulo = lambda base, altura: base*altura/2
print(areaTriangulo(2,3))

def numPar(num):
    if num%2==0:
        return True

numeros = [2,5,14,18,17]
print(list(filter(numPar,numeros)))

# class map(object)
#  |  map(func, *iterables) --> map object
#  |
#  |  Make an iterator that computes the function using arguments from
#  |  each of the iterables.  Stops when the shortest iterable is exhausted.
#  |
#  |  aplica la misma func a todos los elementos de *iterables
