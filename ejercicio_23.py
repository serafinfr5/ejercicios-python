suma = 0
contador = 0

while True:
    numero = float(input("Introduce un número: "))
    if numero == 0:
        break
    suma += numero
    contador += 1

print (f'Suma de los números: {suma}')
if contador > 0:
    media = suma / contador
    print(f'Media de los números: {media:.2f}')
else:
    print("No se introdujeron números válidos para calcular la media.")
