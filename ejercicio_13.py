numero = float(input("Introduce un número: "))

raiz_cuadrada = numero ** 0.5 if numero >= 0 else "No real"

if numero >= 0:
	raiz_cubica = numero ** (1/3)
else:
	raiz_cubica = -abs(numero) ** (1/3)

print(f'Raiz Cuadrada: {raiz_cuadrada}')
print(f'Raiz cubica: {raiz_cubica}')
