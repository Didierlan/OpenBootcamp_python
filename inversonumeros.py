
numeros = []
for i in range(0, 101):
   numeros.append(i)

numeros.sort(reverse=True)
print(numeros)


#Esta es otra manera de las pros 
rango_1_100 = range(1,101)

# Se muestra el rango de números desde 100 hasta 1
for i in reversed(rango_1_100):
    print(f"- {i}")
