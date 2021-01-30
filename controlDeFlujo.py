# if
var = 8
if var==7:
    print('Correcto')
elif var<5:
    print('Correctont')
else: #aquí es como un default
    print('Ahora sí')

#for
lista = ['h', 'g', 'j']
for num in lista:
    print(num+'\n')

for i in range(3):
    print(f'Valor: {i}')

for i in range(2,7):
    print(i)

for i in range(2,25,3):
    print(i)

for i in range(10,2):
    print(i)

for i in reversed(range(2,13,3)):
    print('hola'+str(i))

# while
num = 3
while num<=5:
    num+=1
    print('oc')

# switch
# No existe

for i in 'nombre':
    if i == 'm':
        continue
    print('Letras de '+i)

# pass: no hace nada
# break: igual que en C y Java

email = input('Introduce tu email: ')
for i in email:
    if i=='@':
        arroba = True
        break
else:
    arroba = False

print(str(arroba)+' '+email)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
