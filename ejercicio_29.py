base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente < 0:
    print("Requiere un exponente positivo.")
else:
    resultado = 1
    for i in range(exponente):
        resultado *= base
    print(f"El resultado de la potencia es: {resultado}")
