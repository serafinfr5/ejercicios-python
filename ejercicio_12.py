x1 = float (input("Valor x1: "))
y1 = float(input("Valor y1: "))
x2 = float(input("Valor x2: "))
y2 = float(input("Valor y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(f'La distancia entre los dos puntos es: {distancia:.2f}')
