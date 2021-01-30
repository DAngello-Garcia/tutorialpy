firstDictionary = {'Colombia':'Bogotá','Alemania':'Berlín','Canadá':'Ottawa','Rusia':'Moscú'}
print(firstDictionary['Colombia'])
firstDictionary['Italia'] = 'Madrid'
print(firstDictionary)
firstDictionary['Italia'] = 'Roma'
print(firstDictionary)

del firstDictionary['Canadá']
print(firstDictionary)

# Combinaciones de tipos de datos

miLista = ['Perú','US','Francia']
secondDictionary = {miLista[0]:'Lima',miLista[1]:'Washington',miLista[2]:'París'}

otroDic = {'Colombia':'Bogotá','Alemania':'Berlín','Hola':[1,2,'péguelo']}

print(otroDic['Hola'])

# Diccionario dentro de otro diccionario

print(firstDictionary.keys())
print(firstDictionary.values())
print(len(firstDictionary))