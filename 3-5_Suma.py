print('Encuentra la suma de todos los múltiplos de 3 o 5 por debajo de 1000.')
'''la funcion range debe tener dos parametros
poner bien los bloques identadores
'''
suma = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        suma += i
        print(i,suma)
print(suma)

mult = 0
for i in range(1, 1001):
    if i % 2 == 0 or i % 3 == 0:
        mult = mult +1
print(mult)
