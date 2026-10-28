numero = int(input("Introduce un número entero: "))
if numero < 0:
	print("No pueden ser números negativos")
else:
	factorial = 1
	for i in range (1, numero + 1):
		factorial *= i
	print(f'El factorial de {numero}! es {factorial}')
