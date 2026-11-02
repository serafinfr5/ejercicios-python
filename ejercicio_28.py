inferior = int(input("Mínimo: "))
superior = int(input("Máximo: "))

while inferior >= superior:
    print("¡Error! El mínimo tiene que ser menor que el máximo.")
    inferior = int(input("Mínimo: "))
    superior = int(input("Máximo: "))

suma_dentro = 0
cuenta_fuera = 0
igual_a_limites = "No"

while True:
    num = int(input("Introduce un número (0 para terminar): "))
    if num == 0:
        break 
        
    if num > inferior and num < superior:
        suma_dentro += num
        
    if num < inferior or num > superior:
        cuenta_fuera += 1
        
    if num == inferior or num == superior:
        igual_a_limites = "Sí"

print(f"\nSuma de los de dentro: {suma_dentro}")
print(f"Números fuera del intervalo: {cuenta_fuera}")
print(f"¿Se introdujo algún límite?: {igual_a_limites}")
