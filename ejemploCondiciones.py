#Una manera interesante
contador = 0
while contador < 10:
    contador+= 1
    if contador%2 == 0:
        print(contador, " Es par")
        continue
    print(contador , " No es par")
print('fin del programa ')


#La manera de siempre
contador = 0
while contador <= 10:
    if(contador%2 == 0):
        print(contador, " Es par")
    else:
        print(contador, "NO es par")
    contador += 1
print('termina el programa')


#Esta es con menos lineas hace lo mismo
for i in range(1,11):
    if(i%2 == 0):
        print(i ,' Es par')
    else:
        print(i , 'no es par')
print('Fin del programa lol')


#esto esta  mas loco lol

contador = 1  
lista = []
while contador <= 10:
    lista.append(contador)
    contador+=1

#con este podemos saber si el elemento de la derecha se encuentra en la lista   
if 7 in lista:
    print('si hay numero')



#Ordenar listas con sorted 
lista = [3,7,1,4,9,0]
print(lista)
listaOrdenada = sorted(lista)
print(listaOrdenada)
print("")
print("")

#Esta es una manera de dar la vuelta a un array
listaAlRevez = sorted(lista, reverse=True)
print(listaAlRevez)

#Y esta tambien 
print(list(reversed(listaOrdenada)))
